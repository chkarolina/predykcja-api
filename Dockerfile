# Używamy lekkiego obrazu Pythona
FROM python:3.10-slim

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiujemy pliki do kontenera
COPY requirements.txt .
COPY app.py .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Wystawiamy port 5000
EXPOSE 5000

# Uruchamiamy aplikację Flask
CMD ["python", "app.py"]
