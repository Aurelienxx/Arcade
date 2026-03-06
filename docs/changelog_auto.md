# Changelog automatique

 Différences dans le fichier .github/workflows/doc.yml :
- La ligne 30 a été ajoutée pour exclure un répertoire supplémentaire lors de la recherche des fichiers .java.
- La ligne 37 a été modifiée pour supprimer les contrôles de conformance du fichier JavaDoc (options `-Xdoclint:none` et `-sourcepath .:.` ajoutées).
- La dernière ligne du bloc Javadoc a été ajoutée pour ajouter un message d'erreur en cas d'échec du processus de génération du Javadoc.
