print("Welcome to Python Pizza Delivery!")
size = input("What size pizza do you want? S for small, M for medium, L for large. ")
add_pepperoni = input("Do you want pepperoni? Y for yes and N for no. ")
extra_cheese = input("Do you want extra cheese? Y for yes and N for no. ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("I don't understand!")
if bill != 0 and add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3
    else:
        print("I don't understan.")
elif add_pepperoni == "N":
    bill = bill
else:
    print("I don't Understan.")
if extra_cheese == "Y":
    bill += 1
elif extra_cheese == "N":
    print("Thank you for your order.")
print(f"You bill is ${bill}.")