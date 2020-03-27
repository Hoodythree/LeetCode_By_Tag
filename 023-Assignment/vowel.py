# count vowels in a string

string = input('Please input string : ')
res = []
vowels = ['a', 'e', 'i', 'o', 'u']
for s in string:
    if s in vowels:
        res.append(s)

print(len(res))