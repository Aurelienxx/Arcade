# Changelog automatique

 Aucune modification au changelog technique n'est spécifiée dans le fichier fourni. Cependant, voici les changements apportés au fichier `.github/workflows/doc.yml` :

1. L'extrait de code a été modifié pour exclure les fichiers dans les répertoires `tests` et `javazoom` en plus des répertoires déjà listés `docs` et `javazoom` dans la recherche des fichiers `*.java`.

diff --git a/.github/workflows/doc.yml b/.github/workflows/doc.yml
index 6918f82..a54b4bd 100644
--- a/.github/workflows/doc.yml
+++ b/.github/workflows/doc.yml
@@ -30,9 +30,9 @@ jobs:
         run: |
           echo "=== Génération Javadoc ==="
           mkdir -p docs/javadoc
-          JAVA_FILES=$(find . -name "*.java" -not -path "./docs/*" -not -path "./javazoom/*" | wc -l)
+          JAVA_FILES=$(find . -name "*.java" -not -path "./docs/*" -not -path "./javazoom/*" -not -path "./tests/*" | wc -l)
           echo "Fichiers Java trouvés: $JAVA_FILES"
-          find . -name "*.java" -not -path "./docs/*" -not -path "./javazoom/*" -print0 | xargs -0 javadoc -Xdoclint:none -d docs/javadoc -sourcepath .:. 2>&1 || echo "Javadoc générée avec avertissements"
+          find . -name "*.java" -not -path "./docs/*" -not -path "./javazoom/*" -not -path "./tests/*" -print0 | xargs -0 javadoc -Xdoclint:none -d docs/javadoc 2>&1 || echo "Javadoc générée avec avertissements"
           echo "Javadoc complétée"
       - name: Setup Python
         uses: actions/setup-python@v4
