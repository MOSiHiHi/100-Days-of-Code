import random

namesString = input("Give me everybody's names, seperated by a comma and space (\", \").\n")
names = namesString.split(", ")
namesLen = len(names) - 1
randomPicker = random.randint(0, namesLen)
billPayer = names[randomPicker]
print(f"{billPayer} will pay for the bill.")