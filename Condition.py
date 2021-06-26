price = 100000
good_credit = False


if good_credit:
    downpayment = 0.1*price
else:
    downpayment = 0.2*price

print(f"Down payment = {downpayment} and price is {price}")

name = "H"
print(len(name))

if len(name) < 3:
    print("Too short")
elif len(name) > 50:
    print("Too long")
else:
    print("Perfect")



weight = int(input('Enter you weight : '))
unit = input('(L)bs or (K)gs : ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Your weight is {converted} kgs")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"Your weight is {converted} lbs")

height = int(input('Enter your Cms : '))
unit = input('(I)ns or (F)eet : ')
if unit.upper() == 'I':
    converted = height / 2.54
    print(f"Your height in inches is {converted} inches")
elif unit.upper() == 'F':
    converted = height / 30.48
    print(f"Your height in feet is {converted} feet")