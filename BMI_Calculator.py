height = input("Enter your heigth in m:  ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
bmi_int = int(bmi)
print(f"Your height is {height} m, your weight is {weight} kg and Your BMI score is {bmi_int} .")
