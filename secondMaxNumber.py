"""
You are given 'n' numbers. Store them in a list and find the second largest number. Easy enough!

NOTE : Don't use insertion sort

"""

n = raw_input()
numbers = [int(i) for i in raw_input().split()]

biggest = 0
lessThanBiggest = 0

for x in numbers:
    if x > biggest:
        biggest = x
    if abs(x) > abs(lessThanBiggest) and x < biggest:
        lessThanBiggest = x

print biggest
print lessThanBiggest
