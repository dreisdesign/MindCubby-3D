# GitHub Copilot Agent Mode Guide

This guide explains how to use GitHub Copilot Agent Mode to intelligently manage and update your 3D printing repository.

## What is Agent Mode?

Agent Mode allows Copilot to take autonomous actions in your editor to help maintain documentation, update files, and manage your repository more efficiently. It can:

- Automatically update CHANGELOG.md when you make changes
- Sync documentation across multiple README files
- Suggest and implement file structure improvements
- Generate and update documentation based on your actions
- Manage version numbers and release notes

## Enabling Agent Mode

In VS Code with GitHub Copilot:
1. Open the Copilot Chat panel (Cmd+Shift+I on macOS)
2. Look for the "Agent Mode" toggle in chat settings
3. Enable it to allow Copilot to make file edits autonomously

## How to Use Agent Mode in This Repository

### 1. **Automatic Documentation Updates**

After making changes to printer settings or creating new profiles, use Agent Mode:

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

### 2. **Profile Management**

When adding a new Cura profile:

```
"I've created a new profile: [profile name].
- Update PROFILES/README.md
- Add entry to DOCUMENTATION/PRINTER_SPECS.md
- Update main README.md structure
- Create CHANGELOG entry"
```

### 3. **Documentation Consistency Checks**

Periodically ask:

```
"Scan the entire MINDCUBBY-3D repository and identify any documentation inconsistencies:
- Outdated references
- Missing links
- Files not documented
- Suggestions for improvements"
```

### 4. **GCODE Profile Validation**

When optimizing G-code:

```
"Analyze the GCODE files in PROFILES/ and document:
- Temperature differences from baseline
- Speed optimizations
- Special features or considerations
- When each profile should be used"
```

## Agent Mode Commands for This Repo

### Update Everything After Major Changes
```
"I've made significant changes to [describe changes].
Update all documentation:
1. README.md - update structure/description
2. CHANGELOG.md - create version entry
3. PRINTER_SPECS.md - update specifications
4. PROFILES/README.md - update profile list
5. Verify all cross-references"
```

### Sync Across Documentation
```
"Ensure all README files are in sync:
- Check README.md references DOCUMENTATION/ and PROFILES/ correctly
- Verify PROFILES/README.md matches actual files
- Confirm PRINTER_SPECS.md material profiles are current
- Create summary of any discrepancies"
```

### Generate Release Notes
```
"Generate release notes for version X.X.X based on CHANGELOG.md entries for [date range]"
```

### Profile Comparison
```
"Compare all profiles in PROFILES/ directory:
- List key differences
- Identify overlaps or duplicates
- Suggest optimizations
- Document findings in PROFILES/README.md"
```

## Best Practices with Agent Mode

1. **Review Changes** - Always review Copilot's edits before committing
2. **Clear Instructions** - Be specific about what you want updated
3. **Regular Syncs** - Use Agent Mode weekly to catch documentation drift
4. **Version Control** - Commit frequently so you can revert if needed
5. **Backup First** - Keep local backups of important docs before major updates

## Workflow Example with Agent Mode

1. **Make Changes** - Update printer settings or create new profile
2. **Use Agent Mode**: 
   ```
   "I've updated the nozzle temperature for PLA from 210°C to 215°C.
   Update all documentation and CHANGELOG"
   ```
3. **Review** - Check what Copilot changed
4. **Commit**: `git commit -m "Update: PLA nozzle temperature optimization"`
5. **Push**: `git push`

## Safety Tips

- **Use `--amend` if needed**: If Copilot makes an error, you can fix and amend the commit
- **Branch for experiments**: Try Agent Mode on a test branch first
- **Manual verification**: Don't blindly accept all changes - verify accuracy
- **Lock important files**: Consider protecting critical files like PRINTER_SPECS.md

## Disabling Agent Mode

If you want more control over changes:
- Toggle off Agent Mode in chat settings
- Use regular chat mode for suggestions without auto-edits
- Manually implement changes yourself

---

**Last Updated**: 2025-11-09

**See Also**: [COPILOT_DOCUMENTATION_GUIDE.md](COPILOT_DOCUMENTATION_GUIDE.md) - General documentation maintenance guide
