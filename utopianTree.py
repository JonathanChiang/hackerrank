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
    
    
            
            
