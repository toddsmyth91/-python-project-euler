'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


# initial solution taken from Problem7 where we needed to find prime number in sequence
import argparse
from math import sqrt


parser = argparse.ArgumentParser(description='Will find the prime number in sequence for number provided.')
parser.add_argument('primeToFind', metavar='primeToFind', type=int, nargs='?', 
                    help='an integer for the prime number to find')
args = parser.parse_args()

if not args.primeToFind:
      print('Missing arguments, for correct usage see -h or --help')
      exit()
def isPrimeNumber(primeToFind):
	for x in range(2, int(sqrt(primeToFind))+1):
		if primeToFind % x == 0:
			return False
	return True

# get the x prime number in sequence
sequenceNumber, primeCount, primeNumber, totalOfPrimes = 1, 0, 0, 0
while primeCount <= args.primeToFind:
	if isPrimeNumber(sequenceNumber):
#		print(sequenceNumber, ' is prime ', primeCount)
		primeCount += 1
		primeNumber = sequenceNumber
		totalOfPrimes += primeNumber
	sequenceNumber += 1
print('sum of ', args.primeToFind, ' prime numbers is ', totalOfPrimes)
