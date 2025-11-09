; Ender 3 V2 Optimized Start G-code - v4.0
; Date: 2025-11-09
; Improvements: 
;   - v1.0: 2 parallel priming lines (same Y direction)
;   - v2.0: Enhanced blob clearance - move away from prime line before skirt
;   - v3.0: Nozzle wipe sequence to clean blob before print start
;   - v4.0: Parallel heating (bed + nozzle at same time)
; Status: Active optimization - PLA profile with parallel heating
; Material: PLA | Bed: 60°C | Nozzle: 200°C

; Start heating bed and nozzle in PARALLEL
; M104: Set hotend temp (no wait) - starts heating immediately
; M190: Set bed temp AND WAIT - bed heats while nozzle catches up
M104 S200 ; Preheat nozzle to 200°C (non-blocking)
M190 S60 ; Heat bed to 60°C and wait for it
M109 S200 ; Wait for nozzle to reach 200°C

; Home and probe
G92 E0 ; Reset Extruder
G28 ; Home all axes
G29 ; BLTouch auto-level (if enabled in firmware)

G1 Z2.0 F3000 ; Move Z Axis up to prevent scratching
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position

; Prime line 1: Y direction, extrude 15mm
G1 X0.1 Y200.0 Z0.3 F1500.0 E15
; Move to side (0.3mm spacing for clean nozzle)
G1 X0.4 Y200.0 Z0.3 F5000.0

; Prime line 2: Y direction (same direction as line 1), extrude 15mm
G1 X0.4 Y20 Z0.3 F1500.0 E15
G92 E0 ; Reset Extruder

; Wipe nozzle clean across bed to remove blob
; Move to Y5 (away from print start area)
G1 X0.4 Y5 Z0.3 F5000.0
; Retract slightly to prevent oozing during move
G1 E-0.5 F2400
; Move up to clear bed before traveling
G1 Z5.0 F3000
; Travel to safe position away from prime lines
G1 X30 Y20 Z5.0 F5000.0
; Move back to first layer height
G1 Z0.3 F3000
