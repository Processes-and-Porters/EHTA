#这个作为引入物性数据的接口
#This serves as a port to physical data
class fluid():
    def __init__(self,data_list):
    #data_list is list of properties of a fluid:
    # [dense_mm, viscosity_Pas,........]
      self.rho_kg_m3 = data_list[0] #fluid dense kg/m3
      self.mu_Pas = data_list[1]  #fluid dynamic viscosity Pa*s 

class liquid():
  pass
class gas():
  pass
class mixture():
  pass

