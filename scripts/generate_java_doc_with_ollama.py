#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
from ollama_wrapper import OllamaWrapper
import json


def find_java_files():
    """Trouve uniquement les fichiers .java à la racine du projet"""
    java_files = []

    for file in os.listdir("."):
        if file.endswith(".java") and os.path.isfile(file):
            java_files.append(file)

    return sorted(java_files)


def read_java_file(filepath):
    """Lit un fichier Java"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"⚠️  Impossible de lire {filepath}: {e}")
        return None


def generate_class_doc(client, java_content, filename):
    """Génère la documentation pour une classe Java avec Ollama"""
    prompt = f"""Tu es un expert en documentation Java. 
Analyse le fichier Java suivant et génère une documentation claire et professionnelle.

Inclus:
- Une description générale de la classe
- Les attributs principaux
- Les méthodes publiques avec leurs descriptions
- Exemple d'utilisation si applicable

Fichier: {filename}

```java
{java_content}
```

Génère la documentation en Markdown, sans blocs de code."""

    try:
        response = client.generate_text(
            model="neural-chat",
            prompt=prompt
        )
        return response.response
    except Exception as e:
        print(f"⚠️  Erreur Ollama pour {filename}: {e}")
        return None


def main():
    print("🚀 Génération documentation Java avec Ollama...\n")
    
    # Vérifier qu'Ollama est disponible
    client = OllamaWrapper(base_url="http://localhost:11434", timeout_s=300.0)
    
    if not client.is_server_running():
        print("❌ Ollama n'est pas accessible!")
        return False
    
    # Trouver tous les fichiers Java
    java_files = find_java_files()
    print(f"📄 {len(java_files)} fichier(s) Java trouvé(s)\n")
    
    if not java_files:
        print("⚠️  Aucun fichier Java trouvé")
        return False
    
    # Créer le dossier de sortie
    os.makedirs("docs/java-api", exist_ok=True)
    
    # Générer la documentation pour chaque fichier
    docs_generated = 0
    for java_file in java_files:
        print(f"📝 Traitement: {java_file}")
        
        content = read_java_file(java_file)
        if not content:
            continue
        
        doc = generate_class_doc(client, content, java_file)
        if not doc:
            continue
        
        # Sauvegarder la documentation
        output_file = java_file.replace(".java", ".md").replace("\\", "/")
        output_path = os.path.join("docs/java-api", os.path.basename(output_file))
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {os.path.basename(java_file)}\n\n")
                f.write(doc)
            docs_generated += 1
            print(f"  ✅ Sauvegardé: {output_path}")
        except Exception as e:
            print(f"  ❌ Erreur sauvegarde: {e}")
    
    print(f"\n✨ {docs_generated}/{len(java_files)} documentation(s) générée(s)")
    return docs_generated > 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
