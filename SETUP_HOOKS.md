# Git Hooks Setup

## Overview

This repository uses git hooks to automate G-code spec extraction. The pre-commit hook automatically generates `.txt` and `_printables.txt` files whenever `.gcode` files are modified.

## Quick Commit Command

For even faster workflow, use the **`gcode-commit`** command:

```bash
gcode-commit "your commit message"
```

This single command:
1. Stages all changes (`git add .`)
2. Generates specs for all `.gcode` files
3. Commits with your message
4. Pushes to remote

**Example:**
```bash
gcode-commit "add: new model"
# Output:
# 📦 Staging changes...
# 🔍 Running spec generation...
#   → model.gcode
# ✓ Generated and staged specs for 1 .gcode file(s)
# 💾 Committing: add: new model
# 🚀 Pushing to remote...
# ✅ Done!
```

## Manual Setup (if needed)

After cloning the repository, enable the hooks with:

```bash
git config core.hooksPath .githooks
```

The `gcode-commit` alias should be automatically added to your `~/.zshrc` during initial setup. If not, manually add:

```bash
alias gcode-commit="/path/to/repo/scripts/gcode-commit.sh"
```

Then reload your shell:
```bash
source ~/.zshrc
```

## What the Hook Does

When you commit (after adding `.gcode` files):

1. **Detects** any `.gcode` files in your working directory
2. **Runs** `scripts/gcode_specs.py` on each file
3. **Generates** two output files:
   - `filename.txt` (raw specs)
   - `filename_printables.txt` (formatted for sharing)
4. **Auto-stages** the generated files for commit

## Example Workflow

**Traditional git:**
```bash
cp ~/Downloads/model.gcode PRINTABLES/PROJECT/
git add .
git commit -m "add: model"
git push
```

**With gcode-commit (faster!):**
```bash
cp ~/Downloads/model.gcode PRINTABLES/PROJECT/
gcode-commit "add: model"
# → Stages, generates specs, commits, and pushes in one command
```

## Notes

- `.gcode` files are **ignored by git** (not committed)
- `.txt` spec files are **tracked** (committed)
- Hooks run automatically on every `git commit`
- Archive folders (`_ARCHIVE`, `_archive`) are skipped to avoid bloat
- To run manually without committing, use:
  ```bash
  python3 scripts/gcode_specs.py path/to/file.gcode
  python3 scripts/gcode_specs.py path/to/directory/
  ```

---

**Last Updated:** 2025-11-12
