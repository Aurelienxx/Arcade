# Pointeur.java

 Classe Pointeur
=================
Cette classe est destinée à gérer différents éléments d'affichage dans un environnement graphique, tels que des textures, une valeur et des objets géométriques. Elle est associée à d'autres classes pour constituer un système plus large.

Attributs
---------
- value (int): Valeur représentant l'index du jeu à lancer dans Graphique.tableau.
- triangleGauche (Texture): Texteure représentant un triangle en gauche.
- triangleDroite (Texture): Texteure représentant un triangle en droite.
- rectangleCentre (Texture): Texteure représentant un rectangle dans le centre.

Méthodes
---------
- Pointeur(): Constructeur qui initialise les attributs de classe.
- lancerJeu(ClavierBorneArcade clavier): Méthode appelée lorsque le bouton du joueur 1 est pressé. Elle lance le jeu correspondant en bas de la fenêtre, en interrompant la musique de fond et en attendant la fin de l'exécution du jeu pour reprendre le contrôle sur le menu.
- getValue(): Retourne la valeur de l'attribut value.
- setValue(int value): Définit la valeur de l'attribut value.
- getTriangleGauche(): Retourne la Texteure représentant le triangle en gauche.
- setTriangleGauche(Texture triangleGauche): Définit la Texteure représentant le triangle en gauche.
- getTriangleDroite(): Retourne la Texteure représentant le triangle en droite.
- setTriangleDroite(Texture triangleDroite): Définit la Texteure représentant le triangle en droite.
- getRectangleCentre(): Retourne la Texteure représentant le rectangle dans le centre.
- setRectangleCentre(Texture rectangleCentre): Définit la Texteure représentant le rectangle dans le centre.

Utilisation
------------
Pour utiliser la classe Pointeur, instancier un objet avec `Pointeur p = new Pointeur();`, puis appeler les méthodes appropriées pour modifier ses attributs et utiliser ses fonctionnalités.