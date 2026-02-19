tuple1 = (10, 20, 30, 40, 50)
tuple2 = tuple([1, 2, 3, 4, 5])

print("Direct Display:", tuple1)

print("Display using loop:")
for item in tuple1:
    print(item)

print("Display using slicing:", tuple1[1:4])

tuple_clone = tuple1[:]
print("Cloned Tuple:", tuple_clone)

print("Count of 20:", tuple1.count(20))
print("Maximum:", max(tuple1))
print("Minimum:", min(tuple1))

