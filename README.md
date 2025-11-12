````markdown
# MINDCUBBY 3D Printing Repository

Complete 3D printing workflow with automated specifications, Cura settings, and Printables integration.

**Printer**: Creality Ender-3 V2 + BLTouch | **Nozzle**: 0.4mm | **Bed**: 220x220mm

## 🚀 Quick Start

### View the Interactive Menu
```bash
npm run menu
```
Beautiful CLI menu with 8 options for common tasks.

### Generate Print Specs Quickly
```bash
npm run p
```
Automatically creates markdown tables ready for Printables with:
- Nozzle & bed temperature
- Layer height & filament info
- **Weight (calculated)** & **print time (extracted)**

### Quick Commit
```bash
gcode-commit "Your commit message"
```
Stages changes, auto-generates specs, commits, and pushes—all in one command!

## Quick Links

| Need | File |
|------|------|
| **Automated Workflow** | [DOCUMENTATION/WORKFLOW.md](DOCUMENTATION/WORKFLOW.md) |
| Common tasks & fixes | [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) |
| Printer specs & materials | [DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md) |
| Changes & history | [CHANGELOG.md](CHANGELOG.md) |

## 📊 Repository Contents

**218 tracked files:**
- **72 Markdown** - Printables specs (ready-to-copy tables)
- **91 3D Models** - STL source files
- **21 Cura Projects** - 3MF files with all settings
- **8 G-Code** - Start/end code templates
- **3 Cura Profiles** - Recommended configurations

### Directory Structure

```
DOCUMENTATION/
├── WORKFLOW.md                 # ⭐ Complete automation guide
├── QUICK_REFERENCE.md          # Tasks, troubleshooting, commands
├── PRINTER_SPECS.md            # Hardware & material profiles
└── CURA_PROFILE_MANAGEMENT.md  # Profile setup

PRINTABLES/                      # Projects ready for Printables
├── PRINTABLES_01. Ghost/
│   ├── *.3mf                   # Cura project (settings + model)
│   ├── *.stl                   # 3D model source
│   └── *_printables-description.md  # ⭐ Ready-to-paste specs
├── PRINTABLES_02. Ice Cream Cone Melt/
└── [13 more print projects...]

CURA-SETTINGS/                   # G-code & Cura profiles
├── archived/                    # Previous versions
│   ├── Ender3V2_Baseline_StartGCode.gcode
│   ├── Optimized_StartGCode_v1.gcode
│   └── *.md                    # Specs for each version
├── variants/                    # Experimental configs
│   └── Optimized_StartGCode_v6.gcode
└── MindCubby PETG - Standard.curaprofile

MODELS/                          # General print models
└── *.3mf, *.gcode             # Test files and samples
```

## ⚡ Key Features

### 1. Automated Spec Generation
- Extracts nozzle temp, bed temp, layer height from G-code
- **Calculates filament weight** (1.25g per meter standard)
- **Extracts print time** from `;TIME:` metadata
- Generates **markdown tables** ready for Printables

### 2. Smart Change Detection
- Only regenerates specs for modified G-code files
- 47 files processed in ~1 second if unchanged
- Eliminates redundant file writes

### 3. Git Integration
- **Pre-commit hooks** auto-generate specs on commit
- Full version control of designs, projects, and specs
- `.gcode` files excluded (regenerated each export)
- Media files excluded (store locally)

### 4. Interactive CLI Menu
```bash
npm run menu

# Options:
# 1. Quick Commit
# 2. Generate Specs
# 3. Open PRINTABLES
# 4. Git Status
# 5. View Commits
# 6. Push
# 7. Setup Guide
# 8. Exit
```

## 📋 Typical Workflow

1. **Design in Cura** → Export `.3mf` + `.gcode` to PRINTABLES folder
2. **Auto-Generate Specs** → `npm run p` extracts all print info
3. **Copy to Printables** → Open `_printables-description.md`, copy table
4. **Commit & Push** → `gcode-commit "Add new print"`

That's it! Specs auto-generated, committed, and ready to use.

## 📊 Example Output

### G-Code Metadata Extraction
```
Processing 47 G-code file(s)...

→ PRINTABLES/PRINTABLES_02. Ice Cream Cone Melt/mindcubby--melted-cone.gcode

=== G-Code Specs: mindcubby--melted-cone.gcode ===

Nozzle Temp:       195°C
Bed Temp:          65°C
Layer Height:      0.20 mm
Filament Weight:   3.9 g          ← Calculated
Est. Print Time:   1h 33m 54s     ← Extracted
Total G-Code Lines: 42093

✓ Successfully processed 1/47 files
```

### Generated Markdown (Ready for Printables)
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

## 🔧 Commands Reference

| Command | Purpose |
|---------|---------|
| `npm run menu` | Interactive CLI menu |
| `npm run p` | Quick spec generation (PRINTABLES folder) |
| `npm run specs [dir]` | Generate specs for directory |
| `gcode-commit "msg"` | One-line commit with auto specs |
| `npm run commit` | Alternative commit method |
| `git push` | Push commits to remote |

## 📚 Documentation

- **[WORKFLOW.md](DOCUMENTATION/WORKFLOW.md)** - Complete automation guide with examples
- **[QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md)** - Quick lookup for common tasks
- **[PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md)** - Hardware specifications and materials
- **[CURA_PROFILE_MANAGEMENT.md](DOCUMENTATION/CURA_PROFILE_MANAGEMENT.md)** - Profile setup

## 🔐 What's Tracked in Git

### ✅ Tracked (for version control)
- 3D model files (`.stl`)
- Cura projects (`.3mf`)
- Print specifications (`.md`)
- G-code templates (`.gcode`)
- Cura profiles (`.curaprofile`)

### ❌ Excluded (regenerated/local only)
- Exported G-codes (regenerated from Cura each time)
- Media files (images, videos, PDFs)
- Cache and IDE files

## 🚦 Latest Updates

**November 12, 2025** - Automation Complete
- ✅ Markdown table format for Printables
- ✅ Weight calculation from filament length
- ✅ Print time extraction from G-code
- ✅ Smart change detection (skip unchanged files)
- ✅ Git pre-commit auto-generation
- ✅ Full documentation and workflow guide

See [CHANGELOG.md](CHANGELOG.md) for complete history.

---

**Repository**: MindCubby-3D  
**Owner**: dreisdesign  
**Status**: ⚡ Production Ready  
**Last Updated**: November 12, 2025
````
