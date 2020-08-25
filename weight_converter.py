#Weight converter from Kilograms to Grams and Pounds
import math
class converter():
    def kgs_gms_lbs(self,weight,height):
        self.weight = float(weight)
        self.height = float(height)
        print("Weight in Kgs: ",self.weight)
        print("Weight in meters ",self.height)
        print("Weight in grams: ",self.weight * 1000)
        print("Weight in lbs: ",math.trunc(self.weight * 2.20462),2)
        print("Height in centimeters ",self.height * 100)

class calc_bmi(converter):
    def bmi_cal(self,weight,height):
        self.weight = float(weight)
        self.height = float(height)          
        self.bmi = float(self.weight / (self.height)**2) # kg/m**2
        print("BMI index: ",math.trunc(self.bmi),2)
        if self.bmi < 18.5:
            print("UnderWeight")
        elif self.bmi == 18.5 and self.bmi < 25.0:
            print("Healthy")    
        elif self.bmi == 25.0 and self.bmi < 30.0:
            print("Overweight")    
        elif self.bmi > 30.0:
            print("Obese")    
    

c = calc_bmi()
c.kgs_gms_lbs(100,1.80)
c.bmi_cal(100,1.80)

c.kgs_gms_lbs(60,1.65)
c.bmi_cal(60,1.65)

c.kgs_gms_lbs(20,1.50)
c.bmi_cal(20,1.50)

