'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# sum of squares of first 10 natural numbers
# print(sum([x**2 for x in range(1,11)]))

# square of sum of first 10 natural numbers
# print(sum(x for x in range(1,11))**2)

# difference between sum of squares and square of sum	
print(sum(x for x in range(1,11))**2 - sum([x**2 for x in range(1,11)]))

# difference between sum of squares and square of sum of first 100 numbers
print(sum(x for x in range(1,101))**2 - sum([x**2 for x in range(1,101)]))
