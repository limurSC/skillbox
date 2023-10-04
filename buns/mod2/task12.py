s = input()
result = ""
checkChar = "-() "
for i in s:
    if not i in checkChar:
        result += i
print(result)