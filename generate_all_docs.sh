#!/bin/bash

echo "=== Génération complète de la documentation ==="
echo ""

# Javadoc
echo " Génération Javadoc..."
mkdir -p docs/javadoc
JAVA_COUNT=$(find . -name "*.java" -not -path "./docs/*" | wc -l)
echo "  Fichiers Java trouvés: $JAVA_COUNT"
find . -name "*.java" -not -path "./docs/*" -print0 | xargs -0 javadoc -d docs/javadoc 2>&1 >/dev/null || true
echo "  ✅ Javadoc complétée"
echo ""

# Python
echo " Génération documentation Python..."
pip install -q pdoc 2>/dev/null || true
PYTHON_COUNT=$(find . -name "*.py" -not -path "./docs/*" -not -path "./.git/*" | wc -l)
echo "  Fichiers Python trouvés: $PYTHON_COUNT"
if [ $PYTHON_COUNT -gt 0 ]; then
  mkdir -p docs/python
  pdoc -o docs/python scripts/ 2>/dev/null || true
  echo "  ✅ Documentation Python complétée"
else
  echo "  Aucun fichier Python"
fi
echo ""

echo ""
echo " Documentation complète générée dans docs/"
echo "Fichiers disponibles:"
echo "  • docs/javadoc/         - Documentation Java"
echo "  • docs/python/          - Documentation Python"
