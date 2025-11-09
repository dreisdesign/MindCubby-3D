# G-Code Optimization Changelog

## End G-Code

### v1.0 - Warm Hold for Quick Reprints (2025-11-09)
**Purpose**: Final retract, park, and warm standby for rapid iteration  
**Workflow**: Print finishes → 5-min hold at warm temps → Quick reprint or cool shutdown  
**Nozzle Standby**: 180°C (only ~60s to reach 220°C for reprint)  
**Bed Standby**: 70°C (close to material temps, minimal reheat needed)  
**Hold Duration**: 5 minutes (time to assess print quality and decide)

### Key Features:
- Retract 4mm total to prevent oozing
- Lift Z 10mm to clear print completely
- Park at front-left for easy print removal/assessment
- Keep warm but not active (ready for quick reheat)
- After 5 minutes, cool to off
- Z axis stays locked (holds position)

### Timeline:
```
Print finishes → Retract & lift → Park nozzle
↓
Nozzle: 180°C, Bed: 70°C (warm standby)
↓
5-minute hold (user decides: reprint or remove)
↓
If reprint: Select new profile/material, heat up (~60s to 220°C)
If done: Already cooled, remove print
```

---

## Start G-Code

## v5.0 - Universal Multi-Material Profile (2025-11-09)
**Issue**: Must manually edit G-code temps when switching between PLA/PETG/TPU  
**Solution**: Use Cura variable injection - single G-code for all materials  
**Expected Benefit**: Select material in Cura, temps auto-inject, zero manual edits  
**Materials Supported**: PLA, PETG, TPU (any Cura material profile)  
**Documentation**: See MULTI_MATERIAL_SETUP.md

### Key Implementation:
- `{material_print_temperature}` → Auto-replaced with full print nozzle temp from Cura material
- `{material_bed_temperature}` → Auto-replaced with bed temp from Cura material
- **Result**: One G-code file works for all materials
- **Cura Management**: After first layer, Cura automatically adjusts nozzle temp per profile settings

### Recent Updates:
- Fixed variable injection: Using `material_print_temperature` (stable) instead of `material_print_temperature_layer_0` (buggy in Cura 5.11.0)
- Improved nozzle wipe on bed edge to eliminate stringing from prime to start
- Retract → Lift → Wipe on edge → Lower to print position

### Setup Workflow:
1. Create/verify material profiles in Cura (Settings → Manage Materials)
2. Use v5.0 as Start G-code in printer settings
3. Select material in Cura before printing
4. Cura injects correct temps automatically
5. No manual editing ever needed

### How to Verify It's Working:
```
Export G-code → Open file → Check first 3 lines for correct temps
```

---

## v4.0 - Parallel Heating (2025-11-09)
**Issue**: Bed and nozzle heating sequentially wastes startup time  
**Solution**: Use M104 (non-blocking nozzle set) + M190 (blocking bed wait) for parallel heating  
**Expected Benefit**: ~2-3 minutes faster startup (bed and nozzle heat simultaneously)  
**Material**: PLA (Bed 60°C, Nozzle 200°C) - modify temps for other materials  
**Testing**: Required on physical printer

### Key Changes:
- M104 S200: Set nozzle to 200°C (starts immediately, non-blocking)
- M190 S60: Set bed to 60°C AND WAIT (nozzle heats while bed catches up)
- M109 S200: Wait for nozzle to reach 200°C (bed already hot by now)
- Added G29 for BLTouch auto-level (after homing)
- Result: Both heaters active simultaneously from start

### Heating Timeline:
```
Sequential (old):    |--Bed Heat--|--Nozzle Heat--|
Parallel (v4.0):     |--Bed Heat---|
                     |-Nozzle Heat-|
                     (overlapping)
```

---

## v3.0 - Nozzle Wipe & Blob Cleanup (2025-11-09)
**Issue**: Blob still appearing on first layer despite v2.0 clearance fix  
**Root Cause**: Nozzle dragging filament blob across bed from prime end (X0.4 Y20) to print start  
**Solution**: Added wipe sequence with retract + lift + travel pattern  
**Expected Benefit**: Clean nozzle, no blob on first layer  
**Testing**: Required on physical printer

### Changes:
- Wipe move: Travel from Y20 to Y5 (wiping across bed surface)
- Retract: -0.5mm before lifting to prevent oozing
- Lift sequence: Z0.3 → Z5.0 (clear bed before traveling)
- Travel: Move to X30 Y20 Z5.0 (away from prime lines)
- Approach: Lower Z back to Z0.3 for print start
- Result: Clean nozzle arrives at print position without dragging blob

---

## v2.0 - Blob Catch Fix (2025-11-09)
**Issue**: Priming blob caught by nozzle on second skirt pass  
**Root Cause**: Insufficient clearance between prime line end (X0.4) and safe position (X5)  
**Solution**: Move away to X30 instead of X5 before starting print  
**Status**: Superseded by v3.0

### Changes:
- Final safe position moved from X5 to X30 (25mm additional clearance)
- Z movement order optimized (move up before moving XY away)

---

## v1.0 - Improved Priming (2025-11-09)
**Issue**: Original alternating-direction priming left messy nozzle with excess filament  
**Solution**: Changed to 2 parallel lines in same Y direction for cleaner extrusion  
**Status**: Foundation for v2.0 and v3.0

### Changes:
- Prime line 1: Y direction (Y20→Y200)
- Prime line 2: Y direction same as line 1 (Y200→Y20)
- Parallel spacing: 0.3mm between lines

---

## Reference: Baseline (Original)
- File: `Ender3V2_Baseline_StartGCode.gcode`
- Use for comparison/rollback
- Archive: `Original_StartGCode_Archive.gcode`
