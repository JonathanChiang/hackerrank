"""
In this question, the user enters a string and a substring and you have to print the number of times that substring occurs in that string. String traversal will take place from left to right, not from right to left.

NOTE : Letters of string are case-sensitive.

Input Format

Two strings each in a new line.

Constraints

1 <= len(string) <= 200 
each character in the string is an ascii character.

Output Format

An integer number indicating the total number of occurrences of that string.
"""

st = raw_input()
sub = raw_input()
count = 0
index = 0

for i in range(0, len(st)):
    if st[i] == sub[0]:
        if st[i:i+len(sub)] == sub:
            count += 1

print count
               
