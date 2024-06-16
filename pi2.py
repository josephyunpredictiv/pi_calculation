from decimal import Decimal, getcontext
import math
import mpmath


getcontext().prec = 100
mpmath.mp.dps = 100

value=0
totalValue=0
for n in range(9999999):
	value=mpmath.mpf(4*(mpmath.mpf(pow(-1,n))/mpmath.mpf(2*n+1)))
	totalValue=mpmath.mpf(totalValue)+mpmath.mpf(value)
	print("n="+str(n)+": "+str(value))
print("pi~ "+"{0}".format(mpmath.mpf(totalValue)))

