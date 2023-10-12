s = input()
k = len(s)
matrix = list()
matrix.append(s)
for i in range(k - 1):
    matrix.append(input())
result = "Ничья"

for i in range(k):
    checkChar = matrix[i][i]
    linСhecker = True
    columnСhecker = True
    for j in range(k):
        if checkChar != matrix[i][j]:
            linСhecker = False
        if checkChar != matrix[j][i]:
            columnСhecker = False
    if linСhecker or columnСhecker:
        result = checkChar
        break

if result == "Ничья":
    checkFirstChar = matrix[0][0]
    checkSecondChar = matrix[0][-1]
    firstСhecker = True
    secondСhecker = True
    for i in range(k):
        if checkFirstChar != matrix[i][i]:
            firstСhecker = False
        if checkSecondChar != matrix[i][-1 - i]:
            secondСhecker = False
    if firstСhecker:
        result = checkFirstChar
    if secondСhecker:
        result = checkSecondChar

print(result)