import dis


def display_avg(avg):
    print(f"the average of 4 nos is :{avg}")
    
def get_input():
    a=(input("a:"))
    b=(input("b:"))
    c=(input("c:"))
    d=(input("d:"))
    return (a,b,c,d)   

def get_sum(a,b,c,d):
    val=(int(a)+int(b)+int(c)+int(d))
    return val
def get_avg(val):
    avg=val/4
    return avg
def main():
    a, b, c, d=get_input()
    val=get_sum(a,b,c,d)
    avg=get_avg(val)
    display_avg(avg)
     
dis.dis(get_avg)
main()