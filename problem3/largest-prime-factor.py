import argparse
import logging

parser = argparse.ArgumentParser(description='Will find the largest prime factor of the number provided.')
parser.add_argument("-log", "--log", default="warning", help=("Provide logging level. "
        "Example --log debug', default='warning'"))
parser.add_argument('startingNumber', metavar='startingNumber', type=int, nargs='?', 
                    help='an integer to get the prime factor for')
args = parser.parse_args()

# set your logging level, take argument from user to define what level, otherwise it will default to warn
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(args.log.lower())
logging.basicConfig(level=level)

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

'''
# ------------------------- WHAT DO WE NEED TO DO
# How to find factors of a number
	a factor is a number that divides another number evenly, that is with no remainder
		Find all the numbers less than or equal to the given number.
		Divide the given number by each of the numbers.
		The divisors that give the remainder to be 0 are the factors of the number.
			a good test case could be 81
# How to find only prime factors of a number
	Prime factors are factors of a number that are, themselves, prime numbers
# Find largest number in an array
	python might be able to find largest in array - better than sorting the array and then getting last index
	might be worth doing both just for practise
'''

# ------------------------- THE INITIAL SOLUTION

if not args.startingNumber:
        print('Missing arguments, for correct usage see -h or --help',
                'Logging can be enabled, for correct usage see -log or --log')
        exit()

testNumber = args.startingNumber

'''
def getFactorList(testNumber): 
	factorList = []
	for x in range(2,testNumber):
		logging.debug('testing number %s', x)
		if testNumber % x == 0:
			logging.debug('%s is a factor of %s', x, testNumber)
			factorList.append(x)
	# print('factors of ', testNumber, ' are ', factorList)
	# print('largest number in array ', max(factorList))
	return factorList


print('factors of ', args.startingNumber, ' are ', getFactorList(args.startingNumber))

for x in getFactorList(args.startingNumber):
	if len(getFactorList(x)) == 0:
		logging.debug('%s is a PRIME FACTOR', x)
		print('PRIME FACTOR: ', x)

ABOVE IS AN INEFFICIENT SOLUTION 
	bad news is that while this method works it is highly inefficient looping through nearly all numbers twice.
	as we are only needing to find the highest prime factor, why not start at the other end and work backwards?
	when we find the first prime factor, then that is our answer

# apparently this solution still isnt efficient enough as it gets killed by the terminal when trying to run for larger numbers
# for x in range(2, testNumber):
for x in reversed(range(2, testNumber)):
	factorList = []
	if testNumber % x == 0:
		logging.debug('%s is a factor', x)
		for y in range(2, x):
			if x % y == 0:
				factorList.append(y)
		if len(factorList) == 0:
			logging.debug('%s is a PRIME FACTOR', x)
			exit()


# single line that finds all factors of a given testNumber
# print[x for x in range(1,testNumber+1) if testNumber % x == 0]

# turns out that python uses a tonne of memory to store even just an integer!!!


	https://pythonspeed.com/articles/python-integers-memory/

	one would hope Python would store those million integers in no more than ~8MB: a million 8-byte objects.

	In fact, Python uses more like 35MB of RAM to store these numbers. Why? Because Python integers are objects,
	and objects have a lot of memory overhead.

	SWITCH TO NUMPY
	



# print[x for x in range(1,testNumber+1) if testNumber % x == 0]

# using np.arange(start, stop, step)
np.arange(1, testNumber, 1)

sumOfAll = 0
for x in np.arange(testNumber):
	sumOfAll += x
print sumOfAll

 	turns out that the solution comes out quite quickly for this one and is the fourth prime factor....
	so not as much computational power required as i thought...
	HOWEVER - this has exposed how memory hungry python is and that there needs to be made an efficient
		way of doing anything in python

'''

# didn't know the highest factor could not be greater than the square root of the number 

# ---------------------- BEST SOLUTION FROM INTERNET

# use of while loop instead of for loop must be a huge memory saving as there is nothing being stored

number = testNumber 
divisor = 1 
loopCounter = 0
while number > 1:
	logging.debug('%s %s', number, divisor)
	divisor += 1
    	while number%divisor == 0:          
        	logging.debug("factor = %s", divisor)
        	number = number//divisor
print("largest factor = ", divisor)


