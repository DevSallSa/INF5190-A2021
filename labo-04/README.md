# Installation avec Vagrant

1. Démarrer la machine virtuelle

```bash
# requis: vagrant + virtualbox
vagrant up
```

2. Connecter vous à la VM via vagrant

```bash
# À partir de la racine du projet
vagrant ssh
```

3. Activer l'environnement virtuel python dans la VM

```bash
source /home/vagrant/labo04-env/bin/activate
```

Vous devriez voir apparaitre le nom de votre environnement virtuel (labo-04) entre parenthèse devant votre command prompt.

4. Déplacer vous à la racine du projet

```bash
cd /vagrant
```

5. Installer les requirements du projet.

```bash
# Installer les dépendances python
sudo pip install -r requirements.txt

# Configurer votre fichier d'environnement
cp  /vagrant/app/.env.example /vagrant/app/.env
```

6. Déplacez-vous dans le répertoire /vagrant/app

```bash
cd /vagrant/app
```

7. Lancer Flask !

```bash
flask run
```

# Tailwind CSS configuration.

Reference: https://tailwindcss.com/docs/installation

1. Initialiser votre fichier de configuration.

```bash
npx tailwindcss init
```

1. Adapter votre fichier de configuration pour purger les fichiers HTML.

```bash
# tailwind.config.js
module.exports = {
    mode: 'jit',
    purge: ["./app/templates/*.html"],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
};
```

3.  Lancer le compileur de tailwind en ligne de commande pour l'intégrer à votre projet.

L'option `--watch` permettera de détecter les changements et recompiler.

```bash
# From the root
npx tailwindcss -o app/static/styles/tailwind.css --watch
```
