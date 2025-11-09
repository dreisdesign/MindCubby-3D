# G-Code Optimization Changelog

Track all optimizations and improvements to start/end G-code sequences.

## Versions

### v1.0 - 2025-11-09: Improved Priming Sequence

**File**: `Optimized_StartGCode_v1.gcode`

**Changes from baseline:**
- **Priming improvement**: Changed from alternating directions to 2 parallel lines in same direction (Y-axis)
- **Benefit**: Cleaner nozzle appearance at start of print, less messy primer lines
- **Speed**: Maintained (1500mm/s for priming, 5000mm/s for travel)
- **Extrusion**: Same (15mm per line, 30mm total)

**Comparison to Original:**
```
ORIGINAL:
Line 1: X0.1 → Y20 to Y200 (extrude 15mm)
Line 2: X0.4 → Y200 to Y20 (extrude 15mm) ← REVERSE direction

OPTIMIZED v1:
Line 1: X0.1 → Y20 to Y200 (extrude 15mm)
Line 2: X0.4 → Y20 to Y200 (extrude 15mm) ← SAME direction
```

**Testing Status**: Ready for testing

---

## Template for Future Versions

### v[X.X] - YYYY-MM-DD: [Feature Description]

**File**: `Optimized_StartGCode_v[X.X].gcode`

**Changes from previous:**
- Feature/improvement
- Benefit
- Speed/extrusion changes

**Testing Status**: In progress / Ready / Approved

---

**Last Updated**: 2025-11-09
