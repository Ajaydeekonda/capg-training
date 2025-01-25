def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"FizzBuzz")
        elif i % 3 == 0:
            print(i,"Fizz")
        else:
            print(i,"Buzz")
            
            
if __name__ == "__main__":
    FizzBuzz()