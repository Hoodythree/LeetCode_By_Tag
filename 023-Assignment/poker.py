import random

color = ['heart', 'diamond', 'spade', 'club']
point = [str(i) for i in range(2, 11)]
point.extend(['J', 'K', 'Q', 'A'])

poker = [x+y for x in color for y in point]
pick_pokers = random.sample(poker, 17)

print('pick pokers : {}'.format(pick_pokers))

# points mapping
def mapping_points(dct):
    for k, v in dct.items():
        if v == 'J':
            dct[k] = '11'
        elif v == 'Q':
            dct[k] = '12'
        elif v == 'K':
            dct[k] = '13' 
        elif v == 'A':
            dct[k] = '14' 
        elif v == '2':
            dct[k] = '15' 
        elif v == '0':
            dct[k] = '10'
        else:
            pass
    return dct

# dict存储
# key : poker name 
# value : poker points
dct = {}
for p in pick_pokers:
    dct[p] = p[-1]
print('original dict : {}'.format(dct))

# points mapping
dct = mapping_points(dct)
print('mapped dict : {}'.format(dct))

# sorted by value
dct = {k: v for k, v in sorted(dct.items(), key=lambda item: int(item[1]))}
print('sorted dict : {}'.format(dct))

# print result
res = [k for k, v in dct.items()]
print('result : {}'.format(res))

