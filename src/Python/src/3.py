# Write a program to print prime numbers from one to twenty

def printPrime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


printPrime(20)
