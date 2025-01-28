def oddEvenSeparator(numbers):
    odd = []
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even


if __name__ == "__main__":
        numbersList = input("Enter the numbers separated by spaces: ")
        numbers = list(map(int, numbersList.split()))
        odd, even = oddEvenSeparator(numbers)
        print("Odd numbers:", odd)
        print("Even numbers:", even)
    
