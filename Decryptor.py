#Decryptor
#Derek So
#Version 1.1
import sys

def mod(base,exponential,mod):
	ans = 1
	for i in range(0,exponential):
		ans = (ans * base) % mod
	return ans

def decrypt(textFile,modd,kInverse):
	lineList = []
	advList = []

	new = open(textFile)
	for line in new:
		lineList.append(line) 

	for x in lineList:
		copy = []
		a = 0
		b = 0
		while b != -1:
			b = x.find(" ",a)
			copy.append(int(x[a:b]))
			a = b + 1
		advList.append(copy)

	for x in advList:
		for y in range(len(x)):
			x[y] = chr(mod(x[y],kInverse,modd))

	return advList

stuff = decrypt(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
new = open("decrypted" + str(sys.argv[1]) , "w")
for x in stuff:
	new.write("".join(x))
new.close()
