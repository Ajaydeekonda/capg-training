def display_area(area):
    print(f"the area is {area}")
def get_input():
    length=int(input())
    width=int(input())
    return (length,width)
def area_rectangle_(length,width):
    return length*width
def main():
    (length, width)=get_input()
    area=area_rectangle_(length,width)
    display_area(area)
main()