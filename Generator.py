#Key generator
import random
from Primes import *

def generator():
	return random.sample(primes,2)

def primeFactors(n):
	factors = []
	d = 2
	step = 1
	while d*d <= n:
		while n>1:
			while n%d == 0:
				factors.append(d)
				n = n/d
			d += step
			step = 2
	return factors

#following function is from
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y,u,v = 0,1,1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return y


a = generator()
m = a[0] * a[1]
phi = (a[0] - 1) * (a[1] - 1)
b = primeFactors(phi)
c = random.sample(b,1)

print "Private Key:"
print "p = " + str(a[0])
print "q = " + str(a[1])
print "k inverse = " + str(egcd(phi,17)) + "\n"

print "Public Key:"
print "m" + " = " + str(m)
print "k = 17"
