def sum(num_list):
    res = 0
    for i in num_list:
        res+= i
    return res

if __name__ == "__main__":
    numbers = input("Enter the numbers separated by space:")
    num_list = list(map(int,numbers.split(" ")))
    print(list(num_list))
    print(sum(num_list))
    
