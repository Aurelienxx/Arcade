IUT du Littoral Côte d'Opale (IUT)
====================================
Documentation d'installation de la borne d'arcade
----------------------------------

- Dusannier Léothen
- Fontaine Aurélien

# Ajout d'un jeu à la borne

Ajoutez les fichiers du jeu dans le dossier **projet**

Créer un fichier **.sh** du même nom que le jeu, le fichier sh doit se présenté sous cette forme : 

## JAVA 

```
cd projet/nomDuJeu
love .

javac nomExecutable.java
java nomExecutable
```
## PYTHON
```
cd projet/nomDuJeu

python nomExecutable.py
```

Dans le dossier de votre jeu ajoutez un fichier **bouton.txt** avec la liste des touche, ainsi qu'un fichier **description.txt** avec une courte description.

N'oubliez pas d'y inclure un fichier png qui se nomme 'photo_small.png' qui servira de miniature pour le jeu dans le menu de la borne d'arcade. 