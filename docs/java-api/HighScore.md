# HighScore.java

 Description: La classe HighScore analyse et gère les données liées au classement des joueurs dans un jeu. Elle permet de charger et enregistrer un fichier de classements, déterminer la position d'un nouveau joueur dans le classement et afficher des informations à propos des différents noms de joueurs.

Responsabilités:
- Charger et enregistrer un fichier de classement
- Déterminer la position d'un nouveau joueur dans le classement
- Afficher différents attributs liés à des noms de joueurs

Attributs:
- nom: Nom du joueur
- score: Score du joueur

Méthodes publiques:
- lireFichier: Lire les données d'un fichier de classements
- enregistrerFichier: Enregistrer un fichier de classements
- déterminerPosition: Déterminer la position du nouveau joueur dans le classement
- afficherInformations: Afficher les différentes informations liées aux noms de joueurs

Relations: La classe HighScore interagit avec un fichier de classements (LigneHighScore) et les joueurs du jeu (leur nom et score).