# Main.java

 Description : La classe Main joue un rôle important dans le contexte du projet en étant le point d'entrée pour les programmes en cours d'exécution. Son objectif principal est de définir et gérer la boucle principale de l'application, en coordonnant différentes tâches.

Responsabilités :
1. Gérer le cycle de vie des programmes en cours d'exécution.
2. Assurer le bon fonctionnement des tâches et des processus en interaction avec d'autres classes du projet.

Attributs :
- Main main : Identifie le thread principal de l'application.

Méthodes publiques :
- public static void main(String[] args) : Point d'entrée pour lancer l'application et gérer l'interaction avec les autres programmes en cours d'exécution.

Relations :
- Main est reliée à la classe Graphique, étant donné qu'elle appelle la méthode selectionJeu() de Graphique au sein de la boucle principale.

Utilisation dans le projet : La classe Main est utilisée comme point d'entrée pour l'application, gérant la boucle principale et les interactions avec d'autres classes du projet, permettant ainsi le bon fonctionnement de l'application.