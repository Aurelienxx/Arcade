# Boite.java

 ## Description
La classe Boite représente un conteneur abstrait qui hérite d'une géométrie en 2D (Rectangle) et définit une boîte. Son objectif principal est de représenter facilement un objet contenant un Rectangle, ce qui peut être utile dans différents contextes de développement en utilisant une structure de données cohérente et claire.

## Responsabilités
- Gérer les caractéristiques de la boîte (Rectangle)
- Représenter l'espace physique et virtuel que la boîte occupe

## Attributs
- rectangle (Rectangle) : Représente l'espace géométrique de la boîte en 2D

## Méthodes publiques
- Boite(Rectangle rectangle) : Crée une nouvelle instance de Boite à partir d'un Rectangle
- getRectangle() : Renvoie le Rectangle représentant l'espace géométrique de la boîte
- setRectangle(Rectangle rectangle) : Définit le nouveau Rectangle représentant l'espace géométrique de la boîte

## Relations
- La classe Boite peut interagir avec d'autres classes comme les geometries en 2D ou des classes spécifiques à un projet particulier.

## Utilisation dans le projet
La classe Boite peut être utilisée dans un contexte de développement impliquant des geometries en 2D et des objets contenant de tels espaces, tels que des applications de dessins, de jeux ou de simulations. Elle permet de structurer de manière cohérente et évolutive les objets contenant un Rectangle, facilitant l'interaction avec d'autres classes et le processus de développement.