import random

color = ['heart', 'diamond', 'spade', 'club']
points = [str(i) for i in range(3, 11)]
points.extend(['J', 'K', 'Q', 'A', '2'])

poker = [x+y for x in color for y in points]
pick_pokers = random.sample(poker, 17)

print('pick pokers : {}'.format(pick_pokers))


def sort_key(single_poker):
    if single_poker[-1] == '0':
        return points.index('10')
    else:
        return points.index(single_poker[-1])

# sort pick_pokers based on their original indexes in points

pick_pokers.sort(key = sort_key)

print('sorted pokers : {}'.format(pick_pokers))