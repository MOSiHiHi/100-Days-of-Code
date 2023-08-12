#My code:

weight = float(input("Type your weight in kg: "))
height = float(input("Type your height in m: "))
bmi = weight/height**2
bmi = float("{:.2f}".format(bmi))
print(f"Your BMI is {bmi}.")
if bmi < 18.5:
    print("You are underweight.")
elif bmi > 18.5 and bmi < 25:
    print("You have normal weight.")
elif bmi > 25 and bmi < 30:
    print("You are overweight.")
elif bmi > 30 and bmi < 35:
    print("You are obese.")
elif bmi > 35:
    print("You are clinically obese.")
else:
    print("Sorry, I don't know what to say!!")