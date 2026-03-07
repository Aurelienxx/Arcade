# LigneHighScore.java

 Description : Cette classe, LigneHighScore, représente une ligne de classement dans le jeu. Son objectif principal est de conserver les informations sur les joueurs, leur nom et leur score.

Responsabilités : La classe doit gérer les attributs nom et score pour les joueurs, permettre aux joueurs d'avoir une représentation précise de leurs scores et noms et assurer la gestion des attributs dans différents cas de figure (initialisation, construction par copie, construction à partir de chaine).

Attributs :
- nomAttribut : nom : Représente le nom du joueur
- nomAttribut : score : Représente le score du joueur

Méthodes publiques :
- LigneHighScore() : Construit une nouvelle ligne de classement, avec des valeurs initiales par défaut.
- LigneHighScore(String nnom, int sscore) : Crée une nouvelle ligne de classement en utilisant les arguments fournis, vérifiant que le nom et le score soient appropriés.
- LigneHighScore(LigneHighScore l) : Construit une nouvelle ligne de classement en copiant les valeurs de l'objet donné.
- LigneHighScore(String str) : Construit une nouvelle ligne de classement à partir d'une chaine de caractères en suivant un format spécifique.

Relations : La classe LigneHighScore interagit avec d'autres classes pour gérer le classement global, les noms des joueurs, les scores, les méthodes de gestion de données, etc.

Utilisation dans le projet : Cette classe est utilisée pour conserver les informations sur les joueurs, leurs noms et leurs scores dans le contexte d'un jeu ou d'un système de classement. Elle est indispensable pour garder trace des performances des joueurs, faciliter le tri des classements et les récapitulatifs des résultats.