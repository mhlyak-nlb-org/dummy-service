# 1️⃣ Base image
FROM python:3.12.10-slim

# 2️⃣ Nastavi delovno mapo v containerju
WORKDIR /app

# 3️⃣ Kopiraj requirements datoteko (če obstaja)
COPY requirements.txt .

# 4️⃣ Namesti Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Kopiraj preostalo aplikacijo
COPY . .

# 6️⃣ Nastavi port (če aplikacija posluša, npr. 5000)
EXPOSE 8000

# 7️⃣ Definiraj ukaz, ki zažene aplikacijo
CMD ["python", "app.py"]