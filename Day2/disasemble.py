import dis
def get_inp():
    a=int(input("value of a :"))
    b=int(input("value of b :"))
    return a,b
def get_mul(a,b):
    a=2
    return a*b
def for_loop(n):
    for i in range(n):
        print(i)
def display(data):
    print(f"the multiplied no is {data}")

def main():
    (a,b)=get_inp()
    ans = get_mul(a,b)
    display(ans)
    for_loop(ans)
dis.dis(main)
main()

# # import dis
# # def add():
#     for i in range(5):
#         a=0
# dis.dis(add)    