'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# ------------------- WHAT DO WE NEED TO DO?
# check for division without remainder - MOD
# check that is evenly divisible - x//y % 2 == 0
# positive number x > 0
'''
#2520 - divided by 1 - 10 without remainder
smallestNumber = 10
while smallestNumber > 0:
	loopCount = 0
	for x in range(1,11):
		if smallestNumber % x != 0:
			smallestNumber += 10
			break
		loopCount += 1
	if loopCount == 10:
		print('2520 - ', smallestNumber)
		smallestNumber = 0
'''
# ------------------- MY SOLUTION
# smallest number - divided by 1 - 20 without remainder
# start with 20 as it is the largest divisor with remainder 0
smallestNumber = 20
while smallestNumber > 0:
	smallestNumberPass = True # flag to represent checking all divisors in rangee
	for x in range(1,21):
		if smallestNumber % x != 0:
			smallestNumber += 20 # must increment by largest divisor remainder 0
			smallestNumberPass = False
			break
	if smallestNumberPass:
		print('smallest number - ', smallestNumber)
		break
'''
I don't particularly like this solution - but it is certainly efficient
# ------------------- BEST ONLINE SOLUTION
def func(num):
    a = num
    while True:
        k = 0
        for i in range(1, num + 1):
            k += (a % i)
        if k == 0:
            print(a)
            break
        else:
            a += num
func(20)
'''
