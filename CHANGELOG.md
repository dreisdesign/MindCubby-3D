# Changelog

All changes to the MINDCUBBY-3D repository.

## [2.1.0] - 2025-11-29

### OctoPrint Setup & PrusaSlicer Integration 🖨️

#### Added
- **OctoPrint Server Installation** on macOS with `caffeinate` sleep prevention
- **Start Script** (`scripts/start-octoprint.sh`) for easy OctoPrint launch on port 5001
- **Serial Configuration Fix** - Checksum bypass for mriscoc firmware compatibility
- **PrusaSlicer Integration** - Direct printing to OctoPrint via Global API Key
- **Etsy Shop Branding** - Professional shop title and copy in `.github/instructions/etsy.profile.md`
  - Title: "Delightfully Engineered 3D Design: Form, Function, Fun" (54 chars)
  - Tagline: "I design and engineer functional 3D art that is precise, modular, and delightfully fun to use."
  - Complete about story focused on design systems and functional art

#### Fixed
- **OctoPrint Connection Issue** - "Device not configured" error resolved:
  1. Replaced faulty USB cable
  2. Enabled macOS USB security approval
  3. Added serial checksum bypass to `~/Library/Application Support/OctoPrint/config.yaml`
- **First Layer Quality** - Fixed prime line from `X150 Y205` to `X10 Y205` (prevents nozzle dragging)

#### Configuration
- **OctoPrint Port:** 5001 (avoids macOS AirPlay Receiver on 5000)
- **Printer Profile:** Ender-3 V2 with mriscoc firmware 2.1.3, BLTouch, PEI bed
- **Serial Settings:** 
  ```yaml
  serial:
    sendChecksumWithUnknownCommands: false
    neverSendChecksums: true
    receiveAll: true
  ```
- **Baud Rate:** 115200

#### Documentation
- Created `DOCUMENTATION/OCTOPRINT_SETUP.md` (installation, configuration, PrusaSlicer integration)
- Updated `scripts/start-octoprint.sh` with setup reminders

## [2.0.1] - 2025-11-13

### Documentation Consolidation 📚
Streamlined documentation structure for better navigation and maintainability.

#### Changes
- **Consolidated 6 files** into 2 focused documents (759 lines removed, 36% reduction)
  - Removed: `WORKFLOW.md`, `QUICK_REFERENCE.md`, `PRINTER_SPECS.md`, `CURA_PROFILE_MANAGEMENT.md`, `MULTI_MATERIAL_SETUP.md`, `MILESTONE_1.md`
  - Created: `DOCUMENTATION/SETUP.md` (hardware, materials, profiles, troubleshooting)
  - Created: `DOCUMENTATION/REFERENCE.md` (commands, workflows, tips, benchmarks, FAQ)
  
- **Updated Navigation** in README.md
  - Quick Links: 3 documentation links → 2 consolidated links
  - Directory structure: reflects new doc organization
  
#### Benefits
- Easier to find information (2 focused files vs 6 overlapping files)
- Reduced documentation maintenance burden
- Better cross-referencing between setup and reference topics
- Cleaner repository structure

## [2.0.0] - 2025-11-12

### Complete Automation System ⚡
Major release with comprehensive automation for print-to-Printables workflow.

#### Features
- **Automated Spec Generation** - Extract weight, time, temps from G-code
  - Parses nozzle/bed temperature from G-code comments
  - Calculates filament weight (1.25g per meter standard)
  - Extracts print time from `;TIME:` metadata
  - Generates markdown tables ready for Printables
  
- **Smart Change Detection** - Only regenerate changed files
  - Compares `.gcode` vs `_printables-description.md` modification times
  - Skip unchanged files (47 files in ~1 sec if all unchanged)
  - Reduces redundant processing
  
- **Git Integration** - Auto-generate specs on commit
  - Pre-commit hooks trigger spec generation
  - Updated files auto-staged before commit
  - Transparent to user workflow
  
- **Interactive CLI Menu** - Beautiful terminal UI
  - 8 options for common tasks
  - Arrow key navigation
  - Real-time git integration
  - One-command workflows

#### Commands
- `npm run menu` - Interactive CLI menu
- `npm run p` - Quick spec generation (PRINTABLES folder)
- `npm run specs [dir]` - Generate specs for directory  
- `gcode-commit "msg"` - One-line commit with auto specs
- `npm run commit` - Alternative commit method

#### Files Added
- `DOCUMENTATION/WORKFLOW.md` - Complete automation guide
- `scripts/gcode_specs.py` - Enhanced with weight/time extraction
- `scripts/menu.js` - Interactive CLI with arrow navigation
- `scripts/gcode-commit.sh` - Quick commit helper
- `.githooks/pre-commit` - Auto-generation hook

#### Files Updated
- `README.md` - New quick start and automation focus
- `.gitignore` - Track `.md`, `.3mf`, `.stl` specs and models
- `package.json` - New npm scripts and dependencies

#### Repository Cleanup
- Removed 31 media files from tracking (images, videos, PDFs)
- Removed old `.txt` spec files (replaced with `.md`)
- Final tracked files: 218 (down from 249)

### Tracked File Types (Final)
- **72 Markdown** - `*_printables-description.md` spec tables  
- **91 3D Models** - `.stl` source files
- **21 Cura Projects** - `.3mf` files with settings
- **8 G-Code** - Start/end code templates
- **3 Cura Profiles** - `.curaprofile` configurations

### Example Output
```
## Print Specifications

| Specification | Value |
|---|---|
| Nozzle Temperature | 195°C |
| Bed Temperature | 65°C |
| Layer Height | 0.20 mm |
| Filament Weight | 3.9 g |
| Filament Length | 3.09 m |
| Estimated Print Time | 1h 33m 54s |
```

### Documentation
- Complete workflow guide in `DOCUMENTATION/WORKFLOW.md`
- Updated README with quick commands
- Security best practices documented
- Troubleshooting guide included

---

## [1.0.1] - 2025-11-10

### Added
- `CURA-SETTINGS/variants/Optimized_StartGCode_v6.gcode` — New start G-code variant that lowers the initial Z used for priming/skirt (0.15 mm) to improve first-layer adhesion when prints otherwise require a manual Z-offset adjustment after the skirt.

### Notes
- This change is non-destructive to the baseline files. Use `Ender3V2_Baseline_StartGCode.gcode` for rollback. If you have a probe, consider enabling mesh leveling (G29) or using a saved mesh (M420 S1) before priming.

## [1.0.2] - 2025-11-10

### Changed
- Reorganized `CURA-SETTINGS/` into `active/`, `variants/`, and `archived/` to make it easier to find the currently used start/end code, optimized variants, and historical archives. Updated docs to reference `CURA-SETTINGS/active/START_GCODE.txt` as the active start file.

## [1.0.3] - 2025-11-11

### Fixed
- `CURA-SETTINGS/active/START_GCODE.txt`: Moved priming off-print (corner/back-edge purge) and added a retract → lift → wipe → micro-prime sequence to prevent nozzle blobs being picked up and dragged across the first layer. This reduces first-layer failures caused by deposited blobs during skirt/priming.

### Files
- `CURA-SETTINGS/active/START_GCODE.txt` — updated priming sequence
- `DOCUMENTATION/QUICK_REFERENCE.md` — documented the off-print purge and added verification steps



---

## Guidelines for Updates

### When Adding New Features
- Document changes here first
- Update relevant README files
- Include version bump if applicable

### Version Format
- **Major.Minor.Patch** (e.g., 1.0.0)
- Major: Breaking changes to profiles or workflow
- Minor: New profiles, documentation, or features
- Patch: Bug fixes, improvements, documentation updates

### Documentation Standards
- Keep README files in sync with actual repository structure
- Update CHANGELOG.md immediately after changes
- Include dates and clear descriptions
- Link to related files when applicable

---

## Categories for Changes
- **Added**: New features or files
- **Changed**: Modifications to existing content
- **Deprecated**: Features marked for removal
- **Removed**: Deleted features or files
- **Fixed**: Bug fixes or corrections
- **Security**: Security updates

---

## Recent Changes Template

When making updates, use this template:

```markdown
## [X.X.X] - YYYY-MM-DD

### Added
- Feature/file name and brief description

### Changed
- What was modified and why

### Fixed
- What bug was fixed
```
