# 📝 Notes CLI

A simple command-line tool for managing plain-text notes by name.  
Supports opening, listing, and organizing `.md` and `.txt` notes in a structured directory.

---

## ✨ Features

- `notes new <name>` — Create a new note (both `.txt` and `.md`)
- `notes open-note <name>` — Open a note (will create it if it doesn't exist)

- `notes list` — List all notes (both `.md` and `.txt`)
- Easy-to-extend CLI written in Python
- Minimal Bash wrapper for quick access

---

## 🛠 Usage

### 1. Add to your PATH

Make sure the `notes` script is executable and located in a directory that's part of your system's `PATH`.

You can create the script like this:

```bash
# ~/bin/notes
#!/bin/bash

# Replace /full/path/to/cli.py with the actual path to your script
exec python3 /full/path/to/cli.py "$@"
```

Make it executable:

`chmod +x ~/bin/notes`

Make sure ~/bin exists:

`mkdir -p ~/bin`

Add the script directory to your shell config (.zshrc, .bashrc, etc.):

`source ~/.bashrc  # or source ~/.zshrc`


