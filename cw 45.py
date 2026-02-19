num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

if num <= 1:
    print("Number is Non-Prime")
else:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Number is Prime")
    else:
        print("Number is Non-Prime")
