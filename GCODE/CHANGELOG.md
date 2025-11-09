# G-Code Optimization Changelog

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
