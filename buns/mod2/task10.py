s = input()
result = ""
lastChar = ''
for i in s:
    if i == ' ':
        result += lastChar
    lastChar = i
result += s[-1]
print(result)