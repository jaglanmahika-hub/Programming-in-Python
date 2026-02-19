print("Armstrong numbers from 1 to 1000:")

for num in range(1, 1000):
    temp = num
    sum = 0
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    if sum == num:
        print(num)
