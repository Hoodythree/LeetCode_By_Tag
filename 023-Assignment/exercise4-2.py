import random

color = ['heart', 'diamond', 'spade', 'club']
points = [str(i) for i in range(3, 11)]
points.extend(['J', 'K', 'Q', 'A', '2'])

poker = [x+y for x in color for y in points]
poker_dct = {p:0 for p in poker}
for i in range(5000):
    pick_pokers = random.sample(poker, 1)
    pick_pokers = str(pick_pokers[0])
    poker_dct[pick_pokers] += 1
poker_dct = sorted(poker_dct.items(), key=lambda item: item[1], reverse=True)

for i in range(5): 
    print(poker_dct[i][0] + '\t' + str(poker_dct[i][1]))