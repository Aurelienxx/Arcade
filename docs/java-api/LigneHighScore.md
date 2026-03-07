# LigneHighScore.java

 # LigneHighScore Class Documentation

LigneHighScore est une classe Java destinée à gérer les données d'une ligne de scores. Elle permet de gérer différents types de représentations d'objets ainsi que leurs propriétés et méthodes.

## Attributs

### nom
Type: String
Description: Nom de la personne ayant obtenu le score. Par défaut est "AAA".

### score
Type: int
Description: Score obtenu par la personne. Par défaut est 0.

## Constructeurs

### LigneHighScore()
Description: Construit un nouvel objet de type LigneHighScore avec un nom par défaut et un score par défaut.

### LigneHighScore(String nnom, int sscore)
Description: Construit un nouvel objet de type LigneHighScore avec un nom normalisé (maximum 3 caractères) ou par défaut "AAA" et un score normalisé (supérieur à 0 sinon sera 0).

### LigneHighScore(LigneHighScore l)
Description: Construit un nouvel objet de type LigneHighScore en copiant les valeurs des paramètres de la classe source.

### LigneHighScore(String str)
Description: Construit un nouvel objet de type LigneHighScore en analysant la chaîne de caractères passée en paramètre. Le nom sera normalisé et le score sera déduit. Si les données sont incorrectes, le nom sera par défaut "AAA" et le score sera 0.

## Méthodes

### int getScore()
Description: Renvoie le score associé à l'objet.

### String getNom()
Description: Renvoie le nom associé à l'objet.

### String toString()
Description: Retourne une représentation de l'objet sous la forme nom-score, par exemple "Nom-Score".

## Exemple d'Utilisation

```java
// Exemple de création d'un objet LigneHighScore à partir d'un autre objet
LigneHighScore lhs1 = new LigneHighScore("Jean", 1000);
LigneHighScore lhs2 = new LigneHighScore(lhs1);

// Exemple de lecture et affichage d'un objet LigneHighScore
LigneHighScore lhs3 = new LigneHighScore("John", 3000);
System.out.println("Le joueur " + lhs3.getNom() + " a un score de " + lhs3.getScore() + " points.");

// Exemple de lecture et affichage d'un objet LigneHighScore sous forme de chaîne
LigneHighScore lhs4 = new LigneHighScore("Marie", 200);
System.out.println("Le joueur " + lhs4.toString() + " a un score de " + lhs4.getScore() + " points.");

// Exemple d'utilisation d'un constructeur pour le lire depuis une chaîne de caractères
String ligne = "Sam-4000";
LigneHighScore lhs5 = new LigneHighScore(ligne);
System.out.println("Le joueur " + lhs5.getNom() + " a un score de " + lhs5.getScore() + " points.");
```