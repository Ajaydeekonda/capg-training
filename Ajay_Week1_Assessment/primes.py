import math

def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(2, math.ceil(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

def primes(s,e):
    primes = []
    for num in range(s,e+1):
        if isprime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    s = int(input("Enter the start number:"))
    e = int(input("Enter the end number:"))
    print(primes(s,e))
        
    