# Program to check whether the given number is a vowel, consonant or alphabet


n = input("Enter number: ")


if not n.isalpha():
    print("Not an alphabet")
elif n.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
