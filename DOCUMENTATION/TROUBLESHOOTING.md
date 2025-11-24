# 3D Printer Troubleshooting Guide

## Z-Axis Binding & Elephant's Foot (November 2025)

### Issue
Persistent elephant's foot on symmetrical tube print, which was not resolved by:
- Increasing Z-Offset
- Using negative Initial Layer Horizontal Expansion in Cura

### Symptom Diagnosis
Manual testing revealed the X-gantry would momentarily drop when near the bed after moving the Z-axis, indicating excessive **Z-Axis Binding (friction)** at low Z-heights.

### Root Cause
The two screws holding the Brass Z-Axis Lead Screw Nut to the X-gantry bracket were overtightened or slightly misaligned, forcing the vertical lead screw into a high-friction position. This caused the Z-motor to miss small movements near the bed, resulting in squished first layers.

### Solution

1. **Loosened** the two small screws holding the Z-Axis Lead Screw Nut (on the left vertical gantry)
2. **Allowed** the nut to self-align with the lead screw, releasing the binding tension
3. **Gently re-tightened** the screws to hold the nut in place while allowing a slight degree of "float"

### Result
✅ Z-axis binding was eliminated, allowing precise vertical movement for all layers
✅ Elephant's foot resolved
✅ Symmetrical tube now prints dimensionally accurate from the first layer

### Next Steps
Now that geometry is accurate, you can fine-tune the fit using **Hole Horizontal Expansion** in Cura (for internal diameters) if you need specific clearance/tolerance.

---

## Future Troubleshooting

Document additional issues and solutions here as they arise.
