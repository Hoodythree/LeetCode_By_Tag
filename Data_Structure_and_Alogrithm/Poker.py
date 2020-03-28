import random

# check user input is a number or not
def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


# (1)
poker = ['Spade', 'Heart', 'Diamond', 'Club']

# (2)
poker_info = [str(i) for i in range(2, 11)] 
poker_character = ['A', 'J', 'Q', 'K']
poker_info += poker_character
print(poker_info)

# (3)
poker_list = []
for i in poker:
    for j in poker_info:
        poker_list.append(i + j)
print('Origin poker list : {}'.format(poker_list))

# (4)
random.shuffle(poker_list)
print('Shuffled poker list : {}'.format(poker_list))

# (5)
while True:
    print('Please input a number between 1 to 52: ')
    user_input = input()
    if is_number(user_input):
        if 1 < int(user_input) < 53:
            print('You get {}'.format(poker_list[int(user_input)]))
            break
        else:
            print('The number must be between 1 to 52. Please input again!')
    else:
        print('Please input a number!')