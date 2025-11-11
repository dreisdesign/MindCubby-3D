# Changelog

All changes to the MINDCUBBY-3D repository.

## [1.0.0] - 2025-11-09

### Initial Release
- Repository initialized with Ender-3 V2 documentation
- GCODE optimization experiments directory
- PROFILES/ with BLTouch optimized configuration
- DOCUMENTATION/ with quick reference and printer specs

### G-Code Optimization: v1.0 Improved Priming
- **Change**: Priming sequence now uses 2 parallel lines in same direction (Y-axis)
 - **File**: `CURA-SETTINGS/variants/Optimized_StartGCode_v1.gcode`
- **Benefit**: Cleaner nozzle appearance at print start
- **Status**: Active

### Repository Structure
- `Ender3V2_Baseline_StartGCode.gcode` - Reference baseline
- `Original_StartGCode_Archive.gcode` - Original working version
- `Optimized_StartGCode_v1.gcode` - First optimization iteration
- Conflict resolution in README.md during initial push

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
