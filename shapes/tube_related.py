class tube(object) :
# tube is-a shape 
   def __init__(self,Dt_mm,Ltw_mm,Lt_mm):
       self.Dt_mm = Dt_mm #Tube outer diameter, mm
       self.Ltw_mm = Ltw_mm #Tube wall thickness, mm
       self.Dti_mm = Dt_mm - 2 * Ltw_mm #Tube inner diameter, mm
       self.Lt_mm = Lt_mm #Tube length of Active Heat Transfer Area, mm
       self.Ata_mm2 = 3.14 * self.Dt_mm * self.Lt_mm #Active Outer Heat Transfer Area, mm2
       self.Ati_mm2 = 3.14 * self.Dti_mm * self.Lt_mm #inner Heat Transfer Area, mm2
       self.St_mm2 = 3.14 * self.Dti_mm**2.0 / 4.0#tube inner cross section Area, mm2

class utube(object) :
    pass
class tube_bundle :
    pass
