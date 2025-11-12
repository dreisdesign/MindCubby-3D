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
    """Format extracted specs as a string."""
    output = f"\n=== G-Code Specs: {specs['filename']} ===\n\n"

    if specs['nozzle_temp']:
        output += f"Nozzle Temp:       {specs['nozzle_temp']}°C\n"
    if specs['bed_temp']:
        output += f"Bed Temp:          {specs['bed_temp']}°C\n"
    if specs['layer_height']:
        output += f"Layer Height:      {specs['layer_height']:.2f} mm\n"
    if specs['nozzle_diameter']:
        output += f"Nozzle Diameter:   {specs['nozzle_diameter']:.1f} mm\n"
    if specs['filament_used_mm']:
        output += f"Filament Length:   {specs['filament_used_mm']:.0f} mm ({specs['filament_used_mm']/1000:.1f} m)\n"
    if specs['filament_used_g']:
        output += f"Filament Weight:   {specs['filament_used_g']:.1f} g\n"
    if specs['print_time_s']:
        hours = specs['print_time_s'] // 3600
        minutes = (specs['print_time_s'] % 3600) // 60
        seconds = specs['print_time_s'] % 60
        output += f"Est. Print Time:   {hours}h {minutes}m {seconds}s\n"

    output += f"Total G-Code Lines: {specs['total_lines']}\n"
    
    return output


def generate_printables_description(specs):
    """Generate a Printables-friendly description with specs."""
    desc = "## Print Specifications\n\n"
    
    if specs['nozzle_temp']:
        desc += f"- **Nozzle Temperature:** {specs['nozzle_temp']}°C\n"
    if specs['bed_temp']:
        desc += f"- **Bed Temperature:** {specs['bed_temp']}°C\n"
    if specs['layer_height']:
        desc += f"- **Layer Height:** {specs['layer_height']:.2f} mm\n"
    if specs['filament_used_mm']:
        desc += f"- **Filament Length:** {specs['filament_used_mm']/1000:.2f} m ({specs['filament_used_mm']:.0f} mm)\n"
    if specs['filament_used_g']:
        desc += f"- **Filament Weight:** {specs['filament_used_g']:.1f} g\n"
    if specs['print_time_s']:
        hours = specs['print_time_s'] // 3600
        minutes = (specs['print_time_s'] % 3600) // 60
        desc += f"- **Estimated Print Time:** {hours}h {minutes}m\n"
    
    desc += "\n## Notes\n\n"
    desc += "- This print is optimized for the **Ender-3 V2** with **BLTouch**.\n"
    desc += "- Uses off-print purge to prevent nozzle blobs on first layer.\n"
    desc += "- Compatible with Cura slicer.\n"
    desc += "- Test on a small print first before large jobs.\n"
    
    return desc


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 gcode_specs.py <gcode_file>")
        print("\nExample:")
        print("  python3 gcode_specs.py print.gcode")
        print("  → Output: print.txt (specs)")
        print("  → Output: print_printables.txt (shareable description)")
        sys.exit(1)

    filepath = sys.argv[1]
    specs = parse_gcode(filepath)
    output = print_specs(specs)
    printables_desc = generate_printables_description(specs)
    
    # Write to .txt file with same name as gcode file
    gcode_path = Path(filepath)
    specs_path = gcode_path.with_suffix('.txt')
    printables_path = gcode_path.with_stem(gcode_path.stem + '_printables').with_suffix('.txt')
    
    try:
        with open(specs_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✓ Specs saved to: {specs_path}")
        
        with open(printables_path, 'w', encoding='utf-8') as f:
            f.write(printables_desc)
        print(f"✓ Printables description saved to: {printables_path}")
        
        print(output)
        print("\n" + "="*60)
        print("PRINTABLES-READY DESCRIPTION:\n")
        print(printables_desc)
    except IOError as e:
        print(f"Error writing files: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
