import math

def prime_or_not(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisors up to √n
        if n % i == 0:
            return False
    return True  # If no divisors, n is prime

def get_prime(a):
    print(f"Prime numbers up to {a}:")
    for i in range(2, a + 1):  # Start from 2, as 1 is not prime
        if prime_or_not(i):
            print(i, end=" ")
    print()  # New line for clean output

def get_inp():
    try:
        a = int(input("Enter a number: "))
        if a < 0:
            print("Please enter a positive number.")
            return get_inp()  # Recursively ask for valid input
        return a
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return get_inp()  # Recursively ask for valid input

def main():
    a = get_inp()
    get_prime(a)

main()
