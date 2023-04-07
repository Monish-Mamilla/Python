"""
Author: Monish Mamilla
Program Name: Prime Under X
Date: 3/1/23
Version 2.0
"""
def isPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
num = int(input("Enter an integer >= 2: "))
# user will have to enter an integer >= 2
if num >= 2:
    primes = ""
    for x in range(2, num+1):
        if isPrime(x):
            primes += str(x) + " "
# it will determine all prime numbers less than what the user entered
    print("Prime numbers less than or equal to", num,":", primes)
else:
    print("Invalid input")
