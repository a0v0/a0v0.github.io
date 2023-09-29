# program to print sum of first n positive numbers

n = int(input("Enter upper limit: "))

s = 0

for i in range(n + 1):
    s += i

print(s)
