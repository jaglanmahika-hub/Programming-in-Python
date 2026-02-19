def modify_list(lst):
    lst.append(100)
    print("Inside Function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)

print("Outside Function:", my_list)
