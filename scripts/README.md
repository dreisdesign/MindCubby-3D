# G-Code Scripts

Quick utility scripts for working with G-code files.

## `gcode_specs.py`

Extract basic specifications from a G-code file.

**Usage:**
```bash
python3 gcode_specs.py <gcode_file>
```

**Example:**
```bash
python3 gcode_specs.py MODELS/01.Chip-Clip/CE3E3V2_01-chip_clip--print_in_place.gcode
```

**Output:**
```
=== G-Code Specs: CE3E3V2_01-chip_clip--print_in_place.gcode ===

Nozzle Temp:       218°C
Bed Temp:          70°C
Layer Height:      0.20 mm
Nozzle Diameter:   0.4 mm (if available)
Filament Length:   943 mm (0.9 m)
Filament Weight:   2.3 g (if available)
Est. Print Time:   1h 23m 45s (if available)
Total G-Code Lines: 16862
```

**What it extracts:**
- Nozzle and bed temperatures
- Layer height
- Nozzle diameter
- Filament length (mm) and weight (grams)
- Estimated print time
- Total line count

**Tips:**
- Cura exports most of these as comments in the G-code, so availability depends on your slicer settings.
- Useful for quick validation before printing or for tracking print specs in your model library.

---

**Last Updated:** 2025-11-12
