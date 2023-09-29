# Program to print armstrong number

n = int(input("Enter number: "))


def isArmstrong(n):
    s = 0

    for i in str(n):
        s += int(i) ** 3

    if s == n:
        return True

    return False


if isArmstrong(n):
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
