s = input()
firstNum = 0
secondNum = 0
for i in s[::2]:
    firstNum += int(i)
for i in s[1::2]:
    secondNum += int(i)
if firstNum + 3 * secondNum == 90:
    print("yes")
else:
    print("no")