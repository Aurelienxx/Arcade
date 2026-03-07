# Boite.java

 ## Classe Abstraite Boite

La classe abstraite **Boite** représente une boîte géométrique. Elle gère une structure interne en tant que rectangle. Cette classe est conçue pour être une abstraction d'une boîte plus complexe.

## Attributs Principaux

1. `Rectangle rectangle` : Cette propriété stocke une instance de Rectangle, représentant le rectangle intérieur de la boîte.

## Méthodes publiques

1. `Boite(Rectangle rectangle)` : Constructeur prenant un Rectangle en argument, qui sera utilisé pour initialiser la propriété rectangle.

2. `Rectangle getRectangle()` : Méthode permettant d'accéder au Rectangle intérieur de la boîte.

3. `void setRectangle(Rectangle rectangle)` : Méthode permettant de modifier le Rectangle intérieur de la boîte.

## Exemple d'utilisation (si applicable)

Pour utiliser la classe Boite, vous pouvez suivre ces étapes :

1. Créer un Rectangle correspondant à la boîte :

   ```java
   Rectangle rectangle = new Rectangle(width, height);
   ```

2. Créer une instance de Boite en passant le Rectangle en paramètre au constructeur :

   ```java
   Boite boite = new Boite(rectangle);
   ```

3. Accéder aux informations du Rectangle intérieur de la boîte :

   ```java
   Rectangle interneRectangle = boite.getRectangle();
   ```

4. Modifier le Rectangle intérieur de la boîte :

   ```java
   Rectangle nouvelleDimension = new Rectangle(largeur, hauteur);
   boite.setRectangle(nouvelleDimension);
   ```