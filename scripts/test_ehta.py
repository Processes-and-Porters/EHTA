'''
测试文件，用于检测ehta文件夹内的.py文件
'''
from ehta import thermal_resistance
from ehta import reynolds_number
from ehta import print_test

a1 = 238
a2 = 200
thickness = 0.002
lamda = 50

rezu = thermal_resistance.Thermal_Resistance(a1, a2, thickness, lamda)
in_tube_rezu = rezu.in_tube_thermal_resistance()
out_tube_rezu = rezu.out_tube_thermal_resistance()
tube_wall_rezu = rezu.tube_wall_thermal_resistance()

print(in_tube_rezu)
print(out_tube_rezu)
print(tube_wall_rezu)
print(in_tube_rezu + out_tube_rezu + tube_wall_rezu)

