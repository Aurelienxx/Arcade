# Bouton.java

 Description
Le rôle de la classe Bouton est de représenter et gérer un bouton dans un jeu vidéo. Elle permet d'associer diverses informations à ce bouton, tels que le texte, la texture, le chemin de son dossier, son nom, le numéro de jeu dans lequel il apparaît et d'autres propriétés.

Responsabilités
- Gérer et rendre le texte du bouton visible
- Gérer la texture du bouton
- Gérer les informations liées au bouton (chemin, nom, numéro de jeu)

Attributs
- texte : instance de Texte, permet de gérer l'affichage du texte du bouton
- chemin : chemin d'accès au dossier du bouton
- nom : nom du bouton
- texture : instance de Texture, permet de gérer l'affichage de la texture du bouton
- numeroDeJeu : numéro de jeu auquel le bouton appartient

Méthodes publiques
- setTexte(Texte) : définir le texte du bouton à l'aide d'une instance de Texte
- getChemin() : renvoyer le chemin d'accès au dossier du bouton
- setChemin(String) : définir le chemin d'accès au dossier du bouton
- getNom() : renvoyer le nom du bouton
- setNom(String) : définir le nom du bouton
- getTexte() : renvoyer l'instance de Texte utilisée pour afficher le texte du bouton
- setTexte(Texte) : définir l'instance de Texte utilisée pour afficher le texte du bouton
- getTexture() : renvoyer l'instance de Texture utilisée pour afficher la texture du bouton
- setTexture(Texture) : définir l'instance de Texture utilisée pour afficher la texture du bouton
- getNumeroDeJeu() : renvoyer le numéro de jeu associé au bouton
- setNumeroDeJeu(int) : définir le numéro de jeu associé au bouton

Relations
- Interagit avec les classes Texte et Texture pour gérer l'affichage du texte et de la texture du bouton
- Peut être utilisé dans le contexte d'une classe Graphique pour initialiser un tableau de boutons en fonction d'un dossier et d'un numéro de jeu

Utilisation dans le projet
La classe Bouton est utilisée dans le projet pour représenter et gérer les boutons dans les différents niveaux de jeu. Elle permet de gérer diverses informations pour chacun des boutons, ainsi que de les initialiser de manière homogène. Elle intègre également le dessin de textes et de textures dans la représentation des boutons.