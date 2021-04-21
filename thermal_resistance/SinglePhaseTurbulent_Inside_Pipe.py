
import math

#The following py must be imported
#emphtra.unit_conversion

from emphtra.unit_conversion import *

#Gnielinski
class Gnielinski_TF_Tube(object):
#Please Refer to HEDH 1983 2.5.1 (41)    
  def __init__(self,objTube,objFluid,V_m3_s):
  # objTube is an instance of class tube
  # objFluid is an instance of class fluid
      self.V_m3_s=V_m3_s
      self.objTube=objTube
      self.objFluid=objFluid

  # Fluid Velocity
  def u_m_s(self):
      return self.V_m3_s/m2fmm2(self.objTube.St_mm2)
  # Renolds Number dimensionless
  def Re_1(self):
      return self.objFluid.rho_kg_m3 * \
              self.u_m_s() * \
              mfmm(self.objTube.Dti_mm) / \
              self.objFluid.mu_Pas
  # Prandl Number
  def Pr_1(self):
      return self.objFluid.Cp_J_kgK * \
              self.objFluid.mu_Pas / \
              self.objFluid.lambda_W_mK
  # Friction factor
  def f_1(self):
      return ( 1.82 * math.log10(self.Re_1()) - 1.64 ) ** (-2)
  # Nusselt Number
  def Nu_1(self):
      return self.f_1()/8*(self.Re_1()-1000)*self.Pr_1() / \
              ( 1.0 + 1.27 * (self.f_1())**0.5 * \
                ( self.Pr_1() ** (2/3) -1 ) ) *\
              ( 1.0 + \
                (self.objTube.Dti_mm / self.objTube.Lt_mm) ** \
                (2/3) )
  # Heat transfer rate
  def alpha_W_m2K(self):
      return self.Nu_1() * \
              self.objFluid.lambda_W_mK / \
              mfmm(self.objTube.Dti_mm)
  # Heat Resistence
  def r_m2K_W(self):
      return 1.0 / self.alpha_W_m2K()
