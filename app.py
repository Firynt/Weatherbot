from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoint: /status
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"success": True, "version": "1.0"})


# Endpoint: /weather
@app.route("/weather", methods=["GET"])
def weather():
    # Przykład z OpenWeatherMap – można też użyć fikcyjnych danych
    API_KEY = "95f16b024acab9bacbd13c8c853b5924"  # <- demo key lub podmień na swój
    city = "Warsaw"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"success": False, "error": data.get("message", "Błąd pobierania danych")}), 400

        # Wyciągamy kilka danych
        result = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
