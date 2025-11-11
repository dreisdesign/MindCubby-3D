; Optimized Start G-code - v5 (archived)

M104 S{material_print_temperature} ; Preheat nozzle (non-blocking)
M190 S{material_bed_temperature} ; Heat bed and wait
M109 S{material_print_temperature} ; Wait for nozzle
G92 E0
G28
G29
G1 Z2.0 F3000
G1 X0.1 Y20 Z0.3 F5000.0
G1 X0.1 Y200.0 Z0.3 F1500.0 E15
G1 X0.4 Y200.0 Z0.3 F5000.0
G1 X0.4 Y20 Z0.3 F1500.0 E15
G92 E0
G1 E-0.5 F2400
G1 Z5.0 F3000
G1 X220 Y5 Z0.3 F5000.0
G1 Z0.3 F3000
