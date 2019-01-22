


# app that ask user for inputs to calculate either bmi or whr indexes 


from body_index import *
while True:
    
    try:
        print("Welcome in body index calculator \nInput number 1 for BMI index \nInput number2 for WHR index")
        choice = int(input("Input what index you want to measure:"))
        if choice == 1:
            ask_for_bmi()
            repeat = str(input("Do you want to repeat ?"))
        elif choice == 2:
            ask_for_whr()
            repeat = str(input("Do you want to repeat ?"))
        else:
            repeat = str(input("You put in wrong number. Do you want to repeat ?"))
    except:
        print("You did not put in correct answer !!")
    else:
        if repeat.lower() != "y":
            print("You have finished the app !")
            break
    

