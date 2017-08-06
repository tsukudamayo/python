import sys
from collections import Counter

a = Counter(sys.argv[1])
b = Counter(sys.argv[2])

print(a)
print(b)

print("elments()")
print(list(a.elements()))
print(list(b.elements()))

print("most_commons()")
print(a.most_common())
print(b.most_common())

print("subtract()")
print(a.subtract(b))

print(" a + b ")
print( a + b )

print(" a - b ")
print( a - b )

print(" a & b ")
print( a & b )

print(" a | b ")
print( a | b )


