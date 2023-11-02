def armstrongCheck(num):
    lenNum = len(str(num))
    return num == sum(int(digit) ** lenNum for digit in str(num))


def armstrongGenerator():
    num = 10
    while True:
        if armstrongCheck(num):
            yield num
        num += 1


generator = armstrongGenerator()


def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
