# MINDCUBBY 3D Printing Repository

Repository for 3D printing projects, G-code files, and printer configurations.

## 📚 Quick Start

**New to the repo?** Start here:
1. **[DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md)** - Fast lookup for common tasks
2. **[DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md)** - Printer specs and materials
3. **[GCODE/README.md](GCODE/README.md)** - G-code optimizations

## 📋 Key Resources

| Need | Go To |
|------|-------|
| Quick tasks & checklists | [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) |
| Hardware & materials | [DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md) |
| Using Copilot AI | [DOCUMENTATION/COPILOT_GUIDE.md](DOCUMENTATION/COPILOT_GUIDE.md) |
| Version history | [CHANGELOG.md](CHANGELOG.md) |
| G-code optimizations | [GCODE/README.md](GCODE/README.md) & [GCODE/CHANGELOG.md](GCODE/CHANGELOG.md) |
| Cura profiles | [PROFILES/README.md](PROFILES/README.md) |

## Printer Setup
- **Printer**: Creality Ender-3 V2
- **Nozzle**: 0.4mm
- **Bed**: 220x220mm
- **Features**: BLTouch auto-leveling

## Repository Structure

```
MINDCUBBY-3D/
├── README.md                       # This file
├── CHANGELOG.md                    # Main version history
│
├── DOCUMENTATION/                  # 📚 Guides & references
│   ├── README.md                  # Doc index
│   ├── QUICK_REFERENCE.md         # Fast lookup (START HERE!)
│   ├── PRINTER_SPECS.md           # Hardware & materials
│   ├── COPILOT_GUIDE.md           # AI documentation helper
│   ├── REPOSITORY_REVIEW.md       # Structure analysis (reference)
│   └── MARKDOWN_CONSOLIDATION.md  # Consolidation notes (reference)
│
├── PROFILES/                       # Cura G-code profiles
│   ├── README.md
│   ├── Ender3V2_Baseline_StartGCode.gcode
│   └── Ender3V2_BLTouch_Optimized.txt
│
├── GCODE/                          # G-code optimization experiments
│   ├── README.md
│   ├── CHANGELOG.md               # Optimization history
│   ├── Original_StartGCode_Archive.gcode
│   └── Optimized_StartGCode_v1.gcode
│
├── MODELS/                         # 3D model files (STL/OBJ)
└── .github/
    └── chatmodes/
        └── Ender-3 V2.chatmode.md
```

## Quick Start

1. **Load Cura Profile**: Import from `PROFILES/` directory
2. **Slice Model**: Use optimized start/end G-code
3. **Export G-code**: Save to `GCODE/` folder with naming convention
4. **Print**: Transfer to printer via USB/SD card

## Naming Convention

G-code files: `ProjectName_Date_Material.gcode`
- Example: `GingerbreadMan_2025-11-09_PLA.gcode`

## Printer Profiles

- **Ender3V2_BLTouch_Optimized.txt**: Optimized start/end G-code with BLTouch support

## Notes

- All temperatures in Celsius
- Bed temp default: 60°C (PLA), 70°C (PETG)
- Nozzle temp: See material specifications
