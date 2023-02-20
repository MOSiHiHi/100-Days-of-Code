# My code

print("Welcome to the tip calculator.")
totalBill = int(input("how much was the total bill? "))
tip = round(int(input("What percentage tip would you like to give? "))/100)
people = int(input("How many people to split the bill? "))
payforperson = round((totalBill/people) * (1.00 + tip), 2)
print(payforperson)

# The author' code

print("Welcome to the tip calculator.")
bill = float(input("how much was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {bill_per_person}$")

# My code improved

print("Welcome to the tip calculator.")
bill = int(input("how much was the total bill? "))
tip = round(int(input("What percentage tip would you like to give? "))/100)
people = int(input("How many people to split the bill? "))
payforperson = round((bill/people) * (1.00 + tip), 2)
payforperson = "{:.2f}".format(payforperson)
print(payforperson)

