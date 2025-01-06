# Template Python Docker

Ce template fournit une configuration Docker minimale pour vos projets Python.

## Prérequis

- Python installé sur votre machine de développement
- pipreqs installé : `pip install pipreqs`

## Téléchargement du template

Pour utiliser ce template sans l'histori scriptque Git, vous avez deux options :

1. Via l'interface GitHub :
   - Cliquez sur le bouton vert "Use this template"
   - Choisissez "Create a new repository"
   - Ou "Download ZIP" pour télécharger sans créer de repository

2. Via la ligne de commande :
```bash
mv .git .git_tmp
git clone --depth 1 https://github.com/ID2L/template-python-docker.git .
rm -rf .git
mv .git_tmp .git
```

## Utilisation du Dockerfile

1. Construction de l'image :
```bash
docker build -t mon_app_python .
```

2. Exécution du conteneur :
```bash
docker run -it mon_app_python
```

## Gestion des dépendances

Pour générer automatiquement le fichier `requirements.txt` à partir de votre code :

```bash
pipreqs --force .
```

Cette commande va :
- Analyser tous les fichiers Python de votre projet
- Identifier toutes les dépendances utilisées
- Créer ou mettre à jour le fichier `requirements.txt`

> Note : L'option `--force` permet d'écraser le fichier requirements.txt s'il existe déjà.
