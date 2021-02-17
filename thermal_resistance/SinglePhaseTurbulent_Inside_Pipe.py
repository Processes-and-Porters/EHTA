
#The following py must be imported
#emphtra.unit_conversion

from emphtra.unit_conversion import *
from thermal_resistance.dimensionless_numbers import *

class Gnielinski_TF_Tube(object):
    
  def __init__(self,objTube,objFluid,V_m3):
  # objTube is an instance of class tube
  # objFluid is an instance of class fluid
      self.V_m3=V_m3
      self.objTube=objTube
      self.objFluid=objFluid
      self.u_m_s=V_m3/m2fmm2(objTube.Ats_mm2)
      
  # Renolds Number dimensionless
  def Re_1(rho_kg_m3,u_m_s,L_m):
          return rho_kg_m3 * u_m_s * L_m
  # Prandl Number
  def Pr_1(Cp_J_kgK, lambda_W_mK, mu_Pas):
          return Cp_J_kgK * mu_Pas / lambda_W_mK

  # Velocity
  

  
