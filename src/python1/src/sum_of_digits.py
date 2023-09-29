# Write a program to print sum of digits of a number

n = int(input("Enter number: "))
s = 0

for i in str(n):
    s += int(i)

print(s)
