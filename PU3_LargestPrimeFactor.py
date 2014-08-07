n = raw_input()
nums = []
for entry in range(int(n)):
    nums.append(raw_input())

def isPrime(number):
	for i in range(2,number):
		if (number % i) == 0:
			return False
	return True

for testCase in nums:
	largestFactor = 0;
	for x in range(2, int(testCase)+1):
		if (isPrime(x)):
			if (int(testCase)%x == 0):
				largestFactor = x
	print largestFactor
