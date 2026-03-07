# BoiteImage.java

 # BoiteImage

BoiteImage est une classe étendue de Boite dans le contexte d'un programme. Elle gère les aspects concernant une boîte qui contient une image.

## Description générale
La classe BoiteImage gère les aspects concernant une boîte contenant une image. Elle étend la classe Boite, ajoutant une texture nommée image à l'objet.

## Attributs principaux
- image : texture représentant l'image contenue dans la boîte.

## Méthodes publiques avec leurs descriptions
- BoiteImage(Rectangle rectangle, String chemin) : Constructeur de BoiteImage prenant en paramètres un Rectangle représentant la position et la taille de la boîte et un chemin vers le fichier de l'image.
- getImage() : Méthode qui retourne la texture de l'image.
- setImage(String chemin) : Méthode qui permet de modifier la texture de l'image en chargant une nouvelle image de la même taille.

## Exemple d'utilisation
Dans un programme de jeu 2D, les images pourraient être gérées en utilisant la classe BoiteImage. Par exemple :

```java
BoiteImage boiteImage = new BoiteImage(new Rectangle(new Point(0, 0), new Dimension(400, 320)), "images/monDossierImages/");
boiteImage.setImage("images/monDossierImages/monImage.png");
```
Dans ce code, une boîte image est créée avec une position et une taille spécifiques, puis une image est chargée à partir du dossier images.

## Sources et références
- MG2D : bibliothèque de classes pour le développement de jeux 2D.
- Boite : classe parent de BoiteImage et Boite.
- Texture : classe servant à charger et gérer les images.