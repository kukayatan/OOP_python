

# methods of index bmi and whr calculations 

class Calculation:
    
    def __init__(self, x=0):
        self.x = x
  
       
    def bmi(self,weight, heigh):
        self.weight = weight
        self.heigh = heigh
        ws = "Weight Status"
        bmi_res = round(weight / ( (heigh/100) ** 2 ),1)
        if bmi_res < 18.5:
            return str("{} : Underweight \nYour BMI index is {} points".format(ws,bmi_res))
        elif bmi_res > 18.5 and bmi_res < 24.9:
            return str("{} : Normal \nYour BMI index is {} points".format(ws,bmi_res))
        elif bmi_res > 25 and bmi_res < 29.9:
            return str("{} : Overweight \nYour BMI index is {} points".format(ws,bmi_res))
        else:
            return str("{} : Obese \nYour BMI index is {} points".format(ws,bmi_res))
        
    def whr(self,waist, hip, gender):
        self.waist = waist
        self.hip = hip
        self.gender = gender
        ws = "Waist-to-Hip Ratio"
        whr_res = round(waist / hip,1)
        if gender == "male":
            if whr_res < 0.95:
                return str("{} : Low healt risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
            elif whr_res > 0.96 and whr_res < 1:
                return str("{} : Moderate risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
            else:
                return str("{} : High risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
        elif gender == "female":
            if whr_res < 0.80:
                return str("{} : Low healt risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
            elif whr_res > 0.81 and whr_res < 0.84:
                return str("{} : Moderate risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
            else:
                return str("{} : High risk \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))
        else: pass

# call function to ask for input that is needed for bmi calculations 

def ask_for_bmi():
    
    while True:
        try:
            weight = int(input("Please provide weight in kg:"))
            height = int(input("Please provide height in cm:"))            
        except:
            print("You did not put in correct numbers !")
            continue
        else:
            test = Calculation()
            result = test.bmi(weight,height)
            print(result)
            break



# call function to ask for input that is needed for whr calculations 
            
def ask_for_whr():
    
    while True:
        try:
            waist = int(input("Waist measurement in cm :"))
            hip = int(input("Hip measurement in cm :"))
            gender = str(input("Are you male/female ? "))           
        except:
            print("You did not put in correct infos !")
            continue
        else:
            test = Calculation()
            result = test.whr(waist, hip, gender)
            print(result)
            break

