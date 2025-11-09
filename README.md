# MINDCUBBY 3D Printing Repository

Repository for 3D printing projects, G-code files, and printer configurations.

## Printer Setup
- **Printer**: Creality Ender-3 V2
- **Nozzle**: 0.4mm
- **Bed**: 220x220mm
- **Features**: BLTouch auto-leveling

## Repository Structure

```
MINDCUBBY-3D/
├── DOCUMENTATION/          # Printer specs, setup guides, profiles
├── GCODE/                   # Sliced G-code files
├── MODELS/                  # STL/OBJ 3D models (if tracked)
├── PROFILES/                # Cura profiles and configurations
└── README.md
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
