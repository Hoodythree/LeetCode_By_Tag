n = 1
while n > 0:
    if n % 5 == 1 and n % 6 == 5 and n % 7 == 4 and n % 11 == 10:
        break
    else:
        n += 1

print(n)