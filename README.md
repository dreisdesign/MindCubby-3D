# MINDCUBBY 3D Printing Repository

Ender-3 V2 configuration, G-code optimizations, and printer reference.

**Printer**: Creality Ender-3 V2 + BLTouch | **Nozzle**: 0.4mm | **Bed**: 220x220mm

## Quick Links

| Need | File |
|------|------|
| Common tasks & fixes | [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) |
| Printer specs & materials | [DOCUMENTATION/PRINTER_SPECS.md](DOCUMENTATION/PRINTER_SPECS.md) |
| Changes & history | [CHANGELOG.md](CHANGELOG.md) |

## Repository

```
DOCUMENTATION/
├── QUICK_REFERENCE.md          # Tasks, troubleshooting, commands
└── PRINTER_SPECS.md            # Hardware & material profiles

GCODE/                           # All G-code files & optimizations
├── Ender3V2_Baseline_StartGCode.gcode
├── Ender3V2_BLTouch_Optimized.txt
├── Original_StartGCode_Archive.gcode
└── Optimized_StartGCode_v1.gcode

MODELS/                          # 3D print files (STL/OBJ)
```

## Quick Start

1. Load profile from `GCODE/` (use `Ender3V2_BLTouch_Optimized.txt`)
2. Paste start code from `GCODE/Optimized_StartGCode_v1.gcode`
3. Check [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) for your material

## Latest Optimization

**v1.0** - Improved priming with 2-line parallel sequence (same Y direction)
- Cleaner nozzle appearance at print start
- See [CHANGELOG.md](CHANGELOG.md) for details
