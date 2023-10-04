s = input()
char = ""
num = ""
checkNum = False
for i in s:
    if i == ',':
        checkNum = True
    elif not checkNum:
        char = i
    elif checkNum:
        num += i
num = int(num)
print(chr((ord(char) - 97 + num) % 26 + 97))