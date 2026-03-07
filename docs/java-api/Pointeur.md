# Pointeur.java

 ## Description générale de la classe Pointeur

Cette classe `Pointeur` est un objet permettant de gérer les éléments graphiques d'un jeu. Il contient plusieurs attributs, notamment un nombre entier `value`, deux textures `triangleGauche` et `triangleDroite` représentant des objets graphiques, et une texture `rectangleCentre`. Les différents attributs sont initialisés dans le constructeur de la classe.

La classe `Pointeur` dispose d'une méthode `lancerJeu` qui permet de lancer le jeu à l'aide d'un objet `ClavierBorneArcade`. Lorsque le joueur appuie sur le bouton 1 de la manette, le jeu en cours est lancé et un processus est exécuté afin de lancer le jeu sur le fichier correspondant. Le processus est ensuite attendu jusqu'à sa fin. Après cela, le contrôle est redonné sur le menu.

La classe `Pointeur` permet également de gérer divers autres attributs, tels que la valeur, les textures, et d'accéder et modifier ces attributs via des méthodes publiques. Ces méthodes incluent `getValue`, `setValue`, `getTriangleGauche`, `setTriangleGauche`, `getTriangleDroite`, `setTriangleDroite`, `getRectangleCentre`, et `setRectangleCentre`.