from decimal import Decimal, getcontext
runs=100
import math
import mpmath


getcontext().prec = 200
mpmath.mp.dps = 200

value=0
totalValue=0
for n in range(runs):
	value=mpmath.mpf(4*(mpmath.mpf(pow(-1,n))/mpmath.mpf(2*n+1)))
	totalValue=mpmath.mpf(totalValue)+mpmath.mpf(value)
	print("n="+str(n)+": "+str(value))


pi3=totalValue
print("pi: "+str(pi3))
pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
error=abs(pi3-pi)
print("error: "+str(error))


