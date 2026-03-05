# Changelog automatique

 Résumé des changements suivants pour un changelog technique structuré :

1. Modification de la commande `find` pour générer le changelog de Java, en ajoutant `-path "./docs/*"` pour ne pas inclure les dossiers de documentation dans le nombre de fichiers Java.
2. Modification du script `pip` pour installer le package `pdoc` en utilisant `pip install -q pdoc 2>/dev/null || true`, ce qui permet de continuer le script même si l'installation échoue.
3. Mise à jour de la documentation Python avec le script `pdoc`, en changeant la commande pour utiliser `2>/dev/null` pour rediriger les erreurs vers le bitbucket et `|| true` pour continuer le script même si la génération échoue.
4. Ajout d'un nouveau message d'échec dans le cas où aucun fichier Python n'est trouvé.
