; Ender 3 V2 - Optimized Start G-code (v6)
; Purpose: Improve first-layer adhesion by applying a lower initial Z for priming/skirt
; Date: 2025-11-10
; Notes:
; - This file preserves the baseline priming strategy but reduces the Z used for the
;   prime/skirt moves to improve squish/adhesion.
; - If you have a probe (BLTouch) or mesh bed leveling enabled, consider running
;;  G28
;  G29
;  or enable saved mesh with M420 S1 after homing. Only use G29 if your firmware supports it.
; - If you use a probe and have a known probe offset, persist it with M851 Z<offset> and M500
;   (example: M851 Z-1.85 ; M500). Do not commit offsets into the repo — keep them local.

M140 S{material_bed_temperature} ; Set bed temp (non-blocking)
M104 S{material_print_temperature} ; Set nozzle temp (non-blocking)
M190 S{material_bed_temperature} ; Wait for bed
M109 S{material_print_temperature} ; Wait for nozzle

G92 E0 ; Reset extruder
G28 ; Home all axes
; Enable saved BLTouch mesh so skirt/prime use mesh compensation (saved mesh: MRISCOC)
M420 S1 ; Enable mesh from EEPROM
; If you prefer to re-probe each print, replace the above with G29 (takes longer)

; Move Z up slightly to avoid scratching, then go to prime start position
G1 Z2.0 F3000 ; Lift Z a little
; Use a slightly lower Z for priming/skirt to improve squish/adhesion
G1 X0.1 Y20 Z0.15 F5000.0 ; Move to start position - lowered Z (0.15 mm)
G1 X0.1 Y200.0 Z0.15 F1500.0 E12 ; Draw the first prime line (reduced extrusion to limit ooze)
G1 X0.4 Y200.0 Z0.15 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.15 F1500.0 E24 ; Draw the second prime line (reduced extrusion)
; Retract slightly to prevent oozing/blob pickup, then wipe on bed edge
G1 E-1.5 F1800 ; Retract 1.5mm (increase to reduce oozing)
G92 E0 ; Reset Extruder
G1 Z5.0 F3000 ; Lift Z to clear print
G1 X30 Y5 F5000.0 ; Wipe across bed edge to remove any residual blob
G1 Z2.0 F3000 ; Lower back to safe clearance
G1 X30 Y20 Z2.0 F5000.0 ; Move over to safe print start area
; Sacrificial micro-prime at first layer height to purge any remaining ooze off-print
G1 Z0.15 F1000 ; Lower to first-layer prime height (matches skirt height)
G1 E0.8 F600 ; Small purge onto sacrificial area
G1 E-1.5 F1800 ; Retract back to reduce ooze
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Raise back to safe clearance

; Ready to start print - printer should now align first layer closer to bed for better adhesion

; Troubleshooting notes:
; - If first layer is still too high: reduce Z in the three G1 lines above by -0.05 mm increments (try 0.10 mm)
; - If nozzle drags into the bed: increase Z by +0.05 mm steps until safe
; - For persistent offset differences: measure and set probe offset with M851 and save with M500
