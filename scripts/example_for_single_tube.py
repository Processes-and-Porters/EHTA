'''
测试文件，用于检测shapes文件夹内的.py文件
'''
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from emphtra.unit_conversion import *
from shapes.tube_related import *
from properties.fluid import *
from thermal_resistance.SinglePhaseTurbulent_Inside_Pipe import *

tube1 = tube(88.9,2.77,1000)
tube2 = tube(114.3,2.77,1000)

dicProperty = { 'rho_kg_m3':1000.0,\
                'mu_Pas':8.9*10**(-4),\
                'lambda_W_mK':0.62,\
                'Cp_J_kgK':4187}
water = fluid(dicProperty)

TR_tube = Gnielinski_TF_Tube(tube1, water, m3_sfm3_h(10))
Re=TR_tube.Re_1
print(Re())
print(TR_tube.u_m_s)


#testtube.outer_heat_transfer_area



