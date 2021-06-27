



phone = input("Phone : ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}
output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)