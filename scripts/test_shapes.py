'''
测试文件，用于检测shapes文件夹内的.py文件
'''
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from shapes.tube_related import tube

od = 88.9
thickness = 2.77
length = 1000

testtube = tube(od,thickness,length)
#testtube.outer_heat_transfer_area

print(testtube.outer_heat_transfer_area())
print(testtube.inner_heat_transfer_area())
print(testtube.flow_cross_section_area())

