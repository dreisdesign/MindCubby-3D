#!/usr/bin/env python3
"""
Extract basic specifications from a G-code file.
Usage: python3 gcode_specs.py <gcode_file>
"""

import re
import sys
from pathlib import Path


def parse_gcode(filepath):
    """Parse G-code file and extract basic specs."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    specs = {
        'filename': Path(filepath).name,
        'nozzle_temp': None,
        'bed_temp': None,
        'layer_height': None,
        'nozzle_diameter': None,
        'filament_used_mm': None,
        'filament_used_g': None,
        'print_time_s': None,
        'total_lines': len(content.split('\n')),
    }

    # Extract temperatures from comments
    temp_match = re.search(r'M104 S(\d+)', content)
    if temp_match:
        specs['nozzle_temp'] = int(temp_match.group(1))

    bed_match = re.search(r'M140 S(\d+)', content)
    if bed_match:
        specs['bed_temp'] = int(bed_match.group(1))

    # Extract layer height (often in comment at top)
    layer_match = re.search(r';Layer height: ([\d.]+)', content)
    if layer_match:
        specs['layer_height'] = float(layer_match.group(1))

    # Extract nozzle diameter (usually in comment)
    nozzle_match = re.search(r';Nozzle diameter: ([\d.]+)', content)
    if nozzle_match:
        specs['nozzle_diameter'] = float(nozzle_match.group(1))

    # Extract filament used (in mm or mm^3, often in comment)
    filament_mm_match = re.search(r';Filament used: ([\d.]+)\s*m', content)
    if filament_mm_match:
        specs['filament_used_mm'] = float(filament_mm_match.group(1)) * 1000  # Convert m to mm

    filament_g_match = re.search(r';Filament used: [\d.]+\s*m\s.*?(\d+(?:\.\d+)?)\s*g', content)
    if filament_g_match:
        specs['filament_used_g'] = float(filament_g_match.group(1))

    # Extract print time (often in comment as estimated time)
    time_match = re.search(r';Print time: ([\d:]+)', content)
    if time_match:
        time_str = time_match.group(1)
        parts = time_str.split(':')
        if len(parts) == 3:  # HH:MM:SS
            specs['print_time_s'] = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        elif len(parts) == 2:  # MM:SS
            specs['print_time_s'] = int(parts[0]) * 60 + int(parts[1])

    return specs


def print_specs(specs):
    """Pretty-print extracted specs."""
    print(f"\n=== G-Code Specs: {specs['filename']} ===\n")

    if specs['nozzle_temp']:
        print(f"Nozzle Temp:       {specs['nozzle_temp']}°C")
    if specs['bed_temp']:
        print(f"Bed Temp:          {specs['bed_temp']}°C")
    if specs['layer_height']:
        print(f"Layer Height:      {specs['layer_height']:.2f} mm")
    if specs['nozzle_diameter']:
        print(f"Nozzle Diameter:   {specs['nozzle_diameter']:.1f} mm")
    if specs['filament_used_mm']:
        print(f"Filament Length:   {specs['filament_used_mm']:.0f} mm ({specs['filament_used_mm']/1000:.1f} m)")
    if specs['filament_used_g']:
        print(f"Filament Weight:   {specs['filament_used_g']:.1f} g")
    if specs['print_time_s']:
        hours = specs['print_time_s'] // 3600
        minutes = (specs['print_time_s'] % 3600) // 60
        seconds = specs['print_time_s'] % 60
        print(f"Est. Print Time:   {hours}h {minutes}m {seconds}s")

    print(f"Total G-Code Lines: {specs['total_lines']}\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 gcode_specs.py <gcode_file>")
        print("\nExample:")
        print("  python3 gcode_specs.py print.gcode")
        sys.exit(1)

    filepath = sys.argv[1]
    specs = parse_gcode(filepath)
    print_specs(specs)


if __name__ == '__main__':
    main()
