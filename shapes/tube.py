# tube is a shape 
class tube

   diameter = ""
   length = ""
   heat_transfer_area = ""
   cross_section_area = ""

   def _init_(self,diameter,length):
       self.diameter = diameter
       self.length = length

   def heat_transfer_area():       
       return 3.14*diameter*length

   def cross_section_area():       
       return 3.14*diameter^2/4

