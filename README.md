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

GCODE/                           # All G-code files & optimizations (organized)
├── active/                      # Active start/end and commonly used files
│   ├── START_GCODE.txt          # Currently active start G-code (tested)
│   └── END_GCODE.txt            # Currently active end G-code
├── variants/                    # Experimental or tuned variants
│   └── Optimized_StartGCode_v6.gcode
└── archived/                    # Historical/archived start/end sequences
	├── Ender3V2_Baseline_StartGCode.gcode
	└── Optimized_StartGCode_v1.gcode

MODELS/                          # 3D print files (STL/OBJ)
```

## Quick Start

1. Load profile from `GCODE/active/` (use `Ender3V2_BLTouch_Optimized.txt`)
2. Paste start code from `GCODE/active/START_GCODE.txt`
3. Check [DOCUMENTATION/QUICK_REFERENCE.md](DOCUMENTATION/QUICK_REFERENCE.md) for your material

## Latest Optimization

**v1.0** - Improved priming with 2-line parallel sequence (same Y direction)
- Cleaner nozzle appearance at print start
- See [CHANGELOG.md](CHANGELOG.md) for details
