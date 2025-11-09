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
- **File**: `GCODE/Optimized_StartGCode_v1.gcode`
- **Benefit**: Cleaner nozzle appearance at print start
- **Status**: Active

### Repository Structure
- `Ender3V2_Baseline_StartGCode.gcode` - Reference baseline
- `Original_StartGCode_Archive.gcode` - Original working version
- `Optimized_StartGCode_v1.gcode` - First optimization iteration
- Conflict resolution in README.md during initial push

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
