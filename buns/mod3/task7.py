s = list(map(int, input().split()))
result = len(s) != len(set(s))
print(result)