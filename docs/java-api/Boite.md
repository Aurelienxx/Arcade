# Boite.java

 ## Classe Boite

### Description générale
Classe abstraite représentant une boîte dans un contexte de 2D. La boîte est constituée d'un rectangle.

### Attributs principaux
- rectangle: Rectangle représentant la boîte en 2D.

### Méthodes publiques
- `Boite(Rectangle rectangle)`: Constructeur de la classe Boite, qui prend en paramètre un rectangle et l'utilise pour initialiser l'attribut rectangle de la classe.
- `Rectangle getRectangle()`: Méthode qui retourne la valeur du rectangle représentant la boîte.
- `void setRectangle(Rectangle rectangle)`: Méthode pour modifier la valeur du rectangle représentant la boîte.

### Exemple d'utilisation
```java
// Instanciation d'une boîte avec un rectangle
Rectangle rectangle = new Rectangle(10, 5, 20, 30);
Boite boite = new Boite(rectangle);

// Affichage de la boîte et de son rectangle
System.out.println("La boîte: " + boite);
System.out.println("Le rectangle: " + boite.getRectangle());

// Modification du rectangle de la boîte
Boite.setRectangle(rectangle.scale(2.0));
System.out.println("Le nouveau rectangle: " + boite.getRectangle());
```