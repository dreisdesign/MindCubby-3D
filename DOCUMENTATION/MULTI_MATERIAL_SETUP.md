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

In Cura, go to **Settings → Manage Materials**:

#### PLA Profile
- **Nozzle Temp**: 200°C (or 205-210°C if you prefer)
- **Bed Temp**: 60°C

#### PETG Profile  
- **Nozzle Temp**: 240°C (range 230-250°C)
- **Bed Temp**: 75°C (range 70-80°C)

#### TPU Profile
- **Nozzle Temp**: 230°C (range 220-240°C)
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
   M104 S240   ; Should show PETG nozzle temp
   M190 S75    ; Should show PETG bed temp
   ```

If temps match your material profiles = **working correctly!**

## Important Notes

- ⚠️ **Do NOT manually edit** {variables} in the start G-code
- ✅ **Material profiles must exist** in Cura (create them if missing)
- ✅ **Temps must be set correctly** in material settings
- ✅ **Always export & verify** before printing

## Other Useful Cura Variables

If you want to expand later:

```
{material_print_temperature}     ; Nozzle temp
{material_bed_temperature}       ; Bed temp
{material_print_temperature_layer_0}  ; First layer nozzle temp (if different)
{material_bed_temperature_layer_0}    ; First layer bed temp (if different)
{material_flow}                  ; Flow rate percentage
{material_name}                  ; Material name (for logging)
```

## Troubleshooting

**Q: Variables not being replaced?**  
A: Check that Cura material profiles have temps set. Go to Manage Materials and verify.

**Q: Want different temps for first layer only?**  
A: Replace with `{material_print_temperature_layer_0}` for first-layer-specific temps (if Cura supports in your version).

**Q: How to check Cura version?**  
A: Help → About Cura. Most modern versions (4.8+) support variable injection.

