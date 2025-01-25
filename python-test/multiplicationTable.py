def table(n,tableRange):
    for i in range(1,tableRange+1):
        print(n,"*",i,"=",n*i)
        
        
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    tableRange = int(input("Enter the range of the table: "))
    table(n,tableRange)