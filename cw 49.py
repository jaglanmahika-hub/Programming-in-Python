string = input("Enter a string: ")

result = ""

for ch in string:
    if ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

visited = ""

for i in range(0, len(result)):
    if result[i] not in visited and result[i].isalpha():
        count = 0
        for j in range(0, len(result)):
            if result[i] == result[j]:
                count += 1
        print(str(count) + result[i])
        visited += result[i]
