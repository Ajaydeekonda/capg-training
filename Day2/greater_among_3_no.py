def get_input():
    a=int(input("a value is:"))
    b=int(input("b value is:"))
    c=int(input("c value is:"))
    return(a,b,c)
def display(number):
    print(f"The biggest number is {number}")
def get_max(a,b,c):
    if a>b and a>c :
        return a
    elif b>c:
        return b
    else:
        return c
    
def main():
    a,b,c=get_input()
    number=get_max(a,b,c)
    display(number)
main()