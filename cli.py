import typer
import os
import subprocess


config = {"filepath": os.path.expanduser("~/Documents/dev/tools/notes")}

app = typer.Typer()
TEXT_DIR = os.path.join(f"{config['filepath']}", "txt")
MD_DIR = os.path.join(f"{config['filepath']}", "md")


def ensure_dirs():
    os.makedirs(TEXT_DIR, exist_ok=True)
    os.makedirs(MD_DIR, exist_ok=True)


@app.command()
def new(slug: str):
    """Create new note"""
    ensure_dirs()
    open(os.path.join(TEXT_DIR, f"{slug}.txt"), "a").close()
    open(os.path.join(MD_DIR, f"{slug}.md"), "a").close()
    typer.echo(f"Created note '{slug}'")


@app.command()
def open_note(slug: str):
    """Open note in VSCode"""
    subprocess.run(
        [
            "code",
            os.path.join(TEXT_DIR, f"{slug}.txt"),
            os.path.join(MD_DIR, f"{slug}.md"),
        ]
    )


@app.command()
def list():
    """List all note slugs"""
    slugs = [f[:-4] for f in os.listdir(TEXT_DIR) if f.endswith(".txt")]
    typer.echo("\n".join(slugs))


if __name__ == "__main__":
    app()
