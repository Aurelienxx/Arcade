import subprocess
import os
import re
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


def generate_simple_summary(diff_text):
    """Génère un changelog simple sans IA en parsant le diff"""
    print("📄 Génération du changelog simple (sans IA)...")
    
    lines = diff_text.split('\n')
    files = {}
    current_file = None
    
    for line in lines:
        if line.startswith('diff --git'):
            current_file = re.search(r'b/(.*?)$', line)
            if current_file:
                current_file = current_file.group(1)
                files[current_file] = {'added': 0, 'removed': 0, 'modified': True}
        elif current_file and line.startswith('+') and not line.startswith('+++'):
            files[current_file]['added'] += 1
        elif current_file and line.startswith('-') and not line.startswith('---'):
            files[current_file]['removed'] += 1
    
    summary = "## 📋 Résumé des modifications\n\n"
    
    if not files:
        summary += "Aucune modification détectée.\n"
        return summary
    
    summary += f"**{len(files)} fichier(s) modifié(s)**\n\n"
    
    for file, stats in files.items():
        summary += f"- **{file}**"
        if stats['added'] > 0 or stats['removed'] > 0:
            summary += f" (+{stats['added']}/-{stats['removed']})"
        summary += "\n"
    
    return summary


def generate_summary(diff_text):
    client = OllamaWrapper(base_url="http://localhost:11434")

    if not client.is_server_running():
        print("⚠️  Ollama non accessible")
        return generate_simple_summary(diff_text)

    try:
        prompt = f"""
Résume clairement et professionnellement les modifications suivantes
pour un changelog technique structuré :

{diff_text}
"""
        response = client.generate_text(
            model="neural-chat",
            prompt=prompt,
            stream=False
        )
        print("✅ Résumé généré avec IA")
        return response.response
    except Exception as e:
        print(f"⚠️  Ollama indisponible ({type(e).__name__})")
        return generate_simple_summary(diff_text)


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

    print("\n🤖 Génération du résumé...")
    summary = generate_summary(diff)

    if summary is None:
        print("❌ Erreur lors de la génération du résumé")
        return

    write_changelog(summary)
    print("\n✨ Documentation mise à jour avec succès!")


if __name__ == "__main__":
    main()