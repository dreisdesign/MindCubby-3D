# 🎯 Ender-3 V2 Optimization - Milestone 1

**Date**: 2025-11-09  
**Status**: PRODUCTION BASELINE ESTABLISHED  
**Tested On**: Ender-3 V2 with BLTouch, PETG material

---

## What's Complete

### ✅ Start G-Code (Optimized)
- **File**: `START_GCODE.txt` (clean baseline, no version numbers)
- **Features**:
  - Parallel heating (nozzle + bed simultaneously)
  - Universal multi-material support (auto-temp injection from Cura)
  - 2x parallel prime lines (same Y direction for cleaner nozzle)
  - Nozzle wipe on bed edge (eliminates stringing from prime)
  - BLTouch auto-leveling
  - Tested and verified working on Ender-3 V2

### ✅ End G-Code (Optimized)
- **File**: `END_GCODE.txt` (clean baseline)
- **Features**:
  - 4mm retraction (prevents oozing)
  - 10mm Z-lift (clears print safely)
  - Front-left park position (easy access)
  - 5-minute warm hold (180°C nozzle, 70°C bed)
  - Ready for quick reprint workflow
  - Manual cool shutdown after hold

### ✅ Material Profiles (Cura)
- **PLA**: 200°C nozzle, 60°C bed
- **PETG**: 215-220°C nozzle, 70°C bed (optimized for low stringing)
- **TPU**: 220-230°C nozzle, 50°C bed
- **Setup**: Preferences → Materials (create custom materials if needed)

### ✅ Print Profiles (Cura)
- **print-in-place**: Optimized for articulated parts
  - Retraction: 8mm at 50 mm/s
  - Coasting: Enabled (reduces seam blobs)
  - Extra Prime: Enabled (compensates pressure loss)
  - Z-Seam: Shortest

### ✅ Documentation
- **MULTI_MATERIAL_SETUP.md**: Complete Cura configuration guide
- **QUICK_REFERENCE.md**: Troubleshooting section with fixes
- **CURA_PROFILE_MANAGEMENT.md**: Best practices for profile organization

### ✅ Model Tracking
- **MODELS/README.md**: Library for tracking prints and results
- First model: CE3E3V2_01-chip_clip (PETG, print-in-place, tested)

---

## Archive

Old versions moved to `GCODE/_archive/`:
- `Optimized_StartGCode_v1.gcode` through `v5.gcode`
- `Optimized_EndGCode_v1.gcode`
- `Ender3V2_Baseline_StartGCode.gcode`
- `Ender3V2_BLTouch_Optimized.txt`
- `Original_StartGCode_Archive.gcode`

**Reference**: Keep these for comparison/rollback if needed. They show the optimization journey.

---

## Known Working

✅ **Start G-Code v5.0:**
- Parallel heating works
- Prime lines clean and effective
- Nozzle wipe on bed edge eliminates stringing
- Tested with PETG at 218°C
- Cura variable injection confirmed working

✅ **End G-Code v1.0:**
- 5-minute hold at warm temps works
- Nozzle parks safely at front-left
- Quick reprint workflow verified
- Manual cool shutdown ready

✅ **Material/Profile Integration:**
- Multi-material Cura setup working
- Linked materials properly inheriting temps
- Coasting reduces layer seams
- Extra prime prevents under-extrusion

---

## Next Steps / Future Optimization

### Print Quality Improvements
- [ ] Test lower PETG temp (215°C) for even less stringing
- [ ] Optimize first-layer height if needed
- [ ] Fine-tune coasting volume if seams still visible
- [ ] Test different infill patterns for specific models

### Model Library
- [ ] Add print results to MODELS/README.md
- [ ] Track success rate and issues per model
- [ ] Document which profile/material works best for each

### Additional Profiles (If Needed)
- [ ] Fast-draft profile (high speed, low quality)
- [ ] High-detail profile (slow, 0.1mm layers)
- [ ] Flexible parts profile (special settings for TPU)

### Repository Features (Optional)
- [ ] Export and version control Cura profile files
- [ ] Add test print checklist
- [ ] Create print troubleshooting flowchart

---

## Quick Copy-Paste

**To use these G-codes:**

1. **Start G-Code**: Copy content from `START_GCODE.txt`
   - Paste into: Cura → Printer → Machine Settings → Start G-Code
   
2. **End G-Code**: Copy content from `END_GCODE.txt`
   - Paste into: Cura → Printer → Machine Settings → End G-Code

3. **Test Print**: Use PETG material with print-in-place profile
   - Export G-code and verify temps are injected
   - Should show `M104 S220` (or your material temp)

---

## Tested Configuration

| Component | Setting | Status |
|-----------|---------|--------|
| **Printer** | Ender-3 V2 | ✅ Verified |
| **Hotend** | Creality MK8, 0.4mm | ✅ Working |
| **Bed** | Carborundum glass | ✅ Leveling good |
| **Leveling** | BLTouch auto-level | ✅ Functional |
| **Material** | PETG (215-220°C) | ✅ Optimized |
| **Start G-Code** | v5.0 with edge wipe | ✅ Production |
| **End G-Code** | v1.0 with warm hold | ✅ Production |
| **Cura Version** | 5.11.0 | ✅ Compatible |

---

## Summary

**Milestone 1 Complete**: Production-ready start/end G-codes, multi-material Cura setup, and optimized profiles are **established and tested**. Repository is now at a clean baseline for ongoing optimization and model printing.

**Next**: Print models, track results, and iterate on specific use-case profiles as needed.

---

*Created during intensive optimization session on 2025-11-09*  
*Focus: Ender-3 V2 with BLTouch, multi-material support (PLA/PETG/TPU)*
