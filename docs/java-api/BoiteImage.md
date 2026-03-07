# BoiteImage.java

 Description
La classe BoiteImage représente une boîte à l'image, qui hérite de la classe abstraite Boite. Elle représente une zone géométrique délimitée par une image. Son objectif est de rendre visible une image dans un espace géométrique délimité.

Responsabilités
- Gérer le rendu de l'image en 2D à l'intérieur de la zone géométrique délimitée
- Mettre à disposition la texture associée à l'image

Attributs
- image : Représente la texture de l'image affichée à l'intérieur de la zone géométrique délimitée

Méthodes publiques
- BoiteImage(Rectangle rectangle, String chemin) : Crée une nouvelle boîte à l'image en passant en paramètre le rectangle et le chemin du fichier d'image
- getImage() : Renvoie la texture de l'image associée à l'objet
- setImage(String chemin) : Charge une nouvelle image en remplaçant l'image actuelle par celle du fichier spécifié par le chemin

Relations
- BoiteImage interagit avec la classe Rectangle en utilisant son objet pour définir l'espace géométrique où doit être affichée l'image
- BoiteImage interagit avec la classe Texture pour gérer la texture associée à l'image

Utilisation dans le projet
La classe BoiteImage est probablement utilisée dans le contexte d'un jeu vidéo ou d'un environnement graphique, permettant de visualiser et manipuler des images en 2D dans des zones géométriques délimitées.