# Multi-Material Setup Guide for Cura

## Overview
v5.0 uses Cura's variable injection system to automatically adapt to whatever material profile you select. No manual edits needed.

## How It Works

### Cura Variables Used
```
{material_print_temperature}  → Gets nozzle temp from material profile
{material_bed_temperature}    → Gets bed temp from material profile
```

When you select a material in Cura, these values are **automatically replaced** with the correct temperatures before sending to printer.

## Setup Instructions

### Step 1: Create/Verify Material Profiles in Cura

In Cura, go to **Preferences → Materials**:

#### PLA Profile
- **Nozzle Temp**: 200°C (or 205-210°C if you prefer)
- **Bed Temp**: 60°C

#### PETG Profile  
- **Nozzle Temp**: 215-220°C (230-250°C if needed; lower temp = less stringing)
- **Bed Temp**: 70-75°C

#### TPU Profile
- **Nozzle Temp**: 220-230°C
- **Bed Temp**: 50°C

### Step 2: Use v5.0 as Start G-code

In your Cura printer profile:

1. Go to **Printer → Manage Printers**
2. Select your Ender-3 V2
3. Go to **Machine Settings**
4. Paste v5.0 into **Start G-code** field
5. **Do NOT modify** the {variables} - Cura will replace them

### Step 3: Switch Materials & Print

**To print with different material:**

1. In Cura, click **Material** dropdown
2. Select: PLA, PETG, or TPU
3. Cura automatically injects correct temps
4. Print → start G-code uses right temps automatically

No editing needed! Just select material and go.

## Verification

### Check if it's working:

1. Select **PLA** material in Cura
2. **Export G-code** to a file
3. Open file and look at first few lines:
   ```
   M104 S200   ; Should show PLA nozzle temp
   M190 S60    ; Should show PLA bed temp
   ```

4. Switch to **PETG**, export again:
   ```
   M104 S220   ; Should show PETG nozzle temp (or your adjusted value)
   M190 S70    ; Should show PETG bed temp
   ```

If temps match your material profiles = **working correctly!**

## Important Notes

- ⚠️ **Do NOT manually edit** {variables} in the start G-code
- ✅ **Material profiles must exist** in Cura (create them if missing)
- ✅ **Temps must be set correctly** in material settings
- ✅ **Always export & verify** before printing

## Temperature Tuning Tips

### Reducing Stringing (thin filament between moves):
- **Lower nozzle temp** by 2-5°C (reduces filament flow during travel)
- Example: PETG 220°C → try 215°C if stringing appears
- This is per-material, so adjust in your Material settings

### Reducing Blobs at Layer Seams:
- Enable **Coasting** in print profile (stops extruding early)
- Enable **Retraction Extra Prime** (compensates for pressure loss)
- Lower temp slightly (less ooze pressure)

## Other Useful Cura Variables

If you want to expand later:

```
{material_print_temperature}     ; Nozzle temp
{material_bed_temperature}       ; Bed temp
{material_flow}                  ; Flow rate percentage
{material_name}                  ; Material name (for logging)
```

## Troubleshooting

**Q: Variables not being replaced?**  
A: Check that Cura material profiles have temps set. Go to Preferences → Materials and verify.

**Q: Temps showing but wrong value (e.g., S23 instead of S220)?**  
A: Cura version issue. The start G-code v5.0 uses `{material_print_temperature}` which is stable across versions.

**Q: How to check Cura version?**  
A: Help → About Cura. Most modern versions (4.8+) support variable injection.

