; MC3D--PRUSA_START_GCODE (2025-12-02)
; Ender 3 V2 - Optimized Start G-code (PrusaSlicer Converted)
; Purpose: Improve first-layer adhesion by applying a lower initial Z for priming/skirt
; Format: PrusaSlicer / SuperSlicer
; Settings: 1.02 flow, 0 retraction, 4-sec stabilization dwell

M140 S[first_layer_bed_temperature] ; Set bed temp (non-blocking)
M104 S[first_layer_temperature] ; Set nozzle temp (non-blocking)
M190 S[first_layer_bed_temperature] ; Wait for bed
M109 S[first_layer_temperature] ; Wait for nozzle

G92 E0 ; Reset extruder
G28 ; Home all axes
M82 ; Set extruder to absolute mode
G90 ; Ensure absolute positioning
M501 ; Load settings from EEPROM
M420 S1 ; Enable mesh from EEPROM

G1 Z2.0 F3000 ; Lift Z
; --- Simple purge line (no blob) ---
G1 X10 Y200 F5000.0 ; Move to purge corner
G1 Z0.2 F1200.0 ; Lower to first layer height
G1 X150 Y200 Z0.2 F1500.0 E10 ; Single prime line (minimal extrusion)
G92 E0 ; Reset extruder
G1 Z2.0 F3000 ; Lift Z
G4 P2000 ; Dwell 2 seconds - let nozzle stabilize
G1 X30 Y20 Z2.0 F5000.0 ; Move to print start area
