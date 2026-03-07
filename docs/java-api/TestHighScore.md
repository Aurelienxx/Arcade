# TestHighScore.java

 ## Description
 La classe TestHighScore s'occupe de générer et gérer les classements dans un jeu. Elle permet de demander à l'utilisateur de saisir son nom, enregistrer le résultat du jeu et gérer le classement final.

## Responsabilités
- Générer et gérer les classements dans un jeu.
- Demander l'enregistrement du nom de l'utilisateur.
- Enregistrer le score dans un fichier spécifique.

## Attributs
- Nom de l'utilisateur : utilisé pour enregistrer le classement et le nom du joueur.

## Méthodes publiques
- **public static void main(String[] args)** : point d'entrée du programme, qui démarre le processus d'enregistrement des scores et gère le classement final.

## Relations
- Fenêtre : pour afficher l'interface graphique et gérer les événements clavier.
- ClavierBorneArcade : pour capturer les événements clavier et gérer les interactions du joueur avec le jeu.
- HighScore : pour demander l'enregistrement du nom du joueur et enregistrer le score dans le fichier.
- Texture : pour afficher les images dans la fenêtre du jeu.

## Utilisation dans le projet
TestHighScore est une classe qui s'utilise dans le contexte d'un jeu pour gérer le classement et enregistrer les performances des joueurs. Elle permet d'établir un classement final et de célébrer les performances remarquables du jeu en les enregistrant dans un fichier.