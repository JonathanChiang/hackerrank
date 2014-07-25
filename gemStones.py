"""
John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lowercase latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a 'gem-element' if it occurs at least once in each of the rocks.

Given the list of rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format 
The first line consists of N, the number of rocks. 
Each of the next N lines contain rocks' composition. Each composition consists of lowercase letters of English alphabet.

Output Format 
Print the number gem-elements that exist in those rocks.

Constraints 
1 ≤ N ≤ 100 
Each composition consists of only small latin letters ('a'-'z'). 
1 ≤ Length of each composition ≤ 100

Sample Input

3
abcdde
baccd
eeabg

Sample Output

2
Explanation 
Only "a", "b" are the two kind of gem-elements, since these are the only characters that occur in each of the rocks' composition.

"""
def gemCheck(letter, rocks):
	"""
	Determines if rock is a gem, as per above instructions
	Input:
	letter: letter from the longest string
	rocks: array of strings representing rocks

	Output:
	True if letter is present in each string in rocks
	"""
	ltrRep = 0
	for rock in rocks:
		if letter in rock:
			ltrRep += 1
	if ltrRep / len(rocks) == 1:
		return True


n = int(raw_input()) 
rocks = []
gems = 0

# Input
for i in range(int(n)):
	rocks.append(raw_input().rstrip())

longest = 0

# find the longest string in array of rocks
for j in range(int(n)):
	if len(rocks[j]) > longest:
		longest = j

longestGem = "".join(rocks[longest])

# dictionary to track duplicate letters
duplicates = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}


for letter in longestGem:
	#check if the letter has already been checked
	if duplicates[letter] == 0:
		duplicates[letter] = 1

		# call gemCheck function
		if gemCheck(letter, rocks):
			gems += 1

print gems


