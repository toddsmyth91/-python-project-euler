'''

# ------------------ THINGS WE NEED TO DO
# find the largest palindromic number
#	cannot do this way as we dont know how many digits it is going to have...
#	we can find the largest possible number that could happen:
#		get the largest number with specified digits (eg 2 digit is 99, 3 digit is 999)
			multiply that number by itself - that is the ceiling of what the number could be
	work backwards from the largest number and find the first palindrome	
# find the factors for the palindromic number
#	both numbers must be of two digits / three digits

# while ceilingNumber > 0:
#	if 
print(ceilingNumber)
print(ceilingNumber[0], ceilingNumber[len(ceilingNumber)-1])
print(ceilingNumber[0] == ceilingNumber[len(ceilingNumber)-1])
x = 0
y = -1
while x < len(ceilingNumber):
	print(ceilingNumber[x], ceilingNumber[y])
	x += 1
	y -= 1

def isPalindrome(numberString):
	x, y = 0, -1
	while x < len(numberString):
		if numberString[x] != numberString[y]:
			return false
	return true

# print(isPalindrome('9009'))
# print(isPalindrome('9089'))
# print(ceilingNumber == ceilingNumber[::-1])
'''

# ------------------- MY CORRECT SOLUTION!!

# check if palindrome simply convert to string and check that forward and reverse are same
def returnPalindrome(ceilingNumber):
	palindromeFound = False
	while not palindromeFound:
		if str(ceilingNumber) == str(ceilingNumber)[::-1]:
			palindromeFound = True
			break
		ceilingNumber -= 1
	return ceilingNumber

numOfDigits = 2
numOfDigits = 3
largestNumDigitNum = 10**numOfDigits-1
print(largestNumDigitNum)
print(largestNumDigitNum//10)
ceilingNumber = largestNumDigitNum**2

# print(returnPalindrome(largestNumDigitNum**2))
while ceilingNumber > 0:
	ceilingNumber = returnPalindrome(ceilingNumber)
	print('palindrome: ', ceilingNumber)
	testFactor = largestNumDigitNum
	while testFactor > largestNumDigitNum//10:
	#	print('- ', testFactor)
		testResult = ceilingNumber//testFactor
		if len(str(testResult)) == numOfDigits and  ceilingNumber % testResult == 0:
			print(testFactor, ' x ', testResult, ' = ', ceilingNumber)
			ceilingNumber = 1
			break
		testFactor -= 1
	ceilingNumber -= 1

# ------------------- BEST ONLINE SOLUTION
# this solution uses a lot less storage
# - which is what python is horrible at being an extreme memory hog
c=0
for i in range(999,99,-1):

    for j in range(999,99,-1):
        a = i*j
        b= int(str(a)[::-1])
        if a==b and a>c:
            c = a

print(c)
