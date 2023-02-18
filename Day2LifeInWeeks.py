age = input("What is your current age? ")
yearsLeft = 90 - int(age)
day = yearsLeft * 365
week = yearsLeft * 52
month = yearsLeft * 12
print(f"You have {yearsLeft} years or {day} days, {week} weeks, and {month} months left.")