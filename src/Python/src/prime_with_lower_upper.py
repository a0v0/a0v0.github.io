# Take two integers x and y. Treat x and y as lower and upper limit and print prime numbers between x and y.
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for i in range(lower, upper):
    if isPrime(i):
        print(i)
