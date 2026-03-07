# Main.java

 # Main Class

Main est une classe Java qui sert principalement à lancer l'application et exécuter des tâches liées à la génération de graphes. Cette classe est le point d'entrée de l'application, où le code principal s'exécute.

## Description générale

La classe Main est conçue pour gérer la partie graphique de l'application. Elle contient un seul fichier Java et gère l'exécution du code principal.

## Attributs principaux

Cette classe ne possède pas de variables (attributs) déclarées ou utilisées explicitement.

## Méthodes publiques

### main(String[])

C'est la méthode principale de cette classe. Elle est appelée lorsqu'un fichier Java est exécuté en tant que programme. Elle crée une instance de la classe Graphique et exécute une boucle infinie avec un bloc try-catch pour faire appel à la méthode selectionJeu() de la classe Graphique.

## Exemple d'utilisation (si applicable)

Pour exécuter le programme, il suffit de créer un fichier principal appelé Main.java et d'inclure le code suivant :

```java
public class Main {
    public static void main(String[] args) {
        Graphique g = new Graphique();
        while(true){
            try{
                // Thread.sleep(250);
            }catch(Exception e){};
            g.selectionJeu();
        }
    }
}
```

Enregistrez et exécutez le fichier en ligne de commande en utilisant la commande appropriée pour votre IDE (par exemple, `java Main` pour Java).

Remarquez que l'exemple de code inclut un thread.sleep() qui est commenté dans l'exemple présenté. Cette ligne peut être supprimée pour améliorer le fonctionnement de l'application.