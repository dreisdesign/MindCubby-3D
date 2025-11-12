# Git Hooks Setup

## Overview

This repository uses git hooks to automate G-code spec extraction. The pre-commit hook automatically generates `.txt` and `_printables.txt` files whenever `.gcode` files are modified.

## Initial Setup

After cloning the repository, enable the hooks with:

```bash
git config core.hooksPath .githooks
```

This tells git to use the hooks in the `.githooks/` directory instead of the default `.git/hooks/`.

## What the Hook Does

When you commit (after adding `.gcode` files):

1. **Detects** any `.gcode` files in your working directory
2. **Runs** `scripts/gcode_specs.py` on each file
3. **Generates** two output files:
   - `filename.txt` (raw specs)
   - `filename_printables.txt` (formatted for sharing)
4. **Auto-stages** the generated files for commit

## Example Workflow

```bash
# Export new G-code from Cura
cp ~/Downloads/model.gcode PRINTABLES/PROJECT/

# Stage and commit
git add .
git commit -m "add: new model"

# Output:
# 🔍 Generating specs for .gcode files...
#   → /path/to/model.gcode
# ✓ Generated and staged specs for 1 .gcode file(s)

# Commit includes:
# - model.gcode (ignored by git, not in repo)
# - model.txt (specs, tracked)
# - model_printables.txt (shareable description, tracked)
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
