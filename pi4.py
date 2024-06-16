from decimal import Decimal, getcontext
errorVar=(1/100000000)
import math
import mpmath


getcontext().prec = 200
mpmath.mp.dps = 200

value=0
totalValue=0
n=0
pi3=totalValue
pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
error=abs(pi3-pi)

while error>errorVar:
        value=mpmath.mpf(4*(mpmath.mpf(pow(-1,n))/mpmath.mpf(2*n+1)))
        totalValue=mpmath.mpf(totalValue)+mpmath.mpf(value)
        print("n="+str(n)+": "+str(value))
        pi3=totalValue
        error=abs(pi3-pi)
        n+=1

print("-------------------------"*5)
print(errorVar)
pi3=totalValue
print("pi: "+str(pi3))
pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
error=abs(pi3-pi)
print("error: "+str(error))


