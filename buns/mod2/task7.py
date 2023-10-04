s = input()
check = 0
for i in s:
    if i == '1':
        check += 1
    if i == '0':
        check -= 1
if check == 0:
    print("yes")
else:
    print("no")