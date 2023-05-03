;FLAVOR:Marlin
;TIME:13
;Filament used: 0.00834871m
;Layer height: 0.2
;Generated with Cura_SteamEngine 3.6.0
M140 S60
M105
M190 S60
M104 S195
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
M106 S255
M204 S3000
M205 X10 Y10
;MESH:cube.stl
G0 F3000 X106.92 Y106.92 Z0.2
M204 S1800
M205 X8 Y8
;TYPE:WALL-INNER
G1 F2400 E0
G1 X103.08 Y106.92 E0.17881
G1 X103.08 Y103.08 E0.35761
G1 X106.92 Y103.08 E0.53642
G1 X106.92 Y106.92 E0.71523
M204 S3000
M205 X10 Y10
G0 F3000 X107.48 Y107.48
M204 S1800
M205 X8 Y8
G1 F2400 X102.52 Y107.48 E0.94618
G1 X102.52 Y102.52 E1.17714
G1 X107.48 Y102.52 E1.4081
G1 X107.48 Y107.48 E1.63906
M204 S3000
M205 X10 Y10
G0 F3000 X108.04 Y108.04
M204 S1800
M205 X8 Y8
G1 F2400 X101.96 Y108.04 E1.92217
G1 X101.96 Y101.96 E2.20528
G1 X108.04 Y101.96 E2.48839
G1 X108.04 Y108.04 E2.7715
M204 S3000
M205 X10 Y10
G0 F3000 X108.6 Y108.6
M204 S1800
M205 X8 Y8
G1 F2400 X101.4 Y108.6 E3.10676
G1 X101.4 Y101.4 E3.44202
G1 X108.6 Y101.4 E3.77729
G1 X108.6 Y108.6 E4.11255
M204 S3000
M205 X10 Y10
G0 F3000 X109.16 Y109.16
M204 S1800
M205 X8 Y8
G1 F2400 X100.84 Y109.16 E4.49996
G1 X100.84 Y100.84 E4.88738
G1 X109.16 Y100.84 E5.27479
G1 X109.16 Y109.16 E5.66221
M204 S3000
M205 X10 Y10
G0 F3000 X109.72 Y109.72
M204 S1800
M205 X8 Y8
;TYPE:WALL-OUTER
G1 F2400 X100.28 Y109.72 E6.10177
G1 X100.28 Y100.28 E6.54134
G1 X109.72 Y100.28 E6.9809
G1 X109.72 Y109.72 E7.42047
M204 S3000
M205 X10 Y10
G0 F3000 X109.52 Y109.72
G0 X109.09 Y109.09
G0 X106.37 Y106.37
M204 S1800
M205 X8 Y8
;TYPE:SKIN
G1 F2400 X103.63 Y106.37 E7.54806
G1 X103.63 Y103.63 E7.67564
G1 X106.37 Y103.63 E7.80323
G1 X106.37 Y106.37 E7.93081
M204 S3000
M205 X10 Y10
G0 F3000 X106.109 Y104.525
M204 S1800
M205 X8 Y8
G1 F2400 X105.474 Y103.89 E7.97263
M204 S3000
M205 X10 Y10
G0 F3000 X104.682 Y103.89
M204 S1800
M205 X8 Y8
G1 F2400 X106.109 Y105.317 E8.0666
M204 S3000
M205 X10 Y10
G0 F3000 X106.109 Y106.109
M204 S1800
M205 X8 Y8
G1 F2400 X103.889 Y103.889 E8.21279
M204 S3000
M205 X10 Y10
G0 F3000 X103.889 Y104.681
M204 S1800
M205 X8 Y8
G1 F2400 X105.317 Y106.109 E8.30683
M204 S3000
M205 X10 Y10
G0 F3000 X104.525 Y106.109
M204 S1800
M205 X8 Y8
G1 F2400 X103.889 Y105.473 E8.34871
;TIME_ELAPSED:13.911696

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
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Fine #2\\ndefini
;SETTING_3 tion = anycubic_i3_mega\\n\\n[metadata]\\nquality_type = normal\\ntyp
;SETTING_3 e = quality_changes\\nsetting_version = 5\\n\\n[values]\\nadhesion_ty
;SETTING_3 pe = none\\nlayer_height = 0.2\\nmaterial_bed_temperature = 60\\nsupp
;SETTING_3 ort_enable = True\\nsupport_type = everywhere\\n\\n", "extruder_quali
;SETTING_3 ty": ["[general]\\nversion = 4\\nname = Fine #2\\ndefinition = anycub
;SETTING_3 ic_i3_mega\\n\\n[metadata]\\nquality_type = normal\\ntype = quality_c
;SETTING_3 hanges\\nposition = 0\\nsetting_version = 5\\n\\n[values]\\ngradual_i
;SETTING_3 nfill_steps = 0\\ninfill_pattern = grid\\ninfill_sparse_density = 10\
;SETTING_3 \nmaterial_print_temperature = 195\\nretraction_hop = 0.1\\nspeed_pri
;SETTING_3 nt = 80\\nsupport_angle = 55\\nsupport_infill_rate = 10\\nwall_thickn
;SETTING_3 ess = 2.5\\n\\n"]}
