; Ender 3 V2 Optimized Start G-code - v2.0
; Date: 2025-11-09
; Improvements: 
;   - v1.0: 2 parallel priming lines (same Y direction)
;   - v2.0: Enhanced blob clearance - move away from prime line before skirt
; Status: Active optimization - testing blob catch issue fix

G92 E0 ; Reset Extruder
G28 ; Home all axes
G1 Z2.0 F3000 ; Move Z Axis up to prevent scratching
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position

; Prime line 1: Y direction, extrude 15mm
G1 X0.1 Y200.0 Z0.3 F1500.0 E15
; Move to side (0.3mm spacing for clean nozzle)
G1 X0.4 Y200.0 Z0.3 F5000.0

; Prime line 2: Y direction (same direction as line 1), extrude 15mm
G1 X0.4 Y20 Z0.3 F1500.0 E15
G92 E0 ; Reset Extruder

; Move far away from prime lines to avoid blob catch
; Move to X30 (clear of typical 10-15mm skirt start)
G1 Z2.0 F3000 ; Move Z up
G1 X30 Y20 Z0.3 F5000.0 ; Move 30mm away from prime lines

