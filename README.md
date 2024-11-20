# gestion-de-contact

Une application de bureau simple en Python pour gérer vos contacts, avec une interface utilisateur graphique construite à l'aide de           Tkinter   et une base de données SQLite.


* Fonctionnalités

-Ajouter un contact : Enregistrez un nouveau contact avec un nom, prénom, numéro de téléphone et adresse e-mail.

-Afficher les contacts : Affichez tous les contacts enregistrés dans une liste déroulante.

-Rechercher un contact : Recherchez des contacts par nom, prénom ou numéro de téléphone.

-Modifier un contact : Mettez à jour les informations d'un contact existant.

-Supprimer un contact : Supprimez un contact de la base de données.

* Structure du Projet

├── main.py         # Point d'entrée principal de l'application

├── ui.py           # Gestion de l'interface utilisateur avec Tkinter

├── database.py     # Gestion de la base de données SQLite


├── contact.py      # Définition de la classe Contact

├── contacts.db     # Base de données SQLite (générée automatiquement)

├── README.md       # Documentation du projet

* Pré-requis

Avant de lancer l'application, assurez-vous d'avoir installé les éléments suivants :

1. Python 3.8 ou supérieur : Téléchargez-le depuis python.org.
2. Bibliothèques requises :
    Tkinter (inclus avec Python par défaut)

     SQLite (inclus avec Python par défaut)

Aucune installation supplémentaire de bibliothèques Python n'est nécessaire.

* Installation

1. Clonez ce dépôt ou téléchargez le code source.

2. Naviguez dans le dossier du projet via le terminal ou l'invite de commande.

3. Exécutez le script main.py : python main.py

La fenêtre de l'application devrait apparaître.

* Utilisation

1. Ajouter un contact :

-Remplissez les champs "Nom", "Prénom", "Téléphone" et (optionnellement) "Email".

-Cliquez sur "Ajouter Contact" pour enregistrer le contact.

2. Afficher les contacts :

-Tous les contacts sont affichés dans la liste déroulante au centre de l'application.

3. Rechercher un contact :

-Entrez un mot-clé (nom, prénom ou téléphone) dans le champ de recherche.

-Cliquez sur "Rechercher" pour filtrer les résultats.

3. Modifier un contact :

-Sélectionnez un contact dans la liste.

-Cliquez sur "Modifier Contact" et mettez à jour les informations.

4. Supprimer un contact :

-Sélectionnez un contact dans la liste.

-Cliquez sur "Supprimer Contact" pour l'effacer.

* Développement

Le projet est structuré en plusieurs fichiers pour faciliter la maintenance :

contact.py : Contient la classe Contact, qui représente les objets contacts.

database.py : Fournit les fonctions CRUD pour la base de données SQLite.

ui.py : Contient les fonctions pour gérer les interactions avec l'utilisateur via Tkinter.

main.py : Assemble tout pour créer l'application principale.

* Capture d'écran
![Annotation 2024-11-20 162243](https://github.com/user-attachments/assets/2fce5b6a-de3d-48de-a205-a50f75565068)

![Annotation 2024-11-20 172348](https://github.com/user-attachments/assets/304e0850-d0b1-4650-9e0b-b52d15b51758)

![Annotation 2024-11-20 173045](https://github.com/user-attachments/assets/22e33ea7-318b-4801-b1d5-6ffe980e285c)

