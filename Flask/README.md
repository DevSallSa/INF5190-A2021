# Remarques et informations utiles

L'enoncé du laboratoire est disponible [ici](./enonce.md).

## Création d'un environnement virtuel :

1. Première possibilité :
````
$ python3.9 -m venv env
````

- `-m` permet le changement de module.
- `venv` le module qui permet la création d'un environnement virtuel.

Pour l'activation :

````
$ source env/bin/activate
````

Pour la désactivation :

`````
$ deactivate
`````

2. Deuxième possibilité :
````
$ pip3 install virtualenv
$ virtualenv -p python3.9 env
````

Pour l'activation et la désactivation utiliser les commandes précédentes.

## Conviguration du PATH du shell pyenv

1. Sur macOs :

````
$ ln -s -f /usr/local/bin/python3.9.7 /usr/local/bin/python
````

2. Sur Ubuntu :

````
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9.7 1

$ sudo update-alternatives --config python

$ sudo update-alternatives  --set python /usr/bin/python3.9.7
````

## Lancer l'application
Pour cet exercice il est nécessaire d'intaller `flask` (vu durant la séance) :
````
$ pip install flask
````

**Remarque** : Etant surs de la version python utilisée (3.9.7 dans notre cas), il n'est pas nécessaire de préciser la version de `pip`.

Pour créer le fichier `requirements.txt`:

````
$ pip freeze > requirements.txt
````

Pour lancer directement le corrigé disponible sur le depot :
````
$ pip install -r requirements.txt
$ make
````


## Remarques importantes :

L'URL est l'identifiant unique d'une *ressource* sur le web. La route est un chemin vers cette ressource.

L'URL contient :
- Le protocole de communication utilisé (http, https.. dans notre cas)
- Le nom du domaine ou l'adresse IP (exemple : uqam.ca)
- Le port (pour le protocole http, le port est part défaut 80, sinon il est précisé après le nom du domaine)
- Une route (qui est un chemain vers une ressource)
- Des paramètres

Http est le protocole qui permet l'échange de pages web.

Jinja est un moteur de templation. Plutot que de générer des chaines de caractères directement dans le backend nous allons utiliser des templates.
Les templates sont simplement des fichiers HTML avec probablement des annotations en Jinja.

Ces fichiers vont par défaut se trouver dans le répértoire `templates` qui doit etre au meme niveau que le script python contenant les routes de l'application.

De façon plus vulgaire, Jinja va permettre un echange d'informations du backend (les scripts python) vers le frontend (le fichier HTML).



 