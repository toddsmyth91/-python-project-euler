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
'''

numOfDigits = 2
largestNumDigitNum = 10**numOfDigits-1
ceilingNumber = str(largestNumDigitNum**2)

ceilingNumber = str(9009)
# while ceilingNumber > 0:
#	if 
print(ceilingNumber)
print(ceilingNumber[0], ceilingNumber[len(ceilingNumber)-1])
print(ceilingNumber[0] == ceilingNumber[len(ceilingNumber)-1])
