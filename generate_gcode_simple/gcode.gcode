; Bastian Lipka
M140 S60
M105
M190 S30
M104 S180
M105
M109 S195
M82 ;absolute extrusion mode
G21 ;metric values
G90 ;absolute positioning
M82 ;set extruder to absolute mode
M107 ;start with the fan off
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops
G1 Z15.0 F100 ;move the platform down 15mm
G92 E0 ;zero the extruded length
G1 F200 E3 ;extrude 3mm of feed stock
G92 E0 ;zero the extruded length again
G1 F100
M117 Printing...
G5
G92 E0
G1 F2400 E-6
;LAYER_COUNT:2
;LAYER:0
M106 S255 ;set fan speed
M204 S3000
M205 X10 Y10

G0 F3000 X100 Y100 Z0.2 ;start Point, layer shift
M204 S1800
M205 X8 Y8
G1 F2400 E0


G1 X130 Y100 E0.1
G1 X130 Y130 E0.2
G1 X100 Y130 E0.3
G1 X100 Y100 E0.4

G0 F3000 X100 Y100 Z0.4 ;start Point, layer shift

G1 X130 Y100 E0.5
G1 X130 Y130 E0.6
G1 X100 Y130 E0.7
G1 X100 Y100 E0.8

;end of print
;moves after print
G1 F2400 E2.34871
M140 S0
M204 S4000
M205 X20 Y20
M107
M104 S0 ; turn off extruder
M140 S0 ; turn off bed
M84 ; disable motors
M107
G91 ;relative positioning
G1 E-1 F300 ;retract the filament a bit before lifting the nozzle
to release some of the pressure
G1 Z+0.5 E-5 ;X-20 Y-20 F100 ;move Z up a bit and retract filament even more
G28 X0 ;Y0 ;move X/Y to min endstops
so the head is out of the way
G1 Y180 F2000
M84 ;steppers off
G90
M300 P300 S4000
M82 ;absolute extrusion mode
M104 S0
;End of Gcode