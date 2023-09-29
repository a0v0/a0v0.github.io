# Program to print palindrom


def isPalindrome(n):
    return n == n[::-1]


if isPalindrome(input("Enter string: ")):
    print("Yes, Palindrom")
else:
    print("No, Not a Palindrom")
