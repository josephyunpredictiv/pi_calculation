import math
import mpmath

getcontext().prec = 100
mpmath.mp.dps = 100

value=0
totalValue=0
for n in range(99999):
	value=4*((pow(-1,n))/(2*n+1))
	totalValue=totalValue+value
#	print(value)
print("%.16f"%totalValue)

