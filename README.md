# OCP10: Softdesk API

Application de suivi des problèmes pour les trois plateformes (site web, applications Android et iOS)


## Installation & lancement

Récupérez le dépôt localement
```
git clone https://github.com/nopalpite/OCP10.git
```
Placez vous dans le dossier OCP10, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Installez ensuite les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous dans le sous-dossier softdesk et lancez les commandes suivantes:
```
python manage.py makemigrations
```
Puis: 
```
python manage.py migrate
```
Lancez le serveur: 
```
python manage.py runserver
```

## documentation de l'api

Vous pouvez maintenant tester toutes le fonctionnalité de l'api en vous appuyant sur la documentation: https://documenter.getpostman.com/view/26061791/2s93JwPhtQ

## conformité pep8

Placez vous dans le dossier OCP10, et executez la commande suivante:

```
flake8 --format=html --htmldir=flake-report softdesk
```

Vous pouvez alors consulter le rapport dans le dossier flake-report, en ouvrant le fichier index.html dans un navigateur