"""
Shortest FizzBuzz

Write a program that prints (to STDOUT) the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and
for the multiples of five print "Buzz". For numbers which are
multiples of both three and five print "FizzBuzz".

The goal is to write the shortest code possible.

Scoring: Your score is (200 - number of characters in your source
code)/10
"""      
a = ["FizzBuzz" if y%15==0 else "Buzz" if y%5==0 else "Fizz" if y%3==0 else y for y in range(1, 101)]
for z in a:
    print z
