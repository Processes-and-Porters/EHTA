#这个作为引入物性数据的接口
#This serves as a port to physical data
class fluid():
    def __init__(self,dicProperty):
    #dicProperty is dictionary of properties of a fluid:
    # {'rho_kg_m3':density in kg/m^3,
    #  'mu_Pas':dynamic viscosity,
    #  'Cp_J_kgK':specific heat capacity,...}
      self.rho_kg_m3 = dicProperty['rho_kg_m3'] #fluid dense kg/m^3
      self.mu_Pas =dicProperty['mu_Pas'] #fluid dynamic viscosity Pa*s 
      self.Cp_J_kgK = dicProperty['Cp_J_kgK'] #fluid specific heat capacity J/kg/K
      self.lambda_W_mK = dicProperty['lambda_W_mK'] #fluid thermal_conductivity W/m/K 

class liquid():
  pass
class gas():
  pass
class mixture():
  pass

