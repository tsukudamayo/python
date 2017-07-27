x = 5.0

while(True):
    x2 = x - ( x*x - 2 ) / (x*2)
    print(x2)
    if abs( x2 - x ) < 0.00001:
        break
    x = x2

print(x2)

