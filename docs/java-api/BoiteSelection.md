# BoiteSelection.java

 Description : La classe BoiteSelection représente une boîte dans un jeu, qui gère un pointeur et l'affichage de textes. Elle permet la sélection de différents éléments et gère leurs mouvements en fonction du pointeur.

Responsabilités :
- Gérer le pointeur
- Gérer la sélection d'éléments en utilisant le pointeur
- Gérer la position des textes à afficher

Attributs :
- pointeur

Méthodes publiques :
- selection(ClavierBorneArcade clavier) : Permet de gérer la sélection en fonction des déplacements du pointeur et de l'utilisation du joystick.
- getPointeur() : Retourne la référence du pointeur.
- setPointeur(Pointeur pointeur) : Définit le pointeur à modifier.

Relations : La classe BoiteSelection interagit avec d'autres classes pour gérer la navigation et l'affichage d'éléments dans un menu. Elle utilise des classes telles que ClavierBorneArcade, Rectangle, Pointeur, Texte et Bruitage.