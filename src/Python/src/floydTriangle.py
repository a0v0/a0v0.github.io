# Program to print floyd's triangle of n rows
n = int(input("Enter number of rows: "))
k = 1
for i in range(n):
    for j in range(0, i + 1):
        print(k, end=" ")
        k += 1
    print()
