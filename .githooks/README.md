# Git Hooks

Shared git hooks for the MindCubby-3D project. These are automatically installed when you clone or set up the repo.

## Setup

To enable these hooks locally:

```bash
git config core.hooksPath .githooks
```

## Hooks

### `pre-commit`

Automatically generates `.txt` specs for any `.gcode` files in the working directory and stages them for commit.

**What it does:**
1. Detects any `.gcode` files (even ignored ones)
2. Runs `scripts/gcode_specs.py` on each file
3. Generates `.txt` and `_printables.txt` spec files
4. Auto-stages the generated specs for commit
5. Prevents commit if spec generation fails

**Example workflow:**
```bash
# Export new G-code from Cura
cp ~/Downloads/model.gcode PRINTABLES/PROJECT/

# Stage and commit
git add .
git commit -m "add: model.gcode"

# Hook automatically:
# → Detects model.gcode
# → Generates model.txt and model_printables.txt
# → Stages both files
# → Commits all three files
```

**Note:** `.gcode` files remain ignored in git (see `.gitignore`), but their corresponding `.txt` specs are always tracked and committed.

---

**Last Updated:** 2025-11-12
