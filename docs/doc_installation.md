IUT du Littoral Côte d'Opale (IUT)
====================================
Documentation d'installation de la borne d'arcade
----------------------------------

- Dusannier Léothen
- Fontaine Aurélien

## Installation du système d'exploitation

Installez la dernière version de **Raspberry Pi OS** sur votre Raspberry Pi: https://www.raspberrypi.com/software/operating-systems/.

Une fois le système d'exploitation prêt, installez git. Dans le terminal :
> sudo apt-get install git

Créez un répertoire git :
> cd ~

> mkdir git

> cd git

## Installation de MG2D

On va ensuite télécharger la bibliothèque MG2D et la partie logicielle ici présente. Si vous l'avez déjà téléchargée, vous déplacerez le répertoire dans le répertoire git précédemment créé. Le répertoire doit s'appeler ***borne_arcade***

> git clone http://iut.univ-littoral.fr/gitlab/synave/MG2D.git

> git clone https://github.com/Aurelienxx/Arcade

Suite à ces téléchargements, vous devez avoir l'arborescence suivante :
- répertoire personnel
- &nbsp; &nbsp; |
- &nbsp; &nbsp; |-> git
- &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
- &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |-> MG2D
- &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |-> borne_arcade

Le téléchargement et mise à jour de java, python et des bibliothéques sont effectuer automatiquement au lancement de la borne dans **installe.sh**
## Configuration de la borne

Placez MG2D en variable d'environnement.

> nano ~/.bashrc

> export export CLASSPATH=$CLASSPATH:.:/home/pi/git/MG2D

Lancez le logiciel au démarrage de la borne
> mv borne.desktop ~/.config/autostart/

Redémarrez et normalement, lors du démarrage, un terminal va s'ouvrir et quelques secondes après (10-15 secondes), l'interface de la borne va se lancer. Des informations concernant les opérations en cours sont affichées dans le terminal. Soyez patient.

Sélectionnez le jeu avec haut/bas du joystick du joueur 1 et lancez le jeu avec le bouton A du joueur 1. Quittez le logiciel avec le bouton Z du joueur 1. Une demande de confirmation s'affichera. Validez oui ou non avec le bouton A du joueur 1.

Si vous quittez le menu, vous reviendrez sur le terminal. Attendez 30 secondes pour une extinction totale de la machine.
