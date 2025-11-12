# MindCubby Setup Guide

Complete printer configuration, material settings, and Cura profile management.

---

## Hardware Setup

### Printer Specifications
- **Model**: Creality Ender-3 V2
- **Build Plate**: 220×220 mm
- **Nozzle**: 0.4 mm standard
- **Bed Leveling**: BLTouch (auto-leveling)
- **Filament Diameter**: 1.75 mm
- **Max Hotend Temp**: 260°C
- **Max Bed Temp**: 110°C

### BLTouch Configuration
- **Type**: 3D Touch (BLTouch compatible)
- **Probe Offset**: Varies by installation (calibrate during first setup)
- **Auto-leveling**: Enabled via `G29` command
- **Start G-code**: Includes `G28` (home) + `G29` (auto-level)

### First Print Setup
1. Home printer: `G28`
2. Run auto-level: `G29`
3. Check first layer (should be ~0.1mm gap from nozzle)
4. If needed, adjust BLTouch offset via Cura or M851 command
5. Clean bed with IPA before printing
6. Run test print (25mm cube or bed level pattern)

---

## Material Profiles

All profiles use **MindCubby PETG - Standard.curaprofile** as base, with material-specific adjustments.

### PLA (Standard)
| Setting | Value |
|---------|-------|
| **Nozzle Temp** | 200-210°C |
| **Bed Temp** | 60°C |
| **Print Speed** | 40-60 mm/s |
| **Layer Height** | 0.20 mm |
| **Retraction** | 5mm @ 40mm/s |
| **Fan** | 100% after first layer |
| **First Layer Speed** | 20 mm/s |
| **Notes** | Good for detail work, reliable adhesion |

### PETG (Recommended for MindCubby)
| Setting | Value |
|---------|-------|
| **Nozzle Temp** | 230-250°C |
| **Bed Temp** | 70-80°C |
| **Print Speed** | 30-50 mm/s |
| **Layer Height** | 0.20 mm |
| **Retraction** | 5mm @ 40mm/s |
| **Fan** | 50% (avoid excessive cooling) |
| **First Layer Speed** | 20 mm/s |
| **Notes** | Stronger than PLA, better layer adhesion |

### TPU / Flexible Filament
| Setting | Value |
|---------|-------|
| **Nozzle Temp** | 220-240°C |
| **Bed Temp** | 50°C |
| **Print Speed** | 20-30 mm/s |
| **Retraction** | Disable (TPU doesn't retract well) |
| **Layer Height** | 0.20-0.30 mm |
| **Fan** | 0-25% (minimal) |
| **First Layer Speed** | 15 mm/s |
| **Notes** | Print slowly, use wide nozzle traces |

### ASA (Advanced)
| Setting | Value |
|---------|-------|
| **Nozzle Temp** | 240-250°C |
| **Bed Temp** | 100-110°C |
| **Print Speed** | 25-35 mm/s |
| **Layer Height** | 0.20 mm |
| **Retraction** | 6mm @ 40mm/s |
| **Fan** | 25-50% |
| **Notes** | Requires heated enclosure, strong & UV-resistant |

---

## Cura Profile Management

### Install MindCubby Profile
1. Copy `MindCubby PETG - Standard.curaprofile` to Cura profiles folder:
   - **macOS**: `~/Library/Application Support/CuraEngine/profiles/`
   - **Windows**: `%APPDATA%\CuraEngine\profiles\`
   - **Linux**: `~/.config/CuraEngine/profiles/`
2. Restart Cura
3. Select "MindCubby PETG - Standard" from profile dropdown

### Load Custom G-code
1. Open Cura → **Preferences** → **Printers** → Select Ender-3 V2
2. Click **Machine Settings**
3. Go to **Start/End G-code** tab
4. Copy from `CURA-SETTINGS/active/START_GCODE.txt`
5. Paste into **Start G-code** field
6. Copy from `CURA-SETTINGS/active/END_GCODE.txt`
7. Paste into **End G-code** field
8. Click **Close**

### Available G-code Variants
- **Baseline** (`Ender3V2_Baseline_StartGCode.gcode`) - Original working version
- **Optimized v1** - Improved priming with parallel lines
- **Optimized v6** - Lower Z height for better first-layer adhesion
- See `CURA-SETTINGS/archived/` for all versions with specs

### Apply Per-Print Settings
| Setting | Override | Value |
|---------|----------|-------|
| Nozzle Temp | Material | Material-specific (see above) |
| Bed Temp | Material | Material-specific (see above) |
| Layer Height | Model | 0.20mm (standard) or 0.12mm (detail) |
| Support | Model | Enable if needed |
| Print Speed | Model | 40-60mm/s (depends on material) |
| Wall Line Count | Model | 2-4 walls for strength |

---

## Maintenance

### Before Each Print
- [ ] Clean bed with IPA (isopropyl alcohol)
- [ ] Check nozzle for residue
- [ ] Run auto-level (`G29` via Cura or Pronterface)
- [ ] Test first layer height
- [ ] Verify filament path is clear

### Weekly
- [ ] Check belt tension (should have ~5-10mm play)
- [ ] Verify all bolts are tight
- [ ] Clean build plate with warm soapy water

### Monthly
- [ ] Deep clean hot-end and nozzle
- [ ] Check for wear on Z-axis leadscrew
- [ ] Inspect BLTouch sensor for dust
- [ ] Verify bed leveling accuracy

### As Needed
- [ ] Replace nozzle (every 100+ hours or if damaged)
- [ ] Calibrate BLTouch offset after any physical changes
- [ ] Clean extruder gear if filament slips

---

## Troubleshooting

### First Layer Issues
**Problem**: Uneven first layer height  
**Solution**: Run `G29` (auto-level), verify BLTouch offset

**Problem**: Nozzle too close (rubbing bed)  
**Solution**: Increase BLTouch offset (M851 Z+0.05), re-level

**Problem**: Nozzle too far (poor adhesion)  
**Solution**: Decrease BLTouch offset (M851 Z-0.05), re-level

### Print Quality
**Problem**: Poor layer adhesion  
**Solution**: Clean bed, increase bed temperature +5°C, check nozzle height

**Problem**: Stringing/Oozing  
**Solution**: Increase retraction (6-8mm), reduce nozzle temperature

**Problem**: Under-extrusion  
**Solution**: Verify filament isn't tangled, check nozzle isn't clogged, increase temp +5°C

### Mechanical Issues
**Problem**: X/Y axis grinding  
**Solution**: Clean rails, check for debris, verify belt tension

**Problem**: Z-axis stuttering  
**Solution**: Check leadscrew for debris, verify coupling alignment

**Problem**: Bed not heating**  
**Solution**: Verify heater is plugged in, check thermal fuse (usually under bed)

---

## Quick Temperature Reference

| Material | Nozzle | Bed | Speed | Fan |
|----------|--------|-----|-------|-----|
| **PLA** | 200-210°C | 60°C | 50mm/s | 100% |
| **PETG** | 230-250°C | 75°C | 40mm/s | 50% |
| **TPU** | 220-240°C | 50°C | 25mm/s | 0-25% |
| **ASA** | 240-250°C | 105°C | 30mm/s | 25-50% |

---

## Cura Slicer Tips

### Quick Profiles
1. **Draft** (Fast) - Lower quality, fast prints
   - Layer Height: 0.30mm
   - Infill: 15%
   - Speed: 60mm/s

2. **Standard** (Balanced) - Good quality & speed
   - Layer Height: 0.20mm
   - Infill: 20%
   - Speed: 40mm/s

3. **Quality** (Detailed) - High quality, slower
   - Layer Height: 0.12mm
   - Infill: 25%
   - Speed: 30mm/s

### Support Generation
- **Infill Pattern**: Grid (fastest)
- **Support Density**: 15% (balance between strength and removal)
- **Z Distance**: 0.2mm (easier removal)
- **Interface Layer**: Enabled (faster to remove)

### Adhesion Methods
- **Brim** - Best for small parts (1-2 lines)
- **Raft** - Best for large parts prone to warping (3-4 lines)
- **Skirt** - Just for priming, helps with nozzle wiping

---

## Related Documentation

- **REFERENCE.md** - Quick commands, workflows, automation
- **README.md** - Project overview and quick start

---

**Last Updated**: November 12, 2025  
**Status**: Complete
