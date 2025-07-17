# Weatherbot 🌦️

Weatherbot to prosty bot w Pythonie, który codziennie pobiera dane pogodowe z API OpenWeatherMap i wysyła je na podany e-mail.

## 🔧 Funkcje

- Pobiera aktualne dane pogodowe dla wybranego miasta
- Wysyła e-mail z podsumowaniem pogody
- Łatwy do modyfikacji i rozbudowy

## 🧠 Technologie

- Python
- requests
- smtplib
- OpenWeatherMap API

## 🚀 Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Firynt/Weatherbot.git
Zainstaluj zależności:

bash
Kopiuj
Edytuj
pip install -r requirements.txt
Utwórz plik .env w folderze projektu i wpisz dane:

ini
Kopiuj
Edytuj
EMAIL=twoj_email@example.com
EMAIL_PASSWORD=twoje_haslo
API_KEY=twoj_klucz_api
CITY=twoje_miasto
Uruchom bota:

bash
Kopiuj
Edytuj
python weatherbot.py
📌 Uwagi
Upewnij się, że masz włączony dostęp dla aplikacji mniej bezpiecznych (jeśli używasz Gmaila)

Możesz zautomatyzować uruchamianie np. przez crona lub Windows Scheduler

👨‍💻 Autor
Filip Hanczyn
GitHub: https://github.com/Firynt
