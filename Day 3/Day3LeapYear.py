year = int(input("Which year do you wanna cheack?! "))
if year % 4 == 0:
    if year % 100 != 0:
        print("This is a leap year.")
    elif year % 400 == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")
else:
    print("This is a not leap year.")

