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
        return result.stdout
    except subprocess.CalledProcessError:
        return ""


def generate_summary(diff_text):
    client = OllamaWrapper(base_url="http://localhost:11434")

    if not client.is_server_running():
        print("Ollama non accessible")
        return None

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


def write_changelog(summary):
    os.makedirs("docs", exist_ok=True)

    with open("docs/changelog_auto.md", "w", encoding="utf-8") as f:
        f.write("# 📜 Changelog automatique\n\n")
        f.write(summary)
        f.write("\n")


def main():
    diff = get_last_diff()

    if not diff.strip():
        print("Aucun changement.")
        return

    summary = generate_summary(diff)

    if summary is None:
        return

    write_changelog(summary)
    print("Changelog généré.")


if __name__ == "__main__":
    main()