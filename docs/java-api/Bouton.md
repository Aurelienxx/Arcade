# Bouton.java

 **Bouton.java** est une classe Java qui définit un bouton dans le contexte d'un jeu. Elle comprend les attributs suivants :

- texte: Un objet `Texte` représentant le texte affiché sur le bouton.
- chemin: Une chaîne de caractères représentant le chemin d'accès vers le dossier contenant les éléments du jeu (utilisé pour créer les boutons).
- nom: Une chaîne de caractères représentant le nom du bouton.
- texture: Un objet `Texture` représentant la texture de l'icône du bouton.
- numeroDeJeu: Un entier représentant l'ordre dans lequel les boutons seront initialisés.

La classe Bouton.java comprend les méthodes suivantes :

- Constructeur par défaut: Initialise toutes les propriétés du bouton à leur valeur par défaut.
- Constructeur: Initialise les propriétés du bouton à partir des valeurs fournies.
- `remplirBouton()`: Fonction statique qui charge les boutons et leurs propriétés à partir d'un dossier contenant les éléments du jeu.
- getters et setters pour chacune des propriétés du bouton.

L'utilisation générale de Bouton.java consiste à utiliser l'API pour créer des boutons à partir d'un dossier et de ses fichiers et à utiliser les méthodes pour modifier les propriétés du bouton.