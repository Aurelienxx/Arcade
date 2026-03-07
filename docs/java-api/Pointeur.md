# Pointeur.java

 ## Description
La classe Pointeur représente un contrôle dans un jeu. Elle contient diverses textures, une référence à une classe de jeu et différents attributs. Le constructeur initialise ces textures à partir de différentes images.

## Responsabilités
La classe Pointeur a pour responsabilités :
1. Gérer les textures représentant des éléments du jeu (triangle gauche, triangle droite, rectangle centre).
2. Permettre de gérer le jeu lui-même, en relançant le programme en fonction des interactions avec le clavier.
3. Faciliter la manipulation des différentes valeurs, notamment le nombre d'éléments du tableau, en l'accès aux attributs (getValue, setValue).
4. Permettre d'accéder aux différentes textures et de les modifier si nécessaire.

## Attributs
- value : Contient le numéro du tableau à activer pour lancer le jeu.
- triangleGauche : Texture représentant le triangle gauche du jeu.
- triangleDroite : Texture représentant le triangle droite du jeu.
- rectangleCentre : Texture représentant le rectangle central du jeu.

## Méthodes publiques
- lancerJeu(ClavierBorneArcade clavier) : Permet de relancer le jeu en fonction des interactions du joueur avec le clavier.
- getValue() : Renvoie la valeur actuelle de 'value'.
- setValue(int value) : Définit la nouvelle valeur pour 'value'.
- getTriangleGauche() : Renvoie l'objet Texture représentant le triangle gauche.
- setTriangleGauche(Texture triangleGauche) : Définit le nouvel objet Texture représentant le triangle gauche.
- getTriangleDroite() : Renvoie l'objet Texture représentant le triangle droite.
- setTriangleDroite(Texture triangleDroite) : Définit le nouvel objet Texture représentant le triangle droite.
- getRectangleCentre() : Renvoie l'objet Texture représentant le rectangle central.
- setRectangleCentre(Texture rectangleCentre) : Définit le nouvel objet Texture représentant le rectangle central.

## Relations
La classe Pointeur n'interagit que très légèrement avec d'autres classes dans l'application. Elle utilise des objets Texture qui représentent des éléments du jeu. Le jeu est lui-même représenté par la classe Graphique.

## Utilisation dans le projet
La classe Pointeur est utilisée dans le cadre du développement d'un jeu ou d'un environnement de jeu interactif. Elle permet de gérer différents aspects du jeu, comme la mise en scene, les interactions du joueur et l'intégration de différents éléments visuels.