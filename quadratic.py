import math
a = int(input("a value:"))
b = int(input("b value:"))
c = int(input("c value:"))

root1  = (-b + ((b ** 2) - 4*a*c)**0.5) / 2 * a 
root2  = (-b - math.sqrt((b ** 2) - 4*a*c))/ 2 * a 
print("Root 1: ", root1)
print("Root 2: ",root2)
