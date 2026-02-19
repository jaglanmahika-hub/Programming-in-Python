string = input("Enter a string: ")

print("Forward Order:")
for i in range(0, len(string)):
    print(string[i])

print("Reverse Order:")
for i in range(len(string)-1, -1, -1):
    print(string[i])
