s = input()
result = ''.join(num for num in s if num.isdigit() or num == '+')
print(result)