s = list(map(int, input().split()))
check = set(s)
if len(check) == 1:
    print("Все числа равны")
elif len(check) == len(s):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")