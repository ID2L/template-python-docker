# Utilisation de l'image Python officielle (vous pouvez changer la version selon vos besoins)
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier requirements.txt
COPY requirements.txt .

# Installation des dépendances du projet
RUN pip install -r requirements.txt 