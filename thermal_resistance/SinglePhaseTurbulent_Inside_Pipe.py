
#The following py must be imported
#emphtra.unit_conversion

from emphtra.unit_conversion import *
from thermal_resistance.dimensionless_numbers import *

class Gnielinski_TF_Tube(object):
    
  def __init__(self,objTube,objFluid,V_m3_s):
  # objTube is an instance of class tube
  # objFluid is an instance of class fluid
      self.V_m3_s=V_m3_s
      self.objTube=objTube
      self.objFluid=objFluid
      self.u_m_s=V_m3_s/m2fmm2(objTube.Ats_mm2)
      
  # Renolds Number dimensionless
  def Re_1(self):
      return self.objFluid.rho_kg_m3 * \
              self.u_m_s * \
              mfmm(self.objTube.Dti_mm)
  # Prandl Number
  def Pr_1(self):
      return self.objFluid.Cp_J_kgK * \
              self.objFluid.mu_Pas / \
              sefl.objFluid.lambda_W_mK
