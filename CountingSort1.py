"""
Challenge 
Given a list of integers, can you count and output the number of times each value appears?

Hint: There is no need to sort the data, you just need to count it.

Input Format 
There will be two lines of input:

n - the size of the list
ar - n space separated numbers that makes up the list
Output Format 
Output the number of times every number from 0 to 99 (inclusive) appears in the list.
"""
n = raw_input()
numbers = [i for i in raw_input().split()]
out = ""

for number in range(0,100):
	count = 0
	for inNum in numbers:
		if number == int(inNum):
			count += 1
	out += str(count) + " "

print out