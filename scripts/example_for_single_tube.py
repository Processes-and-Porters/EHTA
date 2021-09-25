'''
测试文件，用于检测shapes文件夹内的.py文件
'''
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from emphtra.unit_conversion import *
from shapes.tube_related import *
from properties.fluid import *
from thermal_resistance.SngTrbInsPp import *

tube1 = tube(88.9,3.05,1000)

dicProperty = { 'rho_kg_m3':1000.0,\
                'mu_Pas':8.9*10**(-4),\
                'lambda_W_mK':0.62,\
                'Cp_J_kgK':4187}
water = fluid(dicProperty)
node1 = {"T_C" : 50, "Q_kW" : 0}
node2 = {"T_C" : 25, "Q_kW" : 0}

TR_tube = GnielinskiSngTrbInsPp(tube1, water, m3_sfm3_h(60), node1, node2)
print(tube1.St_mm2)
print(TR_tube.u_m_s())
print(TR_tube.Re_1())
print(TR_tube.Pr_1())
print(TR_tube.f_1())
print(TR_tube.Nu_1())
print(TR_tube.alpha_W_m2K())

#testtube.outer_heat_transfer_area
