# Print all even no's between 0,20
n = int(input("Enter a number: "))
for i in range(0, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
