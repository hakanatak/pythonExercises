height = input("Enter your heigth in m:  ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print("Your BMI is ", bmi_int)
               
