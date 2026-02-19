list1 = [10, 20, 30, 40, 50]
list2 = list((1, 2, 3, 4, 5))
list3 = []

for i in range(1, 6):
    list3.append(i * 10)

print("Direct Display:", list1)

print("Display using loop:")
for item in list1:
    print(item)

print("Display using slicing:", list1[1:4])
