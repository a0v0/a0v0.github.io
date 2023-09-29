# Program to print whether the number is strong number or not


def getFactorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def isStrong(s):
    sum1 = 0

    for x in str(s):
        sum1 += getFactorial(int(x))

    return sum1 == s


s = int(input("Enter a number: "))

if isStrong(s):
    print("yes, strong number")
else:
    print("no, not a strong number")
