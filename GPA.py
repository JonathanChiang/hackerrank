"""
There is a record of 'n' students, each record having name of student,
percent marks obtained in Maths, Physics and Chemistry. Marks can be
floating values. The user enters an integer 'n' followed by names and
marks for the 'n' students. You are required to save the record in a
dictionary data type. The user then enters name of a student and you
are required to print the average percentage marks obtained by that
student, correct to two decimal places.

Input Format:
Integer N followed by name and marks for N students.

Output Format:
Average percentage of marks obtained

Constraints 
2 <= N <= 10 
0 <= Marks <= 100

Sample Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output
56.00

"""
n = raw_input()
grades = []
for entry in range(int(n)):
    grades.append([i for i in raw_input().split()])
query = raw_input()

# Find list where first item matches name in query and
# assign grades to queryResult
queryResult = [x[1:] for x in grades if x[0] == query]

total = 0
scores = 0
for x in queryResult:
    for y in x:
        total += float(y)
        scores += 1
print "%.2f" % (float(total/scores))
