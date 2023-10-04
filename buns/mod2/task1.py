s = input()
firstNum = ""
secondNum = ""
checkNum = False
for i in s:
    if i == ',' or i == ' ':
        checkNum = True
    elif not checkNum:
        firstNum += i
    elif checkNum:
        secondNum += i
print(int(firstNum) % int(secondNum))