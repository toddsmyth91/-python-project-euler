'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import argparse
from math import sqrt


parser = argparse.ArgumentParser(description='Will find the prime number in sequence for number provided.')
parser.add_argument('primeToFind', metavar='primeToFind', type=int, nargs='?', 
                    help='an integer for the prime number to find')
args = parser.parse_args()

if not args.primeToFind:
      print('Missing arguments, for correct usage see -h or --help')
      exit()

# --------------------- WHAT DO WE NEED TO DO?
# check if a number is prime
#	prime number can only be divided by 1 and itself
def isPrimeNumber(primeToFind):
	for x in range(2, int(sqrt(primeToFind))+1):
		if primeToFind % x == 0:
			return False
	return True

# get the x prime number in sequence
sequenceNumber, primeCount, primeNumber = 1, 0, 0
while primeCount <= args.primeToFind:
	if isPrimeNumber(sequenceNumber):
		print(sequenceNumber, ' is prime')
		primeCount += 1
		primeNumber = sequenceNumber
	sequenceNumber += 1
print(args.primeToFind, ' prime number is ', sequenceNumber-1)
	 
