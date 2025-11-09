# Cura Profiles

Store your optimized Cura profiles here.

## Files

- `Ender3V2_Baseline_StartGCode.gcode` - Original baseline start G-code (reference/rollback)
- `Ender3V2_BLTouch_Optimized.txt` - Optimized start/end G-code with BLTouch support

## Baseline Reference

The baseline file preserves your original working G-code configuration. Use this for:
- Comparing with optimized versions
- Rolling back if new profiles don't work well
- Understanding what changed between versions

## How to Use in Cura

1. Open Cura
2. Go to **Preferences** → **Printers** → Select your printer
3. Click **Machine Settings**
4. Go to **G-code** tab
5. Copy content from files into appropriate fields:
   - **Start G-code**: Paste start section
   - **End G-code**: Paste end section
6. Click **Close** to save

## Creating New Profiles

Use the `Ender3V2_BLTouch_Optimized` as a base template for new material/quality profiles.

## Profile Versioning

When creating new profiles:
- Keep the baseline as reference
- Document changes in CHANGELOG.md
- Name profiles descriptively: `Ender3V2_[Material]_[Purpose].txt`
- Add comments describing key differences from baseline
