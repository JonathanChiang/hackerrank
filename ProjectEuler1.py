"""
This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.
"""

n = int(raw_input())
testCases = []
totals = []
total = 0

for j in range(n):
	testCases.append(int(raw_input()))

for i in testCases:
	for k in range(i):
		if k%3==0 or k%5==0:
			total += k
	totals.append(total)
	total = 0

for l in totals:
	print l
