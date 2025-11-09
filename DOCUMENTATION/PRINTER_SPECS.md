# Creality Ender-3 V2 Specifications

## Hardware
- **Build Volume**: 220 x 220 x 250 mm
- **Nozzle Diameter**: 0.4 mm (standard)
- **Bed Type**: Carborundum glass bed
- **Hotend**: Creality standard (MK8)
- **Z-Axis**: Lead screw (4mm pitch)
- **Leveling**: BLTouch (3D Touch compatible)

## Firmware
- **Mainboard**: Creality 4.2.2 (STM32F103RET6)
- **Firmware**: Marlin with BLTouch support

## Temperature Ranges
- **Bed**: Ambient to 110°C
- **Hotend**: Ambient to 300°C

## Material Profiles

### PLA
- **Bed Temp**: 60°C
- **Nozzle Temp**: 200-210°C
- **Print Speed**: 40-60 mm/s
- **Fan**: 100% after first layer

### PETG
- **Bed Temp**: 70-80°C
- **Nozzle Temp**: 230-250°C
- **Print Speed**: 30-50 mm/s
- **Fan**: 50% (avoid cooling)

### TPU/Flexible
- **Bed Temp**: 50°C
- **Nozzle Temp**: 220-240°C
- **Print Speed**: 20-30 mm/s (very slow)
- **Fan**: 0-25%

## Maintenance
- Clean bed with IPA after each print
- Check bed leveling monthly
- BLTouch probe: Keep clean and test regularly
