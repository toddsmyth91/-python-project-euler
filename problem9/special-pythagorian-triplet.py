'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

'''
	MOST COMMON TRIPLETS
	[3, 4, 5]
	[5, 12, 13]
	[8, 15, 17]
	[7, 24, 25]

	Fib style progresion a, b, c, d so that a+b = c, b+c = d [ a, b, a+b, a+b+b ]
	- legs of triangle are 2bc and ad
	- hypotenuse is b^2 + c^2 = d^2 - 2 b c = a^2 + 2bc
	- perimeter is 2 c d
'''
# ------------------- WHAT DO WE NEED TO DO?
# evaluate pythag statement - a**2 + b**2 = c**2

# example - 3^2 + 4^2 = 5^2 - 9 + 16 + 25 = 50
#	3 + 4 + 5 = 12
#		3 + 4 = (12 - 5)
#		3 + 4 = 7
#	3 * 4 * 5 = 60

# -------------------- MY SOLUTION
'''
	Amazing online resource: https://r-knott.surrey.ac.uk/Pythag/pythag.html
	I want to put in an explanation for this one - using the Fibonnaci style method for calculating triplets
	Firstly we are provided the perimeter of our triangle which will have a pythag triplet

	Fibonnaci Sequence = [A, B, C, D]

	P = 12, 56, 1000 == 2 x C x D

	From this perimeter we can find factors of the resulting number, which become potentialC and potentialD
	
	We know that for Fibonnaci:
		D == B + C or B + (B + A)
		C == B + A
			For our eventual triangle the sides can be calculated:
			first leg = 2 x B x C
			second leg = A x D
	
	Therefore once we have a potential C and D we can calculate potential A and B

		A = C - B
		B = D - C
		C = A + B
		D = A + B + B

	Then to complete the check for pythagorean triplet
		first leg^2 + second leg^2 == h^2 == B^2 + C^2
'''	

import time

def getPythagoreanTripletProduct(perimeter):
	loopCounter = 0
	startNum = perimeter / 2
	# now need to find factors where startNum = c * d && 2cd == perimeter
	for divisor in range(1, startNum + 1):
		loopCounter += 1
#		print loopCounter
		if startNum % divisor == 0:
			if startNum/divisor * divisor * 2 == perimeter and startNum/divisor < divisor:
				potentialC, potentialD = startNum/divisor, divisor
				potentialB = potentialD - potentialC
				if potentialB > 0 and potentialC - potentialB > 0:
					potentialA = potentialC - potentialB
#					print('%s %s %s %s', potentialA, potentialB, potentialC, potentialD)
					firstLeg = potentialB * potentialC * 2
					secondLeg = potentialA * potentialD
#					print(firstLeg, ' ', secondLeg, ' ', (potentialB**2 + potentialC**2))
					if (firstLeg**2 + secondLeg**2) == (potentialB**2 + potentialC**2)**2:
#						print('found pythagorean triplet')
						return firstLeg * secondLeg * (potentialB**2 + potentialC**2)
	return 0	


start = time.time()
#print getPythagoreanTripletProduct(12) 
#print getPythagoreanTripletProduct(56)
print getPythagoreanTripletProduct(1000)
end = time.time()
print(end - start)

# -------------------- BEST ONLINE SOLUTION
# testing with a loop counter we can see that this is still quite a bit of looping in comparison to my solution
# after testing with the timing functions we can see that my execution is significantly faster

start = time.time()
loopCounter = 0
for a in range(1, 499):
    for b in range(a+1, 499):
	loopCounter += 1
#	print loopCounter
        c = 1000-a-b
        if((a**2)+(b**2)==(c**2)):
            print(a*b*c)

end = time.time()
print(end - start)


'''
Since c must be larger than both a and b, a+b must be less than 500 and both a, b must be less than 500, so that let me limit the for-loop bounds. I also don't need a for-loop for c since it is determined by a, b, and the constant 1000.

This took 169ms to run on my computer.
'''
