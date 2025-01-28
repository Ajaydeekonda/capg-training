s1 = set()
s2 = {"apple", "banana", "cherry", "date", "fig"}
s3 = {"cherry", "date", "fig", "grape", "honeydew"}

s2.add("mango")
print(s2)
s2.remove("banana")
print(s2)

print(s1.union(s2)) # s1 | s2
print(s2.intersection(s3)) #s2 & s3
print(s3-s2) # s3.difference(s2)
