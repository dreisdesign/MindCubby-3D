# Quick Reference Guide

Fast lookup for commands, workflows, troubleshooting, and common tasks.

---

## 🚀 Quick Commands

### Interactive Menu
```bash
npm run menu
```
Beautiful CLI with 8 options:
1. Quick Commit - Stage, spec, commit, push
2. Generate Specs - Create/update descriptions
3. Open PRINTABLES - Jump to folder
4. Git Status - Check changes
5. View Commits - See last 10
6. Push - Push to remote
7. Setup Guide - View guide
8. Exit - Close menu

### Generate Specs (Quick)
```bash
npm run p
```
Regenerates specs for changed G-code files only (smart detection).

**Output:**
```
Processing 47 G-code file(s)...
→ PRINTABLES/PRINTABLES_02.../mindcubby--melted-cone.gcode
Nozzle Temp: 195°C, Bed Temp: 65°C, Weight: 3.9g, Time: 1h 33m

✓ Successfully processed 1/47 files
```

### One-Line Commit
```bash
gcode-commit "Your commit message"
```
Stages changes, auto-generates specs, commits, pushes.

### Manual Commands
```bash
# Generate all specs
python3 scripts/gcode_specs.py PRINTABLES

# Git add and commit
git add -A
git commit -m "Your message"

# Push to remote
git push
```

---

## 📋 Typical Workflow

### Step 1: Design & Export
1. Open Cura with MindCubby profile
2. Design or import model
3. Slice with appropriate settings (see SETUP.md)
4. Export → Save `.3mf` + `.gcode`
5. Place in appropriate `PRINTABLES/PRINTABLES_XX...` folder

### Step 2: Auto-Generate Specs
```bash
npm run p
```
Specs automatically generated from G-code:
- Nozzle/bed temps from comments
- Filament length from `;Filament used:`
- **Weight calculated** (1.25g per meter)
- **Time extracted** from `;TIME:` (in seconds)

### Step 3: Copy to Printables
1. Open `*_printables-description.md`
2. Copy the markdown table
3. Paste into Printables description
4. Add custom notes if needed

**Example Output:**
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
- Optimized for Ender-3 V2 with BLTouch
- Uses off-print purge line
- Exported from Cura with custom profile
```

### Step 4: Commit & Push
```bash
gcode-commit "Add Ice Cream Cone variant"
```

---

## 📁 Repository Organization

### `/PRINTABLES/` - Ready for Printables
Each project folder contains:
- `*.3mf` - Cura project (settings + model preview)
- `*.stl` - 3D model source file (for remixing)
- `*_printables-description.md` - Ready-to-paste specs

**Example:**
```
PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/
├── mindcubby--melted-cone.3mf              ✅ Tracked
├── mindcubby--melted-cone.stl              ✅ Tracked
├── mindcubby--melted-cone_printables-description.md  ✅ Tracked
└── mindcubby--melted-cone.gcode            ❌ Local only (regenerated)
```

### `/CURA-SETTINGS/` - G-code & Profiles
- `active/` - Currently recommended settings
- `variants/` - Alternative configurations
- `archived/` - Previous versions with specs
- `.curaprofile` - Recommended Cura profile

### `/DOCUMENTATION/` - This folder
- `SETUP.md` - Printer config, materials, profiles
- `REFERENCE.md` - This file! Commands & workflows
- `README.md` (root) - Project overview

---

## 🔄 Smart Change Detection

System only regenerates specs for files that changed:

```python
if .gcode modification time > .md modification time:
    regenerate specs
else:
    skip (save time)
```

**Benefits:**
- 47 files processed in ~1 second if unchanged
- Only modified files regenerated
- Huge speed improvement for bulk operations

**Example:**
```bash
$ touch PRINTABLES/PRINTABLES_02.*/mindcubby--melted-cone.gcode
$ npm run p

Processing 47 G-code file(s)...
→ Only changed file regenerated
✓ Successfully processed 1/47 files
```

---

## 📊 What's Tracked in Git

### ✅ Always Tracked (218 files)
- **72 Markdown** - `*_printables-description.md` specs
- **91 3D Models** - `.stl` source files
- **21 Cura Projects** - `.3mf` files with settings
- **8 G-Code** - Start/end code templates
- **3 Cura Profiles** - `.curaprofile` configurations

### ❌ Always Excluded
- **G-code exports** - Regenerated on each Cura export
- **Media files** - Images, videos, PDFs (store locally)
- **Cache files** - Python, Node, IDE files
- **OS files** - `.DS_Store`, `Thumbs.db`

---

## 🔧 Git Hooks & Automation

### Pre-Commit Hook (`.githooks/pre-commit`)
Automatically runs on `git commit`:
1. Detects `.gcode` files in commit
2. Runs spec generation for changed files
3. Stages updated `_printables-description.md`
4. Shows summary

**Output:**
```
🔍 Generating specs for .gcode files...
  → PRINTABLES/PRINTABLES_02.../mindcubby--melted-cone.gcode
  → PRINTABLES/PRINTABLES_13.../CE3E3V2_01-chip_clip--print_in_place.gcode
✓ Generated and staged specs for 2 .gcode file(s)
```

---

## 💡 Tips & Tricks

### Speed Up Operations
```bash
# View last 10 commits quickly
git log --oneline -10

# See what changed
git diff HEAD~1

# Check status without pager
git status
```

### Update Multiple Projects
```bash
# Export multiple G-codes from Cura
# Place all in PRINTABLES/ folders
npm run p  # All specs auto-updated!
gcode-commit "Bulk update: 3 new prints"
```

### Verify Specs Before Commit
```bash
# View generated spec table
cat "PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone_printables-description.md"
```

### Manual Spec Update
```bash
# If you modify a spec manually
nano "PRINTABLES/PRINTABLES_02.../mindcubby--melted-cone_printables-description.md"

# Re-export G-code from Cura to auto-regenerate
# Or commit manually:
git add [file]
git commit -m "docs: update specs for [project]"
```

---

## 🐛 Troubleshooting

### "Command not found: gcode-commit"
```bash
# Make sure alias is in ~/.zshrc
grep "gcode-commit" ~/.zshrc

# If missing, add it manually:
echo 'alias gcode-commit="bash ~/path/to/gcode-commit.sh"' >> ~/.zshrc
source ~/.zshrc
```

### Specs Not Generating
```bash
# Verify Python is available
python3 --version

# Test manual generation
python3 scripts/gcode_specs.py PRINTABLES/PRINTABLES_02.*/*.gcode

# Check for errors
python3 scripts/gcode_specs.py PRINTABLES 2>&1 | head -20
```

### Menu Not Starting
```bash
# Verify Node.js is installed
node --version
npm --version

# Reinstall dependencies
npm install

# Try menu again
npm run menu
```

### Changes Not Auto-Committing
```bash
# Check hook is executable
ls -la .githooks/pre-commit
# Should show: -rwxr-xr-x

# Fix if needed:
chmod +x .githooks/pre-commit

# Verify git knows about hooks
git config core.hooksPath
# Should output: .githooks
```

### Git Status Shows Wrong Files
```bash
# Clear git cache and rebuild
git rm --cached -r .
git add -A
git status

# This will show what actually should be tracked
```

---

## 📈 Performance Benchmarks

| Operation | Time | Notes |
|-----------|------|-------|
| Generate all specs (first run) | ~5s | 47 files |
| Generate specs (no changes) | ~1s | Smart detection |
| Generate specs (1 changed) | ~1s | Only 1 file |
| Pre-commit hook | Auto | Transparent |
| Menu startup | <1s | Real-time |
| Git push | 2-5s | Network dependent |

---

## 📚 Full Documentation

- **SETUP.md** - Printer setup, materials, profiles, troubleshooting
- **README.md** (root) - Project overview and features
- **WORKFLOW.md** - Complete automation guide (detailed reference)

---

## 🔐 Security Reminders

**NEVER commit:**
- ❌ Printer IP addresses or network credentials
- ❌ WiFi passwords
- ❌ GitHub tokens or personal access tokens
- ❌ Personal identifying information
- ❌ Financial or sensitive data

**Safe to track:**
- ✅ 3D designs and models
- ✅ Print specifications and settings
- ✅ Cura project files (no secrets stored)
- ✅ Documentation and guides

---

## Common Tasks Checklist

### Adding a New Print
- [ ] Export `.3mf` + `.gcode` from Cura
- [ ] Place in appropriate `PRINTABLES/PRINTABLES_XX` folder
- [ ] Run `npm run p` to generate specs
- [ ] Review `*_printables-description.md`
- [ ] Run `gcode-commit "Add [project name]"`
- [ ] Copy specs to Printables.com

### Before Printing
- [ ] Clean bed with IPA
- [ ] Check nozzle for debris
- [ ] Run auto-level (`G29`)
- [ ] Test first layer height
- [ ] Verify filament path is clear

### Weekly Maintenance
- [ ] Check belt tension
- [ ] Verify all bolts are tight
- [ ] Clean build plate

---

**Last Updated**: November 12, 2025  
**Status**: Complete - Consolidated Documentation
