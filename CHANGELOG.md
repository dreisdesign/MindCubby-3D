# Changelog

All notable changes to the MINDCUBBY 3D Printing Repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GCODE/README.md - Guide for G-code optimization experiments
- GCODE/CHANGELOG.md - Track G-code version improvements
- GCODE/Original_StartGCode_Archive.gcode - Baseline for reference
- GCODE/Optimized_StartGCode_v1.gcode - First optimization: 2-line parallel priming

### Changed
- Moved analysis docs to DOCUMENTATION/ (REPOSITORY_REVIEW.md, MARKDOWN_CONSOLIDATION.md)
- Cleaner root directory - focus on essential files
- Updated README.md with better resource links
- Reorganized repository structure for clarity

### Optimization: v1.0 Improved Priming
- **Change**: Priming sequence now uses 2 parallel lines in same direction (Y-axis)
- **Benefit**: Cleaner nozzle at start of print, less messy primer appearance
- **File**: GCODE/Optimized_StartGCode_v1.gcode

### Changed
- Merged remote README with local documentation

### Fixed
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
