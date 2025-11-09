# GitHub Copilot Guide

Comprehensive guide for using GitHub Copilot to maintain and optimize your 3D printing repository.

## Overview

GitHub Copilot helps maintain accurate documentation and manage your repository efficiently. This guide covers:
- **Documentation Maintenance** - Keep docs in sync with changes
- **Agent Mode** - Autonomous repository management
- **Best Practices** - Workflows and safety tips

Documentation is kept in these locations:
- `README.md` - Main repository overview
- `DOCUMENTATION/PRINTER_SPECS.md` - Printer specifications and materials
- `PROFILES/README.md` - Cura profile usage instructions
- `CHANGELOG.md` - Version history and changes

---

## Getting Started with Copilot

### Installation & Setup

1. Install **GitHub Copilot** extension in VS Code
2. Sign in with GitHub account
3. Open **Copilot Chat** (Cmd+Shift+I on macOS)
4. Test with: `"Help me understand this code"`

### Understanding Copilot Modes

**Regular Chat Mode**:
- Ask questions and get suggestions
- No automatic file editing
- Safe for exploring ideas

**Agent Mode** (Premium):
- Copilot makes autonomous edits
- Updates files automatically
- Requires review before commit

---

## Documentation Maintenance with Copilot

### Proactive Documentation Updates

When you make changes to your printer or profiles:

#### 1. **When Adding New Files or Folders**

Add a comment at the top of new files:
```
; TODO: Document this in README.md and CHANGELOG.md
; Add entry describing: [file purpose, location, and usage]
```

Ask Copilot: 
> *"Update the README.md structure section to include this new folder/file"*

#### 2. **When Modifying Printer Settings**

If you change temperature profiles or print settings:
```markdown
<!-- TODO: Update PRINTER_SPECS.md Material Profiles section -->
```

Ask Copilot: 
> *"Update the material profile table for [material name] with new settings"*

#### 3. **When Creating New Cura Profiles**

Document immediately:
```
- Profile name: [New_Profile_Name]
- Best for: [Material/Use case]
- Temperature: [Nozzle/Bed temps]
```

Ask Copilot: 
> *"Add this profile to PROFILES/README.md with setup instructions"*

#### 4. **CHANGELOG Updates**

After committing changes:
```
"Add an entry to CHANGELOG.md for:
- What changed: [description]
- Type of change: [Added/Changed/Fixed]
- File(s) affected: [list]"
```

---

## Recommended Copilot Prompts

### General Documentation Review
```
"Review the README.md and CHANGELOG.md. Suggest what documentation 
needs updating based on recent changes I've made to the repository."
```

### Consistency Check
```
"Check if the printer specifications in PRINTER_SPECS.md match the 
settings used in the Cura profiles. List any discrepancies."
```

### New Feature Documentation
```
"I've created a new [feature/file]. Generate documentation for it 
including: purpose, usage, and where to add it to the existing README files."
```

### Link Verification
```
"Check all the links and file references in our markdown files 
to ensure they're accurate and up-to-date."
```

### Changelog Generation
```
"Generate a CHANGELOG entry for the changes I just committed: [git message]"
```

---

## Agent Mode: Autonomous Repository Management

### What is Agent Mode?

Agent Mode allows Copilot to take autonomous actions to help maintain your repository:
- Automatically update CHANGELOG.md when changes are made
- Sync documentation across multiple README files
- Suggest and implement file structure improvements
- Generate and update documentation based on your actions
- Manage version numbers and release notes

### Enabling Agent Mode

In VS Code with GitHub Copilot:
1. Open the **Copilot Chat** panel (Cmd+Shift+I on macOS)
2. Look for the **"Agent Mode"** toggle in chat settings
3. Enable it to allow Copilot to make file edits autonomously

### How to Use Agent Mode

#### 1. **Automatic Documentation Updates**

After making changes to printer settings or profiles:

```
"Update the repository documentation to reflect these changes:
- What was modified
- Where it should be documented
- Update CHANGELOG.md accordingly"
```

Copilot will:
- Analyze your changes
- Update relevant README files
- Create CHANGELOG entry
- Update cross-references

#### 2. **Profile Management**

When adding a new Cura profile:

```
"I've created a new profile: [profile name].
- Update PROFILES/README.md
- Add entry to DOCUMENTATION/PRINTER_SPECS.md
- Update main README.md structure
- Create CHANGELOG entry"
```

#### 3. **Documentation Consistency Checks**

Periodically ask:

```
"Scan the entire MINDCUBBY-3D repository and identify any 
documentation inconsistencies:
- Outdated references
- Missing links
- Files not documented
- Suggestions for improvements"
```

#### 4. **GCODE Profile Validation**

When optimizing G-code:

```
"Analyze the GCODE files in PROFILES/ and document:
- Temperature differences from baseline
- Speed optimizations
- Special features or considerations
- When each profile should be used"
```

### Agent Mode Commands for Common Tasks

#### Update Everything After Major Changes
```
"I've made significant changes to [describe changes].
Update all documentation:
1. README.md - update structure/description
2. CHANGELOG.md - create version entry
3. PRINTER_SPECS.md - update specifications
4. PROFILES/README.md - update profile list
5. Verify all cross-references"
```

#### Sync Across All Documentation
```
"Ensure all README files are in sync:
- Check README.md references DOCUMENTATION/ and PROFILES/ correctly
- Verify PROFILES/README.md matches actual files
- Confirm PRINTER_SPECS.md material profiles are current
- Create summary of any discrepancies"
```

#### Generate Release Notes
```
"Generate release notes for version X.X.X based on 
CHANGELOG.md entries for [date range]"
```

#### Compare and Document Profiles
```
"Compare all profiles in PROFILES/ directory:
- List key differences
- Identify overlaps or duplicates
- Suggest optimizations
- Document findings in PROFILES/README.md"
```

---

## Best Practices & Workflow

### Documentation Maintenance Checklist

Use this before pushing to GitHub:

- [ ] All new files documented in README structure
- [ ] CHANGELOG.md updated with changes
- [ ] Cross-references between docs are accurate
- [ ] File paths in markdown are correct
- [ ] No broken links or references
- [ ] Material profiles/specs are current
- [ ] Profile README reflects actual files

### Recommended Workflow

1. **Make Changes** - Update printer settings or create new profile
2. **Use Copilot Chat**: 
   ```
   "I've updated the nozzle temperature for PLA from 210°C to 215°C.
   Update all documentation and CHANGELOG"
   ```
3. **Review** - Check what Copilot changed
4. **Commit**: `git commit -m "Update: PLA nozzle temperature optimization"`
5. **Push**: `git push`

### Best Practices

1. **Review Changes** - Always review Copilot's edits before committing
2. **Clear Instructions** - Be specific about what you want updated
3. **Regular Syncs** - Use Copilot weekly to catch documentation drift
4. **Version Control** - Commit frequently so you can revert if needed
5. **Backup First** - Keep local backups of important docs before major updates
6. **Ask Copilot to be your reviewer** - Use it to catch outdated info
7. **Keep descriptions brief but complete** - Future you will thank present you
8. **Update documentation BEFORE committing** - Makes commits cleaner
9. **Use consistent formatting** - Makes automated tools easier to parse
10. **Reference file paths explicitly** - Helps Copilot understand structure

---

## Safety & Control

### Safety Tips

- **Use `--amend` if needed**: If Copilot makes an error, fix and amend the commit
- **Branch for experiments**: Try Agent Mode on a test branch first
- **Manual verification**: Don't blindly accept all changes - verify accuracy
- **Lock important files**: Consider protecting critical files like PRINTER_SPECS.md
- **Document assumptions**: Tell Copilot what should NOT change

### Disabling Agent Mode

If you want more control over changes:
- Toggle off Agent Mode in chat settings
- Use regular chat mode for suggestions without auto-edits
- Manually implement changes yourself

---

## File Structure to Keep in Sync

```
MINDCUBBY-3D/
├── README.md ......................... Main overview (keep current)
├── CHANGELOG.md ...................... All version changes
├── DOCUMENTATION/
│   ├── PRINTER_SPECS.md ............. Hardware & material specs
│   └── [Other documentation]
├── PROFILES/
│   ├── README.md .................... Profile usage guide
│   └── [Profile files]
└── GCODE/ ........................... Sliced print files
```

---

## Quick Reference: Common Prompts by Task

### Profile Management
```
"I've optimized the [material] profile. Document:
1. What changed from baseline
2. When to use this profile
3. Expected print quality
4. Update CHANGELOG"
```

### Troubleshooting
```
"I've fixed a [issue]. Document:
1. What the problem was
2. How it was solved
3. Prevention tips
4. Add to TROUBLESHOOTING.md"
```

### Version Management
```
"Update VERSION.md with current firmware and settings.
Generate a summary of all changes since last update."
```

### Validation
```
"Validate the repository:
1. Check all links are correct
2. Verify file references are accurate
3. Ensure consistent naming
4. Flag any issues"
```

---

## Troubleshooting Copilot Issues

### If Copilot makes incorrect edits:
1. Review the changes carefully
2. Fix manually if needed
3. Commit as normal (or use `--amend`)
4. Provide feedback to improve future suggestions

### If Copilot doesn't understand context:
1. Provide more specific file references
2. Include examples of what you want
3. Ask it to reference specific sections
4. Break complex requests into smaller parts

### If documentation gets out of sync:
1. Ask: "Review all documentation and identify inconsistencies"
2. Let Copilot suggest fixes
3. Review and approve changes
4. Commit with clear message

---

## Tips for Best Results

1. **Be Specific** - Tell Copilot exactly which files to update
2. **Provide Context** - Explain why changes matter
3. **Give Examples** - Show format/style you want
4. **Ask for Validation** - Have Copilot verify its own work
5. **Iterate** - Ask follow-up questions to refine suggestions

---

## Summary

Using GitHub Copilot effectively:

✅ **Automates** repetitive documentation tasks  
✅ **Maintains** consistency across files  
✅ **Catches** outdated information  
✅ **Suggests** improvements proactively  
✅ **Saves** time on maintenance  

**Key Remember**: Always review before committing - Copilot is a helper, not a replacement for your judgment!

---

**Last Updated**: 2025-11-09  
**Related**: [MARKDOWN_CONSOLIDATION.md](../MARKDOWN_CONSOLIDATION.md)
