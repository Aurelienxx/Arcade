import subprocess
import os
from ollama_wrapper import OllamaWrapper


def get_last_diff():
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        diff = result.stdout
        
        # Affiche le résumé des fichiers modifiés
        print("\n📝 Fichiers modifiés:")
        file_changes = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True
        )
        if file_changes.stdout.strip():
            for file in file_changes.stdout.strip().split('\n'):
                print(f"  • {file}")
        
        return diff
    except subprocess.CalledProcessError:
        print("⚠️  Impossible de récupérer le diff git")
        return ""


def generate_summary(diff_text):
    client = OllamaWrapper(base_url="http://localhost:11434")

    if not client.is_server_running():
        print("❌ Ollama non accessible - changelog IA non généré")
        return None

    try:
        prompt = f"""
Résume clairement et professionnellement les modifications suivantes
pour un changelog technique structuré :

{diff_text}
"""
        response = client.generate_text(
            model="phi3",
            prompt=prompt
        )
        return response.response
    except Exception as e:
        print(f"❌ Erreur lors de la génération avec Ollama: {e}")
        return None


def write_changelog(summary):
    os.makedirs("docs", exist_ok=True)

    with open("docs/changelog_auto.md", "w", encoding="utf-8") as f:
        f.write("# 📜 Changelog automatique\n\n")
        f.write(summary)
        f.write("\n")
    print("✅ Changelog généré avec succès")


def main():
    print("=== Analyse des modifications ===\n")
    diff = get_last_diff()

    if not diff.strip():
        print("\n⚠️  Aucun changement détecté.")
        return

    print("\n🤖 Génération du résumé IA...")
    summary = generate_summary(diff)

    if summary is None:
        print("❌ Erreur lors de la génération du résumé")
        return

    write_changelog(summary)
    print("\n✨ Documentation mise à jour avec succès!")


if __name__ == "__main__":
    main()