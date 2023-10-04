s = input()
result = ""
for i in s:
    if i == '.':
        print(result)
        result = ""
    else:
        result += i
print(result)