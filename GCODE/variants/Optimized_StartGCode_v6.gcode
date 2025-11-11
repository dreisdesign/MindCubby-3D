; Ender 3 V2 - Optimized Start G-code (v6)
; Purpose: Improve first-layer adhesion by applying a lower initial Z for priming/skirt
; Date: 2025-11-10
; Variant: optimized with BLTouch saved mesh enabled and prime/wipe sequence

M140 S{material_bed_temperature} ; Set bed temp (non-blocking)
M104 S{material_print_temperature} ; Set nozzle temp (non-blocking)
M190 S{material_bed_temperature} ; Wait for bed
M109 S{material_print_temperature} ; Wait for nozzle

G92 E0 ; Reset extruder
G28 ; Home all axes
M420 S1 ; Enable saved mesh from EEPROM

G1 Z2.0 F3000 ; Lift Z a little
G1 X0.1 Y20 Z0.15 F5000.0 ; Move to start position - lowered Z (0.15 mm)
G1 X0.1 Y200.0 Z0.15 F1500.0 E12 ; Draw the first prime line (reduced extrusion)
G1 X0.4 Y200.0 Z0.15 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.15 F1500.0 E24 ; Draw the second prime line
G1 E-1.5 F1800 ; Retract 1.5mm
G92 E0 ; Reset Extruder
G1 Z5.0 F3000 ; Lift Z to clear print
G1 X30 Y5 F5000.0 ; Wipe across bed edge
G1 Z2.0 F3000 ; Lower back to safe clearance
G1 X30 Y20 Z2.0 F5000.0 ; Move over to safe print start area
G1 Z0.15 F1000 ; Lower to first-layer prime height
G1 E0.8 F600 ; Small purge onto sacrificial area
G1 E-1.5 F1800 ; Retract back to reduce ooze
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Raise back to safe clearance
