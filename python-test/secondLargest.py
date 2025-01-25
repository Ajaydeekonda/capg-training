def secondLar(numbers):
    numbers.sort(reverse= True)
    return numbers[1]

if __name__ == "__main__":
    numbers = list(map(int,input("Enter the numbers:").split()))
    print(secondLar(numbers)) 