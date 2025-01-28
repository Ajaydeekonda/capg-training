def get_input():
    a=int(input("a value is:"))
    b=int(input("b value is:"))
    c=int(input("c value is:"))

    if a>b and a>c :
        print("a is bigger")
        return a 
    elif b>c:
        print("b is bigger")
        return b
    else:
        print("c is bigger")
        return c
def display(number):
    print(f"The biggest number is {number}")
    
def main():
    number=get_input()
    display(number)
main()