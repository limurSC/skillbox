def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

a = int(input())
b = int(input())
print(euclid(a, b))