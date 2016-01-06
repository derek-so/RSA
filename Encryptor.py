#RSA encryptor
#Derek So
#Version 1.1
import random
import sys
from Primes import *

def mod(base,exponential,mod):
  ans = 1
	for i in range(0,exponential):
		ans = (ans * base) % mod
	return ans

def encrypt(textFile,m,k):
	lineList = []
	encryptedList = []

	text = open(textFile)

	for line in text:
		lineList.append(line)

	for x in lineList:
		copy = []
		for y in x:
			d = ord(y)
			d = mod(d,k,m)
			copy.append(str(d))
		encryptedList.append(copy)
	return encryptedList

stuff = encrypt(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
new = open("encrypted" + str(sys.argv[1]) , "w")
for x in stuff:
	new.write(" ".join(x)+ "\n")
new.close()

