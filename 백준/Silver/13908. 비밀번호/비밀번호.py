import sys
from math import factorial

n, m = map(int, input().split())
if m > 0 :
    A = list(map(int, input().split()))
else :
    print(10**n)
    sys.exit()

a = 10**n
b = 0
for i in range(1, m + 1) :
    b += ((-1)**(i-1)) * ((10-i) ** n) * (factorial(m)//(factorial(i)*factorial(m-i)))

print(a - b)


