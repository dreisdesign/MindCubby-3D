#!/usr/bin/env python3
"""
Process a single G-code file and append copywriting answers.
Reads from stdin:
  Line 1: path to .gcode file
  Line 2+: copywriting answers (model name, primary function, key features, special notes)
"""

import re
import sys
import os
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_gcode(filepath):
    """Parse G-code file and extract specifications."""
    specs = {
        'nozzle_temp': None,
        'bed_temp': None,
        'layer_height': None,
        'filament_length_m': None,
        'weight_g': None,
        'print_time_s': None,
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                
                # Nozzle temperature
                if not specs['nozzle_temp']:
                    match = re.search(r';Nozzle Temp:\s*(\d+)', line)
                    if match:
                        specs['nozzle_temp'] = int(match.group(1))
                
                # Bed temperature
                if not specs['bed_temp']:
                    match = re.search(r';Bed Temp:\s*(\d+)', line)
                    if match:
                        specs['bed_temp'] = int(match.group(1))
                
                # Layer height
                if not specs['layer_height']:
                    match = re.search(r';Layer Height:\s*([\d.]+)', line)
                    if match:
                        specs['layer_height'] = float(match.group(1))
                
                # Filament length in meters
                if not specs['filament_length_m']:
                    match = re.search(r';Filament used:\s*([\d.]+)\s*m', line)
                    if match:
                        filament_m = float(match.group(1))
                        specs['filament_length_m'] = filament_m
                        # Calculate weight: 1.25g per meter (standard PETG/PLA)
                        specs['weight_g'] = round(filament_m * 1.25, 2)
                
                # Print time in seconds
                if not specs['print_time_s']:
                    match = re.search(r';TIME:\s*(\d+)', line)
                    if match:
                        specs['print_time_s'] = int(match.group(1))
    
    except IOError as e:
        print(f"Error reading G-code file '{filepath}': {e}", file=sys.stderr)
        return None
    
    return specs


def generate_printables_description(specs):
    """Generate Printables-compatible markdown description from specs."""
    desc = "## Print Specifications\n\n"
    desc += "| Specification | Value |\n"
    desc += "|---|---|\n"
    
    if specs['nozzle_temp']:
        desc += f"| Nozzle Temperature | {specs['nozzle_temp']}°C |\n"
    
    if specs['bed_temp']:
        desc += f"| Bed Temperature | {specs['bed_temp']}°C |\n"
    
    if specs['layer_height']:
        desc += f"| Layer Height | {specs['layer_height']} mm |\n"
    
    if specs['filament_length_m']:
        desc += f"| Filament Length | {specs['filament_length_m']} m |\n"
    
    if specs['weight_g']:
        desc += f"| Estimated Weight | {specs['weight_g']} g |\n"
    
    if specs['print_time_s']:
        hours = specs['print_time_s'] // 3600
        minutes = (specs['print_time_s'] % 3600) // 60
        seconds = specs['print_time_s'] % 60
        if hours > 0:
            desc += f"| Estimated Print Time | {hours}h {minutes}m {seconds}s |\n"
        else:
            desc += f"| Estimated Print Time | {minutes}m {seconds}s |\n"
    
    desc += "\n## Notes\n\n"
    desc += "- Optimized for **Ender-3 V2** with **BLTouch** bed leveling\n"
    desc += "- Uses off-print purge line to prevent nozzle blobs\n"
    desc += "- Exported from **Cura** with custom profile\n"
    desc += "- Recommended: Test on a small print first before large jobs\n"
    
    return desc


def process_single_file(filepath, answers_text):
    """Process a single G-code file and append copywriting answers."""
    gcode_path = Path(filepath)
    
    if not gcode_path.exists():
        print(f"Error: G-code file '{filepath}' not found.", file=sys.stderr)
        return False
    
    if gcode_path.suffix.lower() != '.gcode':
        print(f"Error: '{filepath}' is not a .gcode file.", file=sys.stderr)
        return False
    
    # Parse the G-code
    specs = parse_gcode(filepath)
    if specs is None:
        return False
    
    # Generate specs description
    printables_desc = generate_printables_description(specs)
    
    # Append copywriting answers
    if answers_text.strip():
        printables_desc += "\n## About This Model\n\n"
        printables_desc += answers_text.strip() + "\n"
    
    # Write to output file
    printables_path = gcode_path.with_stem(gcode_path.stem + '_printables-description').with_suffix('.md')
    
    try:
        with open(printables_path, 'w', encoding='utf-8') as f:
            f.write(printables_desc)
        print(f"✓ Generated: {printables_path}")
        return True
    except IOError as e:
        print(f"Error writing file '{printables_path}': {e}", file=sys.stderr)
        return False


def main():
    """Main entry point - read from stdin."""
    input_lines = sys.stdin.read().strip().split('\n')
    
    if len(input_lines) < 1:
        print("Error: No input provided", file=sys.stderr)
        sys.exit(1)
    
    gcode_filename = input_lines[0].strip()
    answers_text = '\n'.join(input_lines[1:]) if len(input_lines) > 1 else ""
    
    if process_single_file(gcode_filename, answers_text):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
