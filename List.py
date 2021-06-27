numbers = [1, 6, 3, 8, 5]
print(numbers)
numbers.pop(1)
print(numbers)

numbers.insert(1, 6)
print(numbers)

numbers.append(5)
print(numbers)

print(numbers.count(5))





numbers2 = numbers.copy()
numbers2.append("copy of the numbers")
print(numbers2)
print(numbers)