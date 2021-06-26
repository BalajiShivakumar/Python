secret = 9
i = 0
tries = 3
while i < tries:
    number = int(input("Enter the number : "))
    i = i+1
    if number == secret:
        print("Correct ! You won...")
        break
else:
    print("Better luck next time")