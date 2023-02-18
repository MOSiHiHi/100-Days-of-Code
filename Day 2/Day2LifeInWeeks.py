# My code

age = input("What is your current age? ")
yearsLeft = 90 - int(age)
day = yearsLeft * 365
week = yearsLeft * 52
month = yearsLeft * 12
print(f"You have {yearsLeft} years or {day} days, {week} weeks, and {month} months left.")

# Author's code

age = input("What is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
massage = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(massage)

# My code
# I see no way to improve...
