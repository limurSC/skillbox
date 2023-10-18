s = input()
checker = True
result = ""
if len(s) % 2 == 0:
    for i in s:
        if s.count(i) % 2 == 1:
            checker = False
            break
if len(s) % 2 == 1:
    countCheck = 0
    for i in s:
        if s.count(i) % 2 == 1:
            countCheck += 1
            result += i
        if countCheck > 1:
            checker = False
            break
if checker:
    for i in set(s):
        result += i * (s.count(i) // 2)
    if len(s) % 2 == 1:
        result = result[::-1] + result[1::]
    if len(s) % 2 == 0:
        result += result[::-1]
    print(result)