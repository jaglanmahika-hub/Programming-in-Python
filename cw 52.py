numbers = [5, 2, 9, 1, 7]

numbers.append(10)
numbers.insert(2, 15)
numbers.extend([20, 25])
print("After append, insert, extend:", numbers)

print("Count of 2:", numbers.count(2))

numbers.remove(15)
numbers.pop()
print("After remove and pop:", numbers)

numbers.sort()
print("Sorted List:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
