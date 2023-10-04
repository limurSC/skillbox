s = input()
lastChar = s[-1]
str = s[:-2]
result = 0
for i in s:
    if i == lastChar:
        result += 1
    else:
        break
print(result)