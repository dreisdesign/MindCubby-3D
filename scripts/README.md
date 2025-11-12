# G-Code Scripts

Quick utility scripts for working with G-code files.

## `gcode_specs.py`

Extract specifications from G-code files recursively across directories or process individual files.

**Usage:**
```bash
# Process a single file
python3 gcode_specs.py <gcode_file>

# Process all .gcode files in a directory recursively
python3 gcode_specs.py <directory>

# Process current directory (if run from within a directory with .gcode files)
python3 gcode_specs.py
```

**Examples:**
```bash
# Single file
python3 gcode_specs.py MODELS/01.Chip-Clip/CE3E3V2_01-chip_clip--print_in_place.gcode

# Entire PRINTABLES folder (47 files)
python3 gcode_specs.py PRINTABLES/

# Current directory
cd PRINTABLES && python3 ../scripts/gcode_specs.py
```

**Output Files:**
For each `.gcode` file found, generates two output files:
- `filename.txt` — Raw specs summary
- `filename_printables.txt` — Formatted description for Printables

**Example output (filename.txt):**
```
=== G-Code Specs: CE3E3V2_01-chip_clip--print_in_place.gcode ===

Nozzle Temp:       218°C
Bed Temp:          70°C
Layer Height:      0.20 mm
Filament Length:   943 mm (0.9 m)
Total G-Code Lines: 16860
```

**What it extracts:**
- Nozzle and bed temperatures
- Layer height
- Nozzle diameter
- Filament length (mm) and weight (grams)
- Estimated print time
- Total G-code line count

**Tips:**
- Runs recursively through subdirectories, making it ideal for batch processing large print archives
- Cura exports most specs as comments in the G-code header
- Each G-code file gets two corresponding `.txt` files for reference and sharing
- Useful for cataloging prints, validating specs before printing, or generating Printables descriptions

---

**Last Updated:** 2025-11-12
