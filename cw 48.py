first = input("Enter First Name: ")
middle = input("Enter Middle Name: ")
last = input("Enter Last Name: ")

capital_last = last[0].upper() + last[1:]

print(first[0].upper() + "." + middle[0].upper() + ". " + capital_last)
