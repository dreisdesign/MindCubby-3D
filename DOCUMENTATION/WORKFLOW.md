# MindCubby 3D Printing Workflow

Complete guide to the automated repository workflow, commands, and best practices.

## 📋 Overview

This repository combines 3D design files, Cura settings, G-code specs, and automated tooling to streamline the print-to-Printables workflow.

**Key Features:**
- ✅ Automated G-code spec generation (weight, time, temps)
- ✅ Smart file change detection (only regenerates changed files)
- ✅ Markdown tables formatted for easy Printables pasting
- ✅ Git pre-commit hooks for automatic spec generation
- ✅ Interactive CLI menu for common tasks
- ✅ Full version control of models, projects, and specs

---

## 🚀 Quick Commands

### View Interactive Menu
```bash
npm run menu
```
Beautiful terminal UI with 8 options:
1. **Quick Commit** - Stage, spec, commit, push in one command
2. **Generate Specs** - Create/update markdown descriptions
3. **Open PRINTABLES** - Jump to PRINTABLES folder
4. **Git Status** - Check uncommitted changes
5. **View Commits** - See last 10 commits
6. **Push** - Push to remote
7. **Setup Guide** - View initial setup
8. **Exit** - Close menu

### Generate Specs (Fast)
```bash
npm run p
```
Quickly regenerates specs for changed G-code files in PRINTABLES folder.

**Output Example:**
```
Processing 47 G-code file(s)...

→ PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone.gcode

=== G-Code Specs: mindcubby--melted-cone.gcode ===

Nozzle Temp:       195°C
Bed Temp:          65°C
Layer Height:      0.20 mm
Filament Weight:   3.9 g
Est. Print Time:   1h 33m 54s
Total G-Code Lines: 42093

✓ Successfully processed 1/47 files
```

### Generate Specs (Full)
```bash
npm run specs [directory]
```
Process specific directory or all gcode files.

### Quick Commit
```bash
gcode-commit "Your commit message"
```
One-line commit with automatic spec generation via pre-commit hook.

### Manual Commit
```bash
git add -A
git commit -m "Your message"
```
Pre-commit hook automatically runs and stages updated specs.

### Push Changes
```bash
git push
```

---

## 📁 Repository Structure

### `/PRINTABLES/`
Main folder for projects ready to upload to Printables.

**Each project contains:**
- `*.3mf` - Cura project file (settings, model, preview)
- `*.stl` - 3D model source (for remixing)
- `*_printables-description.md` - Ready-to-paste specs table

**NOT tracked:**
- `.gcode` - Regenerated on each Cura export
- Media files (images, videos, PDFs)

### `/CURA-SETTINGS/`
Start/end G-code templates and Cura profiles.

**Includes:**
- `archived/` - Previous G-code versions
- `variants/` - Alternative configurations
- `MindCubby PETG - Standard.curaprofile` - Recommended profile

### `/GCODE/`
Pre-made G-code snippets (deprecated, use CURA-SETTINGS instead).

### `/MODELS/`
General 3D print models and test files.

---

## 🔄 Typical Workflow

### Step 1: Design → Export from Cura
1. Open Cura with MindCubby profile
2. Design or import model
3. Slice settings as needed
4. **Export** → Save as `.3mf` + `.gcode`
5. Place files in appropriate `PRINTABLES/PRINTABLES_XX...` folder

### Step 2: Auto-Generate Specs
```bash
npm run p
```
Specs automatically generated based on G-code metadata:
- Parse `nozzle_temp`, `bed_temp`, `layer_height` from G-code comments
- Extract `filament_used` in meters
- Calculate weight: 1.25g per meter (standard 1.75mm filament)
- Extract print time from `;TIME:` comment (in seconds)

### Step 3: Copy Specs to Printables
1. Open the `_printables-description.md` file
2. Copy the markdown table
3. Paste into Printables description field
4. Add any custom notes or instructions

**Example Markdown Output:**
```markdown
## Print Specifications

| Specification | Value |
|---|---|
| Nozzle Temperature | 195°C |
| Bed Temperature | 65°C |
| Layer Height | 0.20 mm |
| Filament Weight | 3.9 g |
| Filament Length | 3.09 m |
| Estimated Print Time | 1h 33m 54s |

## Notes

- Optimized for **Ender-3 V2** with **BLTouch** bed leveling
- Uses off-print purge line to prevent nozzle blobs
- Exported from **Cura** with custom profile
- Recommended: Test on a small print first before large jobs
```

### Step 4: Commit & Push
```bash
gcode-commit "Add new Ice Cream print variant"
```

Or use menu:
```bash
npm run menu
→ Select "Quick Commit"
→ Type message
→ Done!
```

---

## 🧠 Smart File Detection

The system only regenerates specs for changed files:

```python
def needs_update(gcode_file):
    """Check if .gcode is newer than its _printables-description.md"""
    # Returns True if:
    # - No .md file exists (new file)
    # - .gcode modification time > .md modification time (file changed)
    # Returns False otherwise (skip processing)
```

**Benefits:**
- Fast processing (47 files in ~1 second if all unchanged)
- Only modified files get regenerated
- Reduces unnecessary file writes

**Example:**
```bash
$ touch PRINTABLES/PRINTABLES_02.*/mindcubby--melted-cone.gcode
$ npm run p

Processing 47 G-code file(s)...
→ PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone.gcode
[specs regenerated]
✓ Successfully processed 1/47 files
```

---

## 📊 What's Tracked in Git

### ✅ Tracked (218 files)
- **72 Markdown** - `*_printables-description.md` spec tables
- **91 3D Models** - `.stl` source files for remixing
- **21 Cura Projects** - `.3mf` files with all settings
- **8 G-Code** - Start/end code templates
- **3 Cura Profiles** - `.curaprofile` configuration

### ❌ Excluded
- **G-code exports** - Regenerated on each Cura export
- **Media files** - Images, videos, PDFs (store locally)
- **Cache files** - Python, Node, IDE files
- **OS files** - `.DS_Store`, Thumbs.db

---

## 🔧 Git Hooks

### Pre-Commit Hook
**Location:** `.githooks/pre-commit`

**Automatically runs on `git commit`:**
1. Detects `.gcode` files in commit
2. Runs spec generation for changed files
3. Stages updated `_printables-description.md` files
4. Shows summary of generated specs

**Example Output:**
```
🔍 Generating specs for .gcode files...
  → PRINTABLES/PRINTABLES_02.../mindcubby--melted-cone.gcode
  → PRINTABLES/PRINTABLES_13.../CE3E3V2_01-chip_clip--print_in_place.gcode
✓ Generated and staged specs for 2 .gcode file(s)
```

---

## 🛠️ Manual Spec Generation

### Generate All Specs
```bash
python3 scripts/gcode_specs.py PRINTABLES
```

### Generate Specific Directory
```bash
python3 scripts/gcode_specs.py PRINTABLES/PRINTABLES_02.\ Ice\ Cream\ Cone\ Melt/
```

### Generate Single File
```bash
python3 scripts/gcode_specs.py PRINTABLES/PRINTABLES_02.\ Ice Cream\ Cone\ Melt/mindcubby--melted-cone.gcode
```

### Force Regenerate All (ignore modification times)
```bash
# Remove all .md files first
find PRINTABLES -name "*_printables-description.md" -delete

# Then regenerate
npm run p
```

---

## 📝 Script Locations

- **`scripts/gcode_specs.py`** - Core spec extraction engine
  - Parses G-code metadata
  - Calculates weight from filament length
  - Generates markdown tables
  - Smart change detection

- **`scripts/menu.js`** - Interactive CLI menu
  - Arrow key navigation
  - Real-time git integration
  - One-command workflows

- **`scripts/gcode-commit.sh`** - Quick commit helper
  - Added as shell alias in `~/.zshrc`
  - Stages, commits, pushes in one line

- **`.githooks/pre-commit`** - Automatic spec generation
  - Triggers on every commit
  - Updates specs without user intervention

---

## 🔐 Security & Privacy

**NEVER commit:**
- ❌ Printer network credentials or IP addresses
- ❌ WiFi passwords
- ❌ GitHub tokens or personal access tokens
- ❌ Personal identifying information
- ❌ Financial or sensitive data

**Safe to track:**
- ✅ 3D model designs
- ✅ Print specifications and settings
- ✅ Cura project files (no credentials stored)
- ✅ Documentation and setup guides

---

## 💡 Tips & Tricks

### Speed Up Git Operations
```bash
# Check only current branch
git log --oneline -10

# See what changed
git diff HEAD~1
```

### Update Multiple Projects at Once
```bash
# Export multiple G-codes from Cura
# Place in PRINTABLES/ folders
npm run p  # All specs regenerated automatically
gcode-commit "Bulk update: 3 new prints"
```

### Verify Specs Before Commit
```bash
# View generated spec file
cat "PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone_printables-description.md"
```

### Track Custom Changes
```bash
# If you modify a spec manually
nano "PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone_printables-description.md"

# Re-export G-code from Cura to regenerate automatically
# Or use gcode-commit to manually track your edits
git add [file]
git commit -m "docs: update [project] specs"
```

---

## ⚡ Performance

| Operation | Time | Files |
|---|---|---|
| Generate all specs (first run) | ~5s | 47 files |
| Generate specs (no changes) | ~1s | 47 files |
| Generate specs (1 changed file) | ~1s | 1 file |
| Pre-commit hook | Auto | Staged changes only |
| Menu interaction | Instant | Real-time |

---

## 🐛 Troubleshooting

### "No such file or directory" error
```bash
# Make sure you're in the repo root
cd /Users/danielreis/Documents/3D_PRINTING/MINDCUBBY-3D
```

### Specs not generating
```bash
# Verify G-code file exists
ls PRINTABLES/PRINTABLES_02.*/mindcubby--melted-cone.gcode

# Check file permissions
file PRINTABLES/PRINTABLES_02.*/mindcubby--melted-cone.gcode

# Try manual generation
python3 scripts/gcode_specs.py PRINTABLES/PRINTABLES_02.*/*.gcode
```

### Menu not starting
```bash
# Verify Node.js is installed
node --version

# Reinstall dependencies
npm install

# Try menu again
npm run menu
```

### Changes not auto-committing
```bash
# Check hook permissions
ls -la .githooks/pre-commit

# Should show: -rwxr-xr-x (executable)
# If not, fix with:
chmod +x .githooks/pre-commit

# Verify hook is configured
git config core.hooksPath
# Should output: .githooks
```

---

## 📚 Related Documentation

- **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)** - Common tasks and checklists
- **[PRINTER_SPECS.md](./PRINTER_SPECS.md)** - Ender-3 V2 specifications
- **[CURA_PROFILE_MANAGEMENT.md](./CURA_PROFILE_MANAGEMENT.md)** - Profile setup and management
- **[MULTI_MATERIAL_SETUP.md](./MULTI_MATERIAL_SETUP.md)** - Material-specific settings

---

**Last Updated:** November 12, 2025  
**Status:** Complete - All automation implemented  
**Repo:** MindCubby-3D by dreisdesign
