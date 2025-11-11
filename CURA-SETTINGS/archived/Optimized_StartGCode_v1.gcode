; Optimized Start G-code - v1 (archived)
; See variants for active versions

G92 E0 ; Reset Extruder
G28 ; Home all axes
G1 Z2.0 F3000 ; Move Z Axis up to prevent scratching
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
G1 X0.1 Y200.0 Z0.3 F1500.0 E15
G1 X0.4 Y200.0 Z0.3 F5000.0
G1 X0.4 Y20 Z0.3 F1500.0 E15
G92 E0
G1 Z2.0 F3000
G1 X5 Y20 Z0.3 F5000.0
