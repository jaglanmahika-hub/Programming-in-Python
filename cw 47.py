main_string = input("Enter the main string: ")
sub_string = input("Enter the substring: ")

count = 0

for i in range(0, len(main_string) - len(sub_string) + 1):
    match = 1
    for j in range(0, len(sub_string)):
        if main_string[i + j] != sub_string[j]:
            match = 0
            break
    if match == 1:
        count += 1

print(count)
