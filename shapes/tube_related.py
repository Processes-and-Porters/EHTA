# tube is a shape 
class tube(object) :

   inner_diameter = ""
   Dti = "" #Tube inner diameter
   Dt = "" #Tube outer diameter
   outer_diameter = ""
   wall_thickness = ""
   Ltw = "" #Tube wall thickness
   Lta = "" #Tube length
   length = ""
   outer_heat_transfer_area = ""
   cross_section_area = ""


   def __init__(self,outer_diameter,wall_thickness,length):
       self.outer_diameter = outer_diameter
       self.wall_thickness = wall_thickness
       self.inner_diameter = outer_diameter - wall_thickness
       self.length = length

   def outer_heat_transfer_area(self):       
       return 3.14 * self.outer_diameter * self.length 

   def inner_heat_transfer_area(self):       
       return 3.14 * self.inner_diameter * self.length

   def flow_cross_section_area(self):       
       return 3.14 * self.inner_diameter**2.0 / 4.0

class utube(object) :
    pass
class tube_bundle :
    pass
