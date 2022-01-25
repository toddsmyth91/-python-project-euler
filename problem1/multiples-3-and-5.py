'''	PROBLEM #1
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
	The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.

	BEST SOLUTION FOUND:
		print(sum([i for i in range(1,1000) if i%3==0 or i%5==0]))
'''

# --------------------- NOTES - python 3.10.2
# --------------------- NUMBERS

# booleans are a subtype of integers
# integers have unlimited precision
# floating point numbers usually implemented using double in C
# complex numbers have a real and imaginary part - which are each a floating point number - (z.real, z.imag)

# CONSTRUCTORS
#	int(), float(), complex()

# --------------------- ITERATORS

# building blocks inspired by constructs from APL, Haskell, and SML

''' infinite iterators
	count(), cycle(), repeat()
		count(start, [step])
			count(10) --> 10 11 12 13 14 ... || count(10+2) --> 10 12 14 16 18 ...	
		cycle(p)
			cycle('ABCD') --> A B C D A B C D ...
		repeat(elem, [,n])
			repeat(10,3) -- > 10 10 10
'''

''' terminating interators
	there is lots...
'''

# ---------------------- WRITING THE SOLUTION

# need to check if number is multiple of 3 or 5 (use mod == 0) --> x % y
# iterate from 0 to an ending number -- > for x in y
# create array of numbers from 0 to N --> range(start, stop) --> range(0, 10)
# range returns a range object with numbers from start to stop, must convert to list --> list(range(x, y))
# check that mod returns 0 --> operator.is_(a, b)

'''testingRange = list(range(0,11))
for x in testingRange:
	print(x)
'''

'''sumOfMultiples = 0
# for y in range(1,10):
for y in range(1,1000):
	if y % 3 == 0 or y % 5 == 0:
		sumOfMultiples += y
print'answer to problem: ', sumOfMultiples
'''

# --------------------- ALLOW FOR PARSING IN OF RANGE
import argparse

parser = argparse.ArgumentParser(description='Will find the sum of all the multiples of 3 or 5 in range provided.')
parser.add_argument('startRange', metavar='startRange', type=int, nargs='?', 
                    help='an integer for the beginning of the range')
parser.add_argument('endRange', metavar='endRange', type=int, nargs='?', 
                    help='an integer for the end of the range')
args = parser.parse_args()

if not args.startRange and not args.endRange:
	print'Missing arguments, for correct usage see -h or --help'
	exit()

print'start range:',args.startRange
print'end range:', args.endRange

sumOfMultiples = 0
for z in range(args.startRange, args.endRange):
	if z % 3 == 0 or z % 5 == 0:
		sumOfMultiples += z
print'sum of multiples:', sumOfMultiples

# BEST SOLUTION FOUND: print(sum([i for i in range(1,1000) if i%3==0 or i%5==0]))
