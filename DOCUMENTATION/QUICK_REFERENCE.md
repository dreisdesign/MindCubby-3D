# Quick Reference Guide

Fast lookup for common tasks, checklists, and keyboard shortcuts.

## 🚀 Quick Start Tasks

### Load a Cura Profile
1. Open Cura
2. **Preferences** → **Printers** → Select your printer
3. Click **Machine Settings**
4. Go to **G-code** tab
5. Copy from `PROFILES/Ender3V2_BLTouch_Optimized.txt`
6. Paste into **Start G-code** and **End G-code** fields
7. Click **Close**

### Switch Materials

#### PLA
- **Profile**: Ender3V2_BLTouch_Optimized.txt
- **Bed Temp**: 60°C
- **Nozzle Temp**: 200-210°C
- **Print Speed**: 40-60 mm/s
- **Fan**: 100% after first layer

#### PETG
- **Bed Temp**: 70-80°C
- **Nozzle Temp**: 230-250°C
- **Print Speed**: 30-50 mm/s
- **Fan**: 50% (avoid cooling)

#### TPU/Flexible
- **Bed Temp**: 50°C
- **Nozzle Temp**: 220-240°C
- **Print Speed**: 20-30 mm/s
- **Fan**: 0-25%

### Clean Bed
1. Remove print
2. Let bed cool slightly
3. Use IPA (Isopropyl Alcohol) on cloth
4. Wipe entire bed surface
5. Let dry completely

### Check Bed Leveling
1. Home printer: `G28`
2. Run auto-level: `G29`
3. Check first layer height
4. If needed, adjust BLTouch offset

---

## 🔧 Troubleshooting & Fixes

### Stringing (Thin Filament Between Moves)
**Symptom**: Thin strings or webbing connecting different parts of print

**Quick Fixes (try in order):**
1. **Lower nozzle temp** by 2-5°C (e.g., PETG 220°C → 215°C)
   - Reduces filament flow during travel
   - Set in Cura Material settings
2. **Increase retraction speed** (if not already done)
   - Material → Retraction Speed: 50 → 60-65 mm/s
3. **Enable coasting** (if still present)
   - In print profile: Coasting → Enable
   - Stops extruding early, coast on pressure

### Blobs at Layer Seams
**Symptom**: Visible bump where each layer starts/ends

**Quick Fixes:**
1. **Enable coasting** in print profile
2. **Add retraction extra prime** (compensate for pressure loss)
3. **Lower nozzle temp** by 3-5°C
4. **Z-Seam**: Already set to "Shortest" (good for hiding)

### First Layer Issues
**Symptom**: Poor adhesion, gaps, or uneven extrusion on first layer

**Quick Fixes:**
1. **Check bed level**: Run `G29` (BLTouch auto-level)
2. **Clean bed** with IPA (removes oils/residue)
3. **Check nozzle distance**: Should be paper-thin height
4. **Verify first-layer temp**: Usually 5°C lower than normal

### Active start G-code & archived baseline

The repository's active start G-code is `CURA-SETTINGS/active/START_GCODE.txt` (this is the version currently tested and confirmed working). The original baseline start G-code has been archived to `CURA-SETTINGS/archived/Ender3V2_Baseline_StartGCode.gcode` to avoid accidental use while preserving it for rollback and comparison.

If you switch start G-codes, always re-run a skirt test to validate first-layer adhesion and that your saved BLTouch mesh (if used) is enabled before skirt moves.

### Recent change — off-print purge to prevent nozzle blobs (2025-11-11)

The active `START_GCODE.txt` was updated to perform priming off the model area (corner/back-edge purge) and to include a retract → lift → wipe → micro-prime sequence. This prevents the nozzle from collecting filament blobs on the purge line and dragging them across the first layer.

Quick verification steps after pulling the repo or updating your Machine Settings:
1. Confirm the start G-code in Cura is `CURA-SETTINGS/active/START_GCODE.txt`.
2. Slice a small test (20×20 mm square) with 3 skirt lines and skirt distance 7–10 mm so the skirt doesn't intersect the purge corner.
3. Export and open the G-code: ensure `M420 S1` appears before `;TYPE:SKIRT` and that the purge lines are at the bed edge (look for X10..X150 / Y200..Y205). Run the print and verify the purge/wipe happens off-print and the first skirt passes cleanly.

If you still see oozing, try raising the purge Z slightly (0.35–0.40 mm), increase retract to 2.0 mm, or increase retract speed in Cura (45–60 mm/s). Avoid committing personal `M851` values — keep offsets in EEPROM only.

### Nozzle Oozing During Print
**Symptom**: Drips or blobs falling from nozzle

**Quick Fixes:**
1. **Increase retraction** (8mm is good for PETG)
2. **Increase retraction speed** (45-50 mm/s minimum)
3. **Lower nozzle temp** (less fluid filament = less ooze)
4. **Enable coasting** (stops extruding early)

## 📋 Pre-Print Checklist

- [ ] Bed is clean (IPA wipe)
- [ ] Nozzle is clean (no residue)
- [ ] Filament is loaded
- [ ] Correct material profile selected
- [ ] Bed temperature matches material
- [ ] Nozzle temperature matches material
- [ ] Bed leveling recent (within week)
- [ ] BLTouch sensor working
- [ ] Print file is sliced correctly
- [ ] Estimated time is reasonable

---

## 📋 Post-Print Checklist

- [ ] Remove print carefully
- [ ] Turn off heaters (M104 S0, M140 S0)
- [ ] Clean bed with IPA
- [ ] Remove any residue from nozzle
- [ ] Check print quality
- [ ] Document results in CHANGELOG if notable

---

## 🛠️ Common Commands

### G-Code Commands

| Command | Description | Example |
|---------|-------------|---------|
| `G28` | Home all axes | `G28` |
| `G29` | Auto bed leveling | `G29` |
| `M104 S[temp]` | Set nozzle temp (no wait) | `M104 S210` |
| `M109 S[temp]` | Set nozzle temp (wait) | `M109 S210` |
| `M140 S[temp]` | Set bed temp (no wait) | `M140 S60` |
| `M190 S[temp]` | Set bed temp (wait) | `M190 S60` |
| `M106 S[speed]` | Set fan speed (0-255) | `M106 S255` |
| `M107` | Turn off fan | `M107` |
| `M84` | Disable steppers | `M84` |
| `G1 X Y Z F[speed]` | Move to position | `G1 X10 Y10 Z5 F3000` |

### Git Commands

| Command | Description |
|---------|-------------|
| `git status` | Check repo status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit changes |
| `git push` | Push to GitHub |
| `git pull` | Pull from GitHub |
| `git log --oneline` | View commit history |

---

## 🔧 Troubleshooting Quick Fixes

### First Layer Problems

**Issue**: First layer not sticking  
**Quick Fix**:
1. Check bed leveling (`G29`)
2. Increase bed temp +5°C
3. Clean bed with IPA
4. Check nozzle height

**Issue**: First layer too squished  
**Quick Fix**:
1. Raise Z-offset in Cura
2. Check bed leveling
3. Verify nozzle isn't too close

### BLTouch Issues

**Issue**: BLTouch not responding  
**Quick Fix**:
1. Check sensor cable connection
2. Run `G29` to test
3. Restart printer

**Issue**: Inconsistent leveling  
**Quick Fix**:
1. Run `G29` twice
2. Check bed surface for debris
3. Verify sensor is clean

### BLTouch: saved mesh & Z-offset (MRISCOC)

If you have a saved mesh (for example: `MRISCOC`) and a BLTouch probe, enable the mesh before the priming/skirt moves so the skirt and first layer use the same compensated height.

Quick enable (fast; recommended if you already saved a mesh):
1. Home: `G28`
2. Enable saved mesh: `M420 S1`  ; applies mesh compensation from EEPROM

Example (quick terminal sequence to validate):
```
G28
M420 S1
G1 Z2.0 F3000
G1 X110 Y20 Z0.15 F5000 ; move to prime start position used by Optimized_StartGCode_v6.gcode
```

Measure and save a persistent probe offset (only after confirming with paper test):
1. Home: `G28`
2. Move nozzle to center and lower slowly until paper drag is correct
3. Set probe offset (replace -1.28 with your measured value):
   `M851 Z-1.28`
4. Save to EEPROM: `M500`

Notes & safety:
- `M420 S1` only enables a saved mesh; it does not change offsets by itself.  
- If you prefer re-probing every print, replace `M420 S1` with `G29` (takes longer).  
- Avoid committing personal `M851` values to the repo — keep offsets local and save to EEPROM instead.  
- `G92` can be used as a per-print temporary coordinate shift but use with caution (non-persistent).

See `CURA-SETTINGS/variants/Optimized_StartGCode_v6.gcode` — this start G-code enables a saved mesh (`M420 S1`) and uses a lowered Z for skirt/priming to improve first-layer adhesion for many setups.

### Nozzle Problems

**Issue**: Nozzle clogged  
**Quick Fix**:
1. Heat to 235°C
2. Use needle to clear gently
3. Or do cold pull

**Issue**: Filament not extruding  
**Quick Fix**:
1. Check filament loaded
2. Increase temp +10°C
3. Check for clog

---

## 📁 File Locations

| What | Where |
|------|-------|
| G-code profiles | `PROFILES/` |
| Baseline reference | `PROFILES/Ender3V2_Baseline_StartGCode.gcode` |
| Printer specs | `DOCUMENTATION/PRINTER_SPECS.md` |
| This guide | `DOCUMENTATION/QUICK_REFERENCE.md` |
| Full Copilot guide | `DOCUMENTATION/COPILOT_GUIDE.md` |
| Version history | `CHANGELOG.md` |
| Main overview | `README.md` |

---

## ⚙️ Keyboard Shortcuts (VS Code)

| Action | Mac | Windows |
|--------|-----|---------|
| Copilot Chat | Cmd+Shift+I | Ctrl+Shift+I |
| Command Palette | Cmd+Shift+P | Ctrl+Shift+P |
| Search files | Cmd+P | Ctrl+P |
| Find in file | Cmd+F | Ctrl+F |
| Terminal | Ctrl+` | Ctrl+` |
| New file | Cmd+N | Ctrl+N |

---

## 📞 Quick Contact Info

**Repository**: https://github.com/dreisdesign/MindCubby-3D  
**Printer**: Creality Ender-3 V2  
**Nozzle**: 0.4mm  
**Bed**: 220x220mm  

---

## 💡 Pro Tips

1. **Baseline Comparison** - Always compare against `Ender3V2_Baseline_StartGCode.gcode`
2. **Document Changes** - Update CHANGELOG.md immediately after changes
3. **Test New Profiles** - Use small test print before large project
4. **Track Success** - Note what worked well for future reference
5. **Regular Maintenance** - Monthly: check bed level, clean nozzle, inspect BLTouch
6. **Use Copilot** - Ask Copilot to review documentation monthly

---

## 📊 Temperature Reference Table

| Material | Nozzle Temp | Bed Temp | Speed | Fan | Notes |
|----------|-------------|----------|-------|-----|-------|
| **PLA** | 200-210°C | 60°C | 50 mm/s | 100% | Standard, beginner friendly |
| **PETG** | 230-250°C | 70-80°C | 40 mm/s | 50% | Stronger, needs care |
| **TPU** | 220-240°C | 50°C | 25 mm/s | 25% | Very slow, flexible |
| **Nylon** | 250-260°C | 85°C | 30 mm/s | 0% | Strong, experimental |

---

**Last Updated**: 2025-11-09  
**Quick Feedback**: Having trouble? Check DOCUMENTATION/TROUBLESHOOTING.md for detailed solutions.
