print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower = name1.lower()
name2_lower = name2.lower()
t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")
true = t + r + u + e
l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")
e2 = name1_lower.count("e") + name2_lower.count("e")
love = l + o + v + e2
print(f"True is {true}.")
print(f"Love is {love}.")
loveScore = str(true) + str(love)
if int(loveScore) <= 10 or int(loveScore) >= 90:
    loveStatus = ("you go together like coke and mentos")
elif int(loveScore) >= 40 and int(loveScore) <=50:
    loveStatus = ("you are alright together")
else:
    loveStatus = ("meh")
print(f"Your score is {loveScore}, {loveStatus}.")
