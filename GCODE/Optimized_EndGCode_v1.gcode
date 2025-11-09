; Ender 3 V2 Optimized End G-code - v1.0
; Date: 2025-11-09
; Purpose: Final retract, park, and warm hold for quick reprints
; Status: Production - optimized for rapid iteration

; --- RETRACT & LIFT ---
G91 ; Relative positioning
G1 E-2 F2700 ; Retract filament 2mm quickly
G1 E-2 Z0.2 F2400 ; Retract another 2mm and raise Z 0.2mm
G1 Z10 F3000 ; Raise Z axis 10mm total (clear print)

G90 ; Switch back to Absolute positioning

; --- PARK & COOL SLIGHTLY ---
G1 X0 Y{machine_depth} ; Park nozzle at front-left (easy access to print)
M106 S0 ; Turn-off cooling fan

; --- WARM HOLD PHASE (for quick reprints) ---
; Keep nozzle and bed warm so reheat is fast
M104 S180 ; Nozzle to 180°C (warm standby, 60s to reach 220°C)
M140 S70 ; Bed to 70°C (close to PETG, minimal reheat needed)

G4 P300000 ; **DWELL:** Pause 5 minutes (300,000ms) - time to assess print quality and decide

; --- FINAL SHUTDOWN (after hold decision) ---
M104 S0 ; Turn-off hotend
M140 S0 ; Turn-off bed

M84 X Y E ; Disable X, Y, E steppers (Z remains locked to hold position)

; Print is now parked at front-left, nozzle/bed cooled but not frozen
; Ready for quick reprint or manual removal
