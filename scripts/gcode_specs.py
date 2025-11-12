#!/usr/bin/env python3
"""
Extract basic specifications from G-code files and .3mf files.
Usage: python3 gcode_specs.py [<gcode_file_or_directory>]

If a directory is provided, recursively processes all .gcode files.
If a file is provided, processes that single file.
If no argument provided, processes current directory.

Smart mode: Only processes files newer than their corresponding .md file (if it exists).
"""

import re
import sys
import os
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


def needs_update(gcode_file):
    """Check if .gcode file is newer than its _printables-description.md file."""
    gcode_path = Path(gcode_file)
    printables_path = gcode_path.with_stem(gcode_path.stem + '_printables-description').with_suffix('.md')
    
    # If no _printables-description.md file exists, file needs processing
    if not printables_path.exists():
        return True
    
    # Compare modification times
    gcode_mtime = os.path.getmtime(gcode_path)
    printables_mtime = os.path.getmtime(printables_path)
    
    # If .gcode is newer than _printables-description.md, it needs processing
    return gcode_mtime > printables_mtime


def extract_3mf_metadata(gcode_filepath):
    """Extract weight and time from corresponding .3mf file if it exists."""
    gcode_path = Path(gcode_filepath)
    threemf_path = gcode_path.with_suffix('.3mf')
    
    metadata = {'weight_g': None, 'time_s': None}
    
    if not threemf_path.exists():
        return metadata
    
    try:
        with zipfile.ZipFile(threemf_path, 'r') as zf:
            # Read the Cura-specific metadata file
            try:
                cura_xml = zf.read('Cura/metadata.xml').decode('utf-8')
                root = ET.fromstring(cura_xml)
                
                # Extract weight and time from Cura metadata
                for child in root:
                    if child.tag.endswith('setting') or 'weight' in child.tag.lower():
                        text = child.text or ''
                        # Look for weight value
                        if 'weight' in child.tag.lower() and text:
                            try:
                                metadata['weight_g'] = float(text)
                            except ValueError:
                                pass
                    # Look for time in any element
                    if 'time' in child.tag.lower() and text:
                        try:
                            # Parse time if it's in seconds
                            metadata['time_s'] = float(text)
                        except ValueError:
                            pass
                            
            except KeyError:
                # Try alternative metadata locations
                pass
                
    except Exception as e:
        pass  # Silently fail if .3mf can't be read
    
    return metadata


def parse_gcode(filepath):
    """Parse G-code file and extract basic specs."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None

    specs = {
        'filename': Path(filepath).name,
        'filepath': str(filepath),
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

    # Extract print time (in seconds from ;TIME: comment)
    time_match = re.search(r';TIME:(\d+)', content)
    if time_match:
        specs['print_time_s'] = int(time_match.group(1))

    # Extract filament used (in meters from ;Filament used:)
    filament_mm_match = re.search(r';Filament used: ([\d.]+)\s*m(?!\w)', content)
    if filament_mm_match:
        filament_m = float(filament_mm_match.group(1))
        specs['filament_used_mm'] = filament_m * 1000  # Convert m to mm
        # Calculate weight: standard 1.75mm PLA/PETG is ~1.25g per meter
        specs['filament_used_g'] = filament_m * 1.25
    
    # Try to find explicit weight if provided
    filament_g_match = re.search(r';Filament used:.*?(\d+(?:\.\d+)?)\s*g', content)
    if filament_g_match:
        specs['filament_used_g'] = float(filament_g_match.group(1))

    # Try to extract weight and time from .3mf if not found in G-code
    threemf_metadata = extract_3mf_metadata(filepath)
    if threemf_metadata['weight_g'] and not specs['filament_used_g']:
        specs['filament_used_g'] = threemf_metadata['weight_g']
    if threemf_metadata['time_s'] and not specs['print_time_s']:
        specs['print_time_s'] = threemf_metadata['time_s']

    return specs


def format_specs(specs):
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
    """Generate a Printables-friendly markdown description with table format."""
    desc = "## Print Specifications\n\n"
    desc += "| Specification | Value |\n"
    desc += "|---|---|\n"
    
    if specs['nozzle_temp']:
        desc += f"| Nozzle Temperature | {specs['nozzle_temp']}°C |\n"
    if specs['bed_temp']:
        desc += f"| Bed Temperature | {specs['bed_temp']}°C |\n"
    if specs['layer_height']:
        desc += f"| Layer Height | {specs['layer_height']:.2f} mm |\n"
    if specs['nozzle_diameter']:
        desc += f"| Nozzle Diameter | {specs['nozzle_diameter']} mm |\n"
    
    # Filament info
    if specs['filament_used_g']:
        desc += f"| Filament Weight | {specs['filament_used_g']:.1f} g |\n"
    if specs['filament_used_mm']:
        desc += f"| Filament Length | {specs['filament_used_mm']/1000:.2f} m |\n"
    
    # Print time
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


def process_file(filepath):
    """Process a single G-code file and generate Printables markdown output."""
    specs = parse_gcode(filepath)
    if specs is None:
        return False
    
    printables_desc = generate_printables_description(specs)
    
    gcode_path = Path(filepath)
    printables_path = gcode_path.with_stem(gcode_path.stem + '_printables-description').with_suffix('.md')
    
    try:
        with open(printables_path, 'w', encoding='utf-8') as f:
            f.write(printables_desc)
        return True
    except IOError as e:
        print(f"Error writing file for '{filepath}': {e}")
        return False


def main():
    """Main entry point."""
    # Determine target: file, directory, or current directory
    if len(sys.argv) < 2:
        target = Path.cwd()
        print(f"No argument provided; scanning current directory: {target}\n")
    else:
        target = Path(sys.argv[1])
    
    if not target.exists():
        print(f"Error: Path '{target}' does not exist.")
        sys.exit(1)
    
    gcode_files = []
    
    if target.is_file():
        # Single file
        if target.suffix.lower() == '.gcode':
            gcode_files = [target]
        else:
            print(f"Error: '{target}' is not a .gcode file.")
            sys.exit(1)
    elif target.is_dir():
        # Directory: recursively find all .gcode files
        gcode_files = sorted(target.rglob('*.gcode'))
        if not gcode_files:
            print(f"No .gcode files found in '{target}' or subdirectories.")
            sys.exit(0)
    
    print(f"Processing {len(gcode_files)} G-code file(s)...\n")
    
    success_count = 0
    for gcode_file in gcode_files:
        # Skip if file hasn't changed
        if not needs_update(gcode_file):
            continue
        
        print(f"→ {gcode_file.relative_to(target.parent if target.is_file() else target.parent)}")
        if process_file(gcode_file):
            success_count += 1
            specs = parse_gcode(gcode_file)
            print(format_specs(specs))
        else:
            print(f"  ✗ Failed to process\n")
    
    if success_count == 0:
        print("✓ All files up to date, nothing to process")
    else:
        print(f"\n✓ Successfully processed {success_count}/{len(gcode_files)} files")


if __name__ == '__main__':
    main()
