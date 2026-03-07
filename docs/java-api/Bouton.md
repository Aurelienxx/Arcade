# Bouton.java

 Cette classe nommée `Bouton` est conçue pour représenter un bouton dans un jeu. Elle contient divers attributs et méthodes permettant de configurer et gérer le bouton. Le fichier Java ci-dessus permet d'initialiser des boutons à l'aide de divers éléments de la librairie MG2D, ainsi que de réplir et modifier leur position.

Voici une explication des éléments clés du code :

1. **Constructeur**: Il y a deux constructeurs : un par défaut et un permettant de spécifier les valeurs des attributs initialement.
   - `public Bouton()` : Constructeur sans paramètres qui initialise tous les attributs à null ou à leurs valeurs par défaut.
   - `public Bouton(Texte texte, Texture texture, String chemin, String nom)` : Constructeur avec paramètres permettant de spécifier les valeurs des attributs texte, texture, chemin et nom.

2. **Méthode statique 'remplirBouton()'**: Cette méthode permet de remplir tous les boutons du jeu en prenant en compte les textures et les textes situés dans le dossier projet.

3. **Accesseurs et mutateurs** : Cette classe fournit divers accesseurs et mutateurs pour les différents attributs, permettant de modifier les valeurs de ces derniers. Par exemple :
   - getChemin(), setChemin()
   - getNom(), setNom()
   - getTexte(), setTexte()
   - getTexture(), setTexture()
   - getNumeroDeJeu(), setNumeroDeJeu()

4. **Méthode 'RemplirBouton()'**: Cette méthode effectue une fonctionnalité essentielle dans le jeu. Elle charge chaque bouton avec un texte et une texture en fonction du fichier situé dans le dossier 'projet' de l'application.

Ainsi, en résumé, cette classe permet de gérer et de représenter des boutons dans un jeu, permettant de personnaliser leur texte, leur texture et leur position.