# AI Agent Instructions for MindCubby-3D

## Project Overview

**MindCubby-3D** is an automated 3D printing workflow repository for an Ender-3 V2 printer. It manages 15+ printable projects with automated spec extraction, Git integration, and Printables publishing pipeline.

### Key Architecture
- **`PRINTABLES/`** - Project folders (design + G-code + auto-generated specs)
- **`CURA-SETTINGS/`** - Printer profiles, start/end G-code templates
- **`scripts/`** - Automation: spec extraction (Python), CLI menu (Node.js)
- **`.githooks/pre-commit`** - Auto-triggers spec generation on every commit
- **`.github/instructions/`** - Copywriting templates for Printables listings

### Tech Stack
- Python 3 - G-code parsing and spec extraction (`scripts/gcode_specs.py`)
- Node.js 14+ - Interactive CLI menu (`scripts/menu.js`)
- Bash - Git hook coordination
- Git hooks - Pre-commit automation

---

## Critical Developer Workflows

### 1. Spec Generation (The Core Automation)
```bash
npm run p              # Quick: regenerate specs for changed PRINTABLES/ G-code
python3 scripts/gcode_specs.py <directory>  # Full: specify directory
```

**How it works:**
- Smart detection: compares `.gcode` vs `_printables-description.md` modification times
- Only processes changed files (47 files in ~1 sec if unchanged)
- Extracts from G-code comments: nozzle temp, bed temp, layer height
- **Calculates weight:** 1.25g per meter standard (from `;Filament used:` metadata)
- **Extracts time:** Parses `;TIME:` (seconds) → formats as H:M:S
- **Outputs:** Markdown table ready to copy/paste into Printables

**Key file:** `scripts/gcode_specs.py` - Contains `needs_update()`, `parse_gcode()`, `generate_printables_description()`

### 2. One-Command Commit Workflow
```bash
gcode-commit "Your message"
# Equivalently: npm run commit
```

**Execution order:**
1. Stages all changes (`git add -A`)
2. Pre-commit hook triggers (`.githooks/pre-commit`)
3. Hook runs spec generation for modified `.gcode` files
4. Stages generated `.md` files
5. Commits everything
6. Pre-commit hook pushes to origin

**Why it matters:** Specs are always in sync with G-code, preventing stale documentation.

### 3. Interactive CLI Menu
```bash
npm run menu
```

8 options accessible via arrow keys: Quick Commit, Generate Specs, Open PRINTABLES folder, Git Status, View Commits, Push, Setup Guide, Exit. Used for quick navigation without memorizing commands.

---

## Project-Specific Patterns & Conventions

### File Naming & Structure
- **Specs output:** `<gcode_basename>_printables-description.md` (NOT `.txt`)
- **Project folders:** `PRINTABLES/PRINTABLES_XX. Project Name/` (numbered, human-readable)
- **G-code files:** Always accompanied by `.3mf` Cura project in same folder
- **Git tracking:** `.md` specs tracked ✓, `.gcode` files excluded (regenerated on export)

### Data Extraction Patterns

**G-code comment parsing:** Lines like `;Nozzle Temp: 195°C` are parsed with regex
```python
# Example from gcode_specs.py
nozzle_temp = re.search(r';Nozzle Temp:\s*(\d+)°?C', line)
filament_length_m = re.search(r';Filament used:\s*([\d.]+)m', line)
time_seconds = re.search(r';TIME:\s*(\d+)', line)
```

**Weight calculation:** `weight = filament_length_m * 1.25` (standard PETG/PLA density). This is a deliberate approximation—do not change without updating documentation.

**Time formatting:** Converts seconds to `H:M:S` format for readability.

### Printables Integration
- **Copywriting template:** `.github/instructions/printables.instructions.md` - Defines structure (Title, Summary, Tags, Description) and tone (technical, metrics-focused, no sales language)
- **Output format:** Markdown table with 6 key fields (Nozzle Temp, Bed Temp, Layer Height, Weight, Filament Length, Print Time)
- **Workflow assumption:** User copies `*_printables-description.md` content directly into Printables description field

---

## Integration Points & External Dependencies

### Pre-Commit Hook Integration
- **Location:** `.githooks/pre-commit`
- **Trigger:** Every `git commit`
- **Side effect:** Modifies staging area (adds generated `.md` files)
- **Important:** Hook is configured via Git config (not standard `.git/hooks/` location)

### Cura Integration
- **Input:** `.3mf` files (Cura project format - ZIP with metadata + model)
- **Assumption:** User exports both `.3mf` + `.gcode` to project folder
- **Data source:** `.3mf` contains metadata for weight/time (attempted in code but G-code parsing is primary)

### Git Tracking Strategy
- **Tracked:** `.md` specs, `.3mf` projects, `.stl` models, `.curaprofile` configs
- **Excluded:** `.gcode` files (size, regenerated on each Cura export), media files (images/videos/PDFs)
- **Rationale:** Version control designs/specs, not build outputs

---

## When Modifying This Codebase

### Adding New Features
1. **Spec extraction:** Modify `parse_gcode()` in `scripts/gcode_specs.py`, update regex patterns
2. **Output format:** Modify `generate_printables_description()` to change markdown table layout
3. **CLI options:** Add to `scripts/menu.js` (menu structure) and `package.json` (npm scripts)
4. **Git hooks:** Update `.githooks/pre-commit` (test thoroughly—hook errors block commits)

### Key Files to Update Together
- `package.json` - npm script definitions
- `DOCUMENTATION/REFERENCE.md` - User-facing command documentation
- `CHANGELOG.md` - Version history
- `.github/instructions/printables.instructions.md` - Copywriting standards (if changing output format)

### Testing Workflows
```bash
# Test spec generation locally (no git commit)
npm run p

# Test menu functionality
npm run menu

# Verify Git hook would run (or run manually)
python3 scripts/gcode_specs.py PRINTABLES
```

---

## Quick Diagnostic Tips

- **Specs not generating?** Check `.githooks/pre-commit` is executable (`chmod +x .githooks/pre-commit`)
- **Wrong weights/times?** Verify G-code contains `;TIME:` and `;Filament used:` comments (Cura profile requirement)
- **Smart detection not working?** Check file modification times: `stat <file>` on `.gcode` vs `.md`
- **Menu issues?** Verify Node.js 14+: `node --version`

---

## Documentation References
- **User guide:** `DOCUMENTATION/REFERENCE.md` - Commands and typical workflow
- **Setup guide:** `DOCUMENTATION/SETUP.md` - Hardware specs, materials, Cura profiles
- **Copywriting:** `.github/instructions/printables.instructions.md` - Tone, structure, examples
- **This file:** `.github/copilot-instructions.md` - Architecture for AI agents
