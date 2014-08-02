"""
Challenge 
Given an unsorted list of integers, output the integers in order.

Input Format 
There will be two lines of input:
n - the size of the list
ar - n space separated numbers that belong to the list

Output Format 
Output all the numbers of the list in-order.

"""
n = raw_input()
numbers = [i for i in raw_input().split()]
out = ""

for number in range(0,100):
	for inNum in numbers:
		if number == int(inNum):
			out += str(number) + " "

print out