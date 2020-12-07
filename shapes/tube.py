# tube is a shape 
class tube

   inner_diameter = ""
   outer_diameter = ""
   wall_thickness = ""
   length = ""
   heat_transfer_area = ""
   cross_section_area = ""

   def _init_(self,outer_diameter,wall_thickness,length):
       self.outer_diameter = outer_diameter
       self.wall_thickness = wall_thickness
       self.inner_diameter = inner_diameter
       self.length = length

   def outer_heat_transfer_area():       
       return 3.14*outer_diameter*length

   def inner_heat_transfer_area():       
       return 3.14*inner_diameter*length

   def flow_cross_section_area():       
       return 3.14*inner_diameter^2/4

