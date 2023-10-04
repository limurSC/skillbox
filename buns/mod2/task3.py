s = input()
firstNum = ""
secondNum = ""
thirdNum = ""
checkNum = 1
for i in s:
    if i == ' ':
        checkNum += 1
    elif checkNum == 1:
        firstNum += i
    elif checkNum == 2:
        secondNum += i
    elif checkNum == 3:
        thirdNum += i
firstNum, secondNum, thirdNum = int(firstNum), int(secondNum), int(thirdNum)
if secondNum < firstNum < thirdNum or secondNum > firstNum > thirdNum:
    print(firstNum)
if firstNum < secondNum < thirdNum or firstNum > secondNum > thirdNum:
    print(secondNum)
if firstNum < thirdNum < secondNum or firstNum > thirdNum > secondNum:
    print(thirdNum)