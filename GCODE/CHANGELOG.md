# G-Code Optimization Changelog

## v2.0 - Blob Catch Fix (2025-11-09)
**Issue**: Priming blob caught by nozzle on second skirt pass  
**Root Cause**: Insufficient clearance between prime line end (X0.4) and safe position (X5)  
**Solution**: Move away to X30 instead of X5 before starting print  
**Expected Benefit**: Clean skirt without nozzle collision  
**Testing**: Required on physical printer

### Changes:
- Final safe position moved from X5 to X30 (25mm additional clearance)
- Z movement order optimized (move up before moving XY away)
- Comments clarified for future debugging

---

## v1.0 - Improved Priming (2025-11-09)
**Issue**: Original alternating-direction priming left messy nozzle with excess filament  
**Solution**: Changed to 2 parallel lines in same Y direction for cleaner extrusion  
**Expected Benefit**: Cleaner nozzle appearance at print start  
**Status**: Active (predecessor to v2.0)

### Changes:
- Prime line 1: Y direction (Y20→Y200)
- Prime line 2: Y direction same as line 1 (Y200→Y20)
- Parallel spacing: 0.3mm between lines

---

## Reference: Baseline (Original)
- File: `Ender3V2_Baseline_StartGCode.gcode`
- Use for comparison/rollback
- Archive: `Original_StartGCode_Archive.gcode`
