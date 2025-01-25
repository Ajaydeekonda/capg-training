def pattern(n, patterntype):
    if patterntype == 'straight':
        for i in range(n):
            print("*" * (i + 1))
    elif patterntype == "reverse":
        for i in range(n):
            print("*" * (n - i))
            
if __name__ == "__main__":
    n = int(input("Enter the n value:"))
    patterntype = input("Enter the pattern type (straight/reverse):")
    pattern(n, patterntype)
    