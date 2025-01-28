def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return -1
    else:
        return num * factorial(num - 1)
    

if __name__ == "__main__":
    num = int(input("Enter the number:"))
    res = factorial(num)
    if(res < 0):
        print("Factorial of negative number doesn't exist")
    else:
        print("Factorial of",num,"is:",res)
    
    
        