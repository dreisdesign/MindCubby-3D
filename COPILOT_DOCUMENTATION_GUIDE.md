# GitHub Copilot Documentation Maintenance Guide

This guide helps you maintain accurate documentation across the repository using GitHub Copilot.

## Overview

Documentation is kept in multiple locations:
- `README.md` - Main repository overview
- `DOCUMENTATION/PRINTER_SPECS.md` - Detailed printer specifications
- `PROFILES/README.md` - Cura profile usage instructions
- `CHANGELOG.md` - Version history and changes

## Copilot Instructions for Proactive Documentation

### 1. **When Adding New Files or Folders**

Add a comment at the top of new files:
```
; TODO: Document this in README.md and CHANGELOG.md
; Add entry describing: [file purpose, location, and usage]
```

Ask Copilot: *"Update the README.md structure section to include this new folder/file"*

### 2. **When Modifying Printer Settings**

If you change temperature profiles or print settings:
```markdown
<!-- TODO: Update PRINTER_SPECS.md Material Profiles section -->
```

Ask Copilot: *"Update the material profile table for [material name] with new settings"*

### 3. **When Creating New Cura Profiles**

Document it immediately:
```
- Profile name: [New_Profile_Name]
- Best for: [Material/Use case]
- Temperature: [Nozzle/Bed temps]
```

Ask Copilot: *"Add this profile to PROFILES/README.md with setup instructions"*

### 4. **CHANGELOG Updates**

After committing changes, ask Copilot:
```
"Add an entry to CHANGELOG.md for:
- What changed: [description]
- Type of change: [Added/Changed/Fixed]
- File(s) affected: [list]"
```

## File Structure to Keep in Sync

```
MINDCUBBY-3D/
├── README.md ......................... Main overview (keep current)
├── CHANGELOG.md ...................... All version changes
├── DOCUMENTATION/
│   └── PRINTER_SPECS.md ............. Hardware & material specs
├── PROFILES/
│   ├── README.md .................... Profile usage guide
│   └── [Profile files]
└── GCODE/ ........................... Sliced print files
```

## Recommended Copilot Prompts

### General Documentation Update
> "Review the README.md and CHANGELOG.md. Suggest what documentation needs updating based on recent changes I've made to the repository."

### Consistency Check
> "Check if the printer specifications in PRINTER_SPECS.md match the settings used in the Cura profiles. List any discrepancies."

### New Feature Documentation
> "I've created a new [feature/file]. Generate documentation for it including: purpose, usage, and where to add it to the existing README files."

### Link Verification
> "Check all the links and file references in our markdown files to ensure they're accurate and up-to-date."

### Changelog Entry
> "Generate a CHANGELOG entry for the changes I just committed: [git commit message or description]"

## Documentation Maintenance Checklist

Use this before pushing to GitHub:

- [ ] All new files documented in README structure
- [ ] CHANGELOG.md updated with changes
- [ ] Cross-references between docs are accurate
- [ ] File paths in markdown are correct
- [ ] No broken links or references
- [ ] Material profiles/specs are current
- [ ] Profile README reflects actual files

## Tips

1. **Ask Copilot to be your documentation reviewer** - Use it to catch outdated info
2. **Keep descriptions brief but complete** - Future you will thank present you
3. **Update documentation BEFORE committing** - Makes commits cleaner
4. **Use consistent formatting** - Makes automated tools easier to parse
5. **Reference file paths explicitly** - Helps Copilot understand structure

## Example Workflow

1. Make changes to printer settings or create new profiles
2. Ask Copilot: "Update PRINTER_SPECS.md with these new temperatures"
3. Ask Copilot: "Generate a CHANGELOG entry for this change"
4. Ask Copilot: "Check that all README files are consistent"
5. Commit with clear message: `git commit -m "Update [feature]: [brief description]"`
6. Push: `git push`

---

**Last Updated**: 2025-11-09
