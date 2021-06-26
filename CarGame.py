command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started, ready to go !!")
    elif command == "stop":
        print("Car is gonna stop")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand")
        break
