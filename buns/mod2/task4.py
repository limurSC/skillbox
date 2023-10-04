def CheckNaturalNum(num):
    if num % 1 == 0 and num > 0:
        return True
    return "Неверный ввод"

def Bin(num):
    result = ""
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]

def Octal(num):
    result = ""
    while num > 0:
        result += str(num % 8)
        num //= 8
    return result[::-1]

def Hexadecimal(num):
    result = ""
    while num > 0:
        if(num % 16 < 10):
            result += str(num % 16)
        else:
            result += chr(65 + num % 16 - 10)
        num //= 16
    return result[::-1]

startNum = float(input())
if CheckNaturalNum(startNum):
    startNum = int(startNum)
    print(f"{Bin(startNum)}, {Octal(startNum)}, {Hexadecimal(startNum)}")