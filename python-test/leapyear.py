def leapOrNot(year):
    if year % 4 == 0 and (year % 100 != 0):
        print(f"{year} is a Leap year")
    elif year % 400 == 0:
        print(f"{year} is a Leap year")
    else:
        print(f"{year} is not a Leap year")
    
    
if __name__ == "__main__":
    
    year = int(input("Enter a year: "))
    leapOrNot(year)
        