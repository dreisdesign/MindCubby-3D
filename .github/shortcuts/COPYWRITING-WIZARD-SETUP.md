# Printables Copywriting Wizard Setup

Complete guide for the Apple Shortcuts automation that generates Printables listing descriptions with G-code specifications and copywriting sections.

## Overview

The **Printables Copywriting Wizard** is an interactive Apple Shortcuts workflow that:
1. Asks 4 copywriting questions interactively
2. Collects the G-code file path
3. Generates a markdown file combining:
   - Extracted G-code specifications (nozzle temp, bed temp, layer height, weight, time)
   - Your copywriting answers formatted as an "About This Model" section

## System Components

### 1. Python Script: `gcode_specs_single.py`
**Location:** `/scripts/gcode_specs_single.py`

Processes a single G-code file and appends copywriting content.

**Input (via stdin):**
```
Line 1: Full path to .gcode file
Lines 2+: Copywriting answers (model name, primary function, key features, special notes)
```

**Output:**
- Generates `[filename]_printables-description.md` in the same directory as the G-code file
- Contains specs table + copywriting sections

**Example Run:**
```bash
cat << 'EOF' | python3 scripts/gcode_specs_single.py
/path/to/model.gcode
Model Display Name
What this model does
- Feature 1
- Feature 2
Optional special notes or instructions
EOF
```

### 2. Apple Shortcuts Workflow: `Printables-Copywriting-Wizard.shortcut`
**Location:** `.github/shortcuts/Printables-Copywriting-Wizard.shortcut`

Interactive user interface for collecting input and triggering the Python script.

**Workflow Steps:**
1. Create question list (4 prompts)
2. Loop through questions, collecting answers into a list
3. Ask user to select/enter the G-code file path
4. Combine all inputs into text block (newline-separated)
5. Run shell script with combined input
6. Display success message with file path

**Key Variables:**
- `questionsList` - Array of 4 questions
- `answers` - List of collected responses
- `gcodePath` - Full path to selected G-code file
- `allInput` - Combined text passed to Python script

### 3. AppleScript Wrapper: `script_printables--copywriting-wizard.scpt`
**Location:** `/shortcuts-scripts/script_printables--copywriting-wizard.scpt`

Bridges Stream Deck to the Shortcuts app for one-click triggering.

**Content:**
```applescript
tell application "Shortcuts Events"
    launch
    run the shortcut named "Printables-Copywriting-Wizard"
end tell
```

## Setup Instructions

### Prerequisites
- macOS with Apple Shortcuts app installed
- Python 3.8+
- Stream Deck (optional, for quick triggering)

### Step 1: Verify Python Script
Ensure `gcode_specs_single.py` exists and is executable:
```bash
cd /Users/danielreis/Documents/3D_PRINTING/MINDCUBBY-3D
ls -la scripts/gcode_specs_single.py
```

### Step 2: Import Shortcuts Workflow
1. Open Apple Shortcuts app
2. File → Import → Select `Printables-Copywriting-Wizard.shortcut`
3. Grant necessary permissions when prompted

### Step 3: Configure "Run Shell Script" Action
In the Shortcuts workflow, locate the "Run Shell Script" action and verify:

**Shell:** `bash`

**Command:**
```
/usr/bin/python3 /Users/danielreis/Documents/3D_PRINTING/MINDCUBBY-3D/scripts/gcode_specs_single.py
```

**Input:** Text variable containing combined input

**Pass Input:** `as stdin` ✓

### Step 4 (Optional): Set Up Stream Deck
1. Open Stream Deck application
2. Add "Execute Shell Script" or "Open URL" action
3. Point to `/Users/danielreis/shortcuts-scripts/script_printables--copywriting-wizard.scpt`
4. Configure as needed (name, icon, etc.)

## Usage

### Quick Start
1. Run the Shortcut (or press Stream Deck button if configured)
2. Answer 4 questions when prompted:
   - **Model Name** - Display name for the model
   - **Primary Function** - What the model does
   - **Key Features** - Feature list or description
   - **Special Notes** - Optional tips/warnings
3. Select or enter the full path to the `.gcode` file
4. Shortcut processes the file and generates markdown

### Example Workflow
```
Question 1: "What should we call this model?"
Answer: "Chip Clip - Print in Place"

Question 2: "What is the primary function?"
Answer: "Organizes and holds bags closed"

Question 3: "What are the key features?"
Answer: "- Flexible hinge for durability
- Compact design fits any drawer
- No supports needed"

Question 4: "Any special notes?"
Answer: "Use PETG for best flexibility. Test-print on a small model first."

Select file: /Users/danielreis/Documents/3D_PRINTING/MODELS/PRINTABLES_13.Chip-Clip/CE3E3V2_01-chip_clip--print_in_place.gcode

Output: CE3E3V2_01-chip_clip--print_in_place_printables-description.md
```

### Output Format
Generated markdown includes:

```markdown
## Print Specifications

| Specification | Value |
|---|---|
| Filament Length | 0.94 m |
| Estimated Weight | 1.18 g |
| Estimated Print Time | 19m 50s |

## Notes

- Optimized for **Ender-3 V2** with **BLTouch** bed leveling
- Uses off-print purge line to prevent nozzle blobs
- Exported from **Cura** with custom profile
- Recommended: Test on a small print first before large jobs

## About This Model

**Chip Clip - Print in Place**

Organizes and holds bags closed

### Key Features
- Flexible hinge for durability
- Compact design fits any drawer
- No supports needed

### Special Notes
Use PETG for best flexibility. Test-print on a small model first.
```

## Troubleshooting

### "File not found" Error
- **Cause:** G-code file path is incorrect or incomplete
- **Fix:** Verify the full absolute path to the `.gcode` file exists
- **Example correct path:** `/Users/danielreis/Documents/3D_PRINTING/MODELS/PRINTABLES_13.Chip-Clip/CE3E3V2_01-chip_clip--print_in_place.gcode`

### "SyntaxError: invalid syntax" in Shortcuts
- **Cause:** Run Shell Script action has wrong Shell setting (likely set to Python instead of bash)
- **Fix:** Change Shell dropdown to `bash` or `zsh`

### Output file not created
- **Cause:** Python script has no write permissions or file path issues
- **Fix:** 
  1. Check directory permissions: `ls -ld /path/to/directory`
  2. Test script manually: `cat input.txt | python3 scripts/gcode_specs_single.py`

### Questions not asking in order
- **Cause:** Shortcuts loop configuration issue
- **Fix:** Verify "Repeat with each item in list" loop contains "Ask for Text" action

## File Locations Reference

| Component | Path |
|-----------|------|
| Python Script | `scripts/gcode_specs_single.py` |
| Shortcuts Workflow | `.github/shortcuts/Printables-Copywriting-Wizard.shortcut` |
| AppleScript Wrapper | `/shortcuts-scripts/script_printables--copywriting-wizard.scpt` |
| Documentation | `.github/shortcuts/COPYWRITING-WIZARD-SETUP.md` |

## Customization

### Change Questions
Edit the `questionsList` in the Shortcuts workflow to modify prompts.

### Modify Output Format
Edit the "About This Model" section in `gcode_specs_single.py` (lines 91-99):
```python
# Append copywriting answers
if answers_text.strip():
    printables_desc += "\n## About This Model\n\n"
    printables_desc += answers_text.strip() + "\n"
```

### Add More G-code Fields
Modify `parse_gcode()` function in `gcode_specs_single.py` to extract additional fields from G-code comments.

## Related Files

- **Copywriting Guidelines:** `.github/prompts/copywriting.prompt.md` - Tone, structure, and examples for Printables copy
- **Original Recursive Script:** `scripts/gcode_specs.py` - For batch processing directories
- **Git Hooks:** `.githooks/pre-commit` - Auto-generates specs on every commit

## Quick Reference: Manual Testing

Test the script without Shortcuts:
```bash
cd /Users/danielreis/Documents/3D_PRINTING/MINDCUBBY-3D

cat << 'EOF' | python3 scripts/gcode_specs_single.py
/path/to/your/model.gcode
Model Name
Primary Function
Key Features
Special Notes
EOF
```

Expected output: `✓ Generated: /path/to/your/model_printables-description.md`
