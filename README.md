# MINDCUBBY 3D Printing Repository

Repository for 3D printing projects, G-code files, and printer configurations.

## 📚 Quick Start

**New to the repo?** Start here:
1. **[DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md)** - Fast lookup for common tasks
2. **[DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md)** - Printer specs and materials
3. **[PROFILES/README.md](PROFILES/README.md)** - How to load profiles

**All Documentation:** [DOCUMENTATION/README.md](DOCUMENTATION/README.md) (complete index)

## 📋 Key Resources

| Need | Go To |
|------|-------|
| Quick tasks & checklists | [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) |
| Hardware & materials | [DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md) |
| Using Copilot AI | [DOCUMENTATION/COPILOT_GUIDE.md](DOCUMENTATION/COPILOT_GUIDE.md) |
| Version history | [CHANGELOG.md](CHANGELOG.md) |
| G-code profiles | [PROFILES/README.md](PROFILES/README.md) |
| Structure analysis | [REPOSITORY_REVIEW.md](REPOSITORY_REVIEW.md) |

## Printer Setup
- **Printer**: Creality Ender-3 V2
- **Nozzle**: 0.4mm
- **Bed**: 220x220mm
- **Features**: BLTouch auto-leveling

## Repository Structure

```
MINDCUBBY-3D/
├── README.md                       # This file - main overview
├── CHANGELOG.md                    # Version history and changes
├── REPOSITORY_REVIEW.md            # Structure analysis
│
├── DOCUMENTATION/                  # 📚 All guides & references
│   ├── README.md                  # Documentation index
│   ├── QUICK_REFERENCE.md         # Fast lookup (START HERE!)
│   ├── PRINTER_SPECS.md           # Hardware & material profiles
│   ├── COPILOT_GUIDE.md           # Using AI for documentation
│   └── [Coming soon: TROUBLESHOOTING, MAINTENANCE, VERSION]
│
├── PROFILES/                       # G-code profiles & optimization
│   ├── README.md
│   ├── Ender3V2_Baseline_StartGCode.gcode
│   └── Ender3V2_BLTouch_Optimized.txt
│
├── GCODE/                          # Sliced print files
├── MODELS/                         # STL/OBJ 3D models
├── .github/
│   ├── chatmodes/
│   │   └── Ender-3 V2.chatmode.md # Custom chat mode
│   └── workflows/
│
└── .gitignore                      # Git configuration
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
