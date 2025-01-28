def smallest_largest_prime(low, high):
    smallest = None
    for num in range(low, high + 1):
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            smallest = num
            break

    largest = None
    for num in range(high, low - 1, -1):
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            largest = num
            break

    return smallest, largest

def main():
    while True:
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        if low >= 0 and high >= 0 and low < high:
            break

    smallest, largest = smallest_largest_prime(low, high)
    if smallest is None or largest is None:
        print("No prime numbers found in the range.")
    else:
        print(f"Smallest prime: {smallest}, Largest prime: {largest}")

main()
