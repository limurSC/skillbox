s = input()
result = ""
answer = False
for i in s:
    if i != ' ':
        if i in result:
            answer = True
            break
        result += i
print(answer)