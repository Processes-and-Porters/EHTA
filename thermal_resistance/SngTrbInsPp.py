'''Collection of single phase turbulent heat transfer and thermal resistance

'''
import math
#The following py must be imported
#emphtra.unit_conversion

from emphtra.unit_conversion import *
from emphtra.node import *
from emphtra.exceptions import *



#Gnielinski
class GnielinskiSngTrbInsPp(object):
    '''caculate in tube turbulent flow heat transfer coefficient
    
    
    '''
    
  #Please Refer to HEDH 1983 2.5.1 (41)    
    def __init__(self,objTube,objFluid, V_m3_s,
            node1 = {"T_C" : 25, "Q_kW" : 0},
            node2 = {"T_C" : 25, "Q_kW" : 0},
            mode = "heating"):
    # objTube is an instance of class tube
    # objFluid is an instance of class fluid
        self.V_m3_s=V_m3_s
        self.objTube=objTube
        self.objFluid=objFluid
        self.node_initializer(node1,node2)

    # Find the task
    def node_initializer(self,node1,node2):
        '''define the task for this element

           node1(T1,Q1),node2(T2,Q2)
            T1      T2      Q1         Q2     mode       input    output/overide
           -----------------------------------------------------------------------------------
           any      any   !=""&!=Q2   !=""    any                 exception: heat unbalance
           !=""    !=""    !=""       any     any                 exceotion: over rigid  
            =""     any     any       any     any                 exceotion: no temperature difference
           !=""     =""     =""        =""    any                 exception: insufficient input 
            =""    !=""     =""        =""    any                 exception: insufficient input 

           !=""     !=""    =""        =""    any        T1,T2    Q1,Q2=Q1

           !=""     =""    !=""        =""    any        T1,Q1    Q2=Q1,T2    
           !=""     =""     =""       !=""    any        T1,Q2    Q1=Q2,T2    
            >T2    !=""    !=""        =""    heating    T1,Q1    Q1=Q2,T2    
            >T2    !=""     =""       !=""    heating    T1,Q2    Q1=Q2,T2    
           !=""     >T1    !=""        =""    heating    T2,Q1    Q2=Q1,T1    
           !=""     >T1     =""       !=""    heating    T2,Q2    Q2=Q1,T1    
            <T2    !=""    !=""        =""    cooling    T1,Q1    Q1=Q2,T2    
            <T2    !=""     =""       !=""    cooling    T1,Q2    Q1=Q2,T2    
           !=""     <T1    !=""        =""    cooling    T2,Q1    Q2=Q1,T1    
           !=""     <T1     =""       !=""    cooling    T2,Q2    Q2=Q1,T1    


        '''
        #rule out four exceptions
        if node1["Q_kW"] != node2["Q_kW"] \
                and node1["Q_kW"] != "" and node2["Q_kW"] != "":
                    raise InvalidNodeError("heat unbalance") 
        if node1["T_C"] == node2["T_C"] :
            raise InvalidNodeError("no temperature difference")
        if node1["Q_kW"] == "" and node2["Q_kW"] == "" :
            pass
        elif node1["T_C"] != "" and node2["T_C"] != "" :
            raise InvalidNodeError("over rigid")
        if node1["T_C"] != "" and node2["T_C"] == "" \
                and node1["Q_kW"] == "" and node2["Q_kW"] == "" :
                    raise InvalidNodeError("insufficient input")
        if node1["T_C"] == "" and node2["T_C"] != "" \
                and node1["Q_kW"] != "" and node2["Q_kW"] == "" :
                    raise InvalidNodeError("insufficient input")

        # a special case where only temperatures are set
        if node1["Q_kW"] == "" and node2["Q_kW"] == "" :
            pass
        else:
            #set Q
            if node1["Q_kW"] != "" and node2["Q_kW"] == "" :
                node2["Q_kW"] == node1["Q_kW"]
            elif node2["Q_kW"] != "" and node1["Q_kW"] == "" :
                node1["Q_kW"] == node2["Q_kW"]
            #set T
            if self.mode == "heating" :
                if node1["T_C"] > node2["T_C"] :
                    node2["T_C"] == ""
                else:
                    node1["T_C"] == ""
            if self.mode == "cooling" :
                if node1["T_C"] < node2["T_C"] :
                    node2["T_C"] == ""
                else:
                    node1["T_C"] == ""

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
