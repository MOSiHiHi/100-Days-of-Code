# The code written by me:

weight = input("Type your weight in kg: ")
height = input("Type your height in m: ")
weight = float(weight)
height = float(height)
bmi = weight/height**2
bmi = int(bmi)
print(bmi)

# The code written by the author:

weight = input("Type your weight in kg: ")
height = input("Type your height in m: ")
bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

# My code after I watched the author's code.

weight = input("Type your weight in kg: ")
height = input("Type your height in m: ")
bmi = int(weight)/float(height)**2
bmi = int(bmi)
print(bmi)
