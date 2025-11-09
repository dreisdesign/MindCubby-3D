# 3D Model Library & Print Tracking

## Overview
Central repository for tracking all models, their specifications, materials, and print results.

---

## Models

### CE3E3V2_01-chip_clip--print_in_place
- **Description**: Print-in-place chip bag clip (movable hinge)
- **Material**: PETG
- **Filament Used**: 0.89m (~0.9g)
- **Print Time**: ~20 minutes (1187 seconds)
- **Layer Height**: 0.2mm (standard quality)
- **Build Area Used**: X 71-149mm, Y 57-163mm
- **Model Height**: 5.8mm
- **Start G-code**: v5.0 (Cura variables)
- **Hotend Temp**: 220°C
- **Bed Temp**: 70°C
- **Status**: Ready to print
- **Notes**: Thin flexible part - PETG chosen for durability and flexibility
- **Date Added**: 2025-11-09

---

## Print History Template

When you print a model, add results here:

```
### [Model Name] - Print #X
- **Date**: YYYY-MM-DD
- **Material**: [PLA/PETG/TPU]
- **Result**: [Success/Failed - reason]
- **Issues**: [Any problems encountered]
- **Quality**: [Visual assessment - 1-5 stars]
- **Notes**: [What worked, what didn't]
```

**Example:**
```
### CE3E3V2_01-chip_clip--print_in_place - Print #1
- **Date**: 2025-11-09
- **Material**: PETG
- **Result**: Success
- **Issues**: None
- **Quality**: ⭐⭐⭐⭐⭐ (5/5)
- **Notes**: Clean first layer, no blob, clip moves smoothly
```

---

## Quick Reference: Material Selection

| Material | Best For | Nozzle Temp | Bed Temp | Speed |
|----------|----------|-------------|----------|-------|
| **PLA** | Prototypes, decorative | 200°C | 60°C | 40-60 mm/s |
| **PETG** | Flexible, durable | 220-240°C | 70-75°C | 30-50 mm/s |
| **TPU** | Soft, stretchy parts | 230°C | 50°C | 20-30 mm/s |

---

## File Organization

```
MODELS/
├── README.md (this file)
├── CE3E3V2_01-chip_clip--print_in_place.gcode
├── [Future models...]
└── _archive/
    └── [Previous versions/failed prints]
```

---

## Tips for Model Tracking

1. **Before Printing**: Check this README for that model's specs and history
2. **During Printing**: Monitor first layer, watch for blob issues
3. **After Printing**: Add result to Print History section with date and notes
4. **Problem Solving**: Use print history to see what worked/failed in past attempts

---

## Stats at a Glance

| Stat | Value |
|------|-------|
| Total Models | 1 |
| Total Prints | 0 (ready to test) |
| Success Rate | N/A |
| Avg Print Time | ~20 min |
| Most Used Material | PETG |

*(Update as you print more)*

