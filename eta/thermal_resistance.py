'''
热阻计算模块
此文件初步应用于无相变管壳式换热器
由于换热器的管束有Φ25X2.5mm和Φ19X2mm两种，管径远大于壁厚，所以采用R=R1+Rw+R2计算总传热热阻，完全可以满足工业的精度要求
R1为管内热阻，Rw为管壁导热热阻，R2为管外热阻
管壁导热热阻需考虑污垢热阻等，后续进一步细化
'''


class Thermal_Resistance():

    def __init__(self, a1, a2, thickness, lamda):
        """Initialize class

        Args:
         a1：管内流体等对流换热系数
         a2：管外流体等对流换热系数
         thickness：壁厚
         lambda：管束的导热系数，python中lambda最好别随便用，所以写了个lamda
        上述参数一般都是经计算或查表得出，此处为快速搭框架直接引入了，后续再细化该部分参数
        """
        self.a1 = a1
        self.a2 = a2
        self.thickness = thickness
        self.lamda = lamda

    def in_tube_thermal_resistance(self):
        """
        计算管内热阻
        """
        return float(1 / self.a1)

    def out_tube_thermal_resistance(self):
        """
        计算管外热阻
        """
        return float(1 / self.a2)

    def tube_wall_thermal_resistance(self):
        """
        计算管壁导热热阻
        """
        return float(self.thickness / self.lamda)
    # return里的加号用不了，不知道为什么
    # def K(self):
    #     return self.in_tube_thermal_resistance + self.out_tube_thermal_resistance + self.tube_wall_thermal_resistance
