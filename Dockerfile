# 1. Używamy obrazu Pythona
FROM python:3.11-slim

# 2. Tworzymy katalog roboczy w kontenerze
WORKDIR /app

# 3. Kopiujemy pliki projektu do kontenera
COPY . .

# 4. Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# 5. Otwieramy port 5000
EXPOSE 5000

# 6. Uruchamiamy aplikację
CMD ["python", "app.py"]
