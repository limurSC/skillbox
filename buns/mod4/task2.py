def degree(a, n):
    if n < 0:
        return 1 / degree(a, -n)
    if n == 0:
        return 1
    elif n % 2 == 0:
        return degree(a * a, n // 2)
    else:
        return a * degree(a, n - 1)
a = int(input())
n = int(input())
print(degree(a, n))