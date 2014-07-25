"""
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle of the tree
occurs during the monsoon, when it doubles in height. The second growth cycle of the tree occurs
during the summer, when its height increases by 1 meter. 
Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. 
Can you find the height of the tree after N growth cycles?

Input Format 
The first line contains an integer, T, the number of test cases. 
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

Constraints 
1 <= T <= 10 
0 <= N <= 60

Output Format 
For each test case, print the height of the Utopian tree after N cycles.

"""


cases = int(raw_input())
seasons = []
heights = []
for i in range(cases):
    seasons.append(raw_input())

for x in seasons:
    height = 1
    x = int(x)
    y = 0
    while y != x:
        if y == x:
            break
        elif y % 2 == 1:
            height += 1
            y += 1
        elif y % 2 == 0:
            height *= 2
            y += 1
    heights.append(height)

for tree in heights:
    print tree
    
    
            
            
