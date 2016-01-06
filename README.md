# RSA
Simple RSA encrypter and decrypter in python.

This repository contains several files that will perfrom RSA encryption on a .txt file.
-Primes.py， is a file containing a list of prime numbers used to generate the private and public key. Feel free to add to    this  list, but keep in mind that too big of prime numbers can cause problems with "int arithmetic."

-Generator.py, a script file that creates both the private and public for the user.

-Encryptor.py, a script file that encrypts a .txt file using the given public key. It outputs a .txt file with the name       "encrypted(original file name).txt". When running the script, the first argument is the file name. The second argument  is   the  modulus (commonly written as m) and the third argument is the exponent  (commonly written as k). Running this script    looks  something like...
 python Encryptor.py "filename" 3403(the modulus) 17(our exponent or "k")

-Decryptor.py, a script file that decrypts a .txt file encrypted using Encryptor.py. It outputs a .txt file with the name     "decrypted(encrypted file name).txt". When running the script, the first argument is the file name. The second argument  is  the  modulus (commonly written as m) and the third argument is the exponent (commonly written as k inverse). Running this    script looks  something like...
 python Decryptor.py "encrypted filename" 3403(the modulus) 193(our exponent or "k inverse")
