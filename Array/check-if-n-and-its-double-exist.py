# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

# sort + two pointer
def checkIfExist(arr):
    # use dict
    dct = {}
    for i, a in enumerate(arr):
        if a * 2 in dct:
            return True
        elif not a % 2 and a // 2 in dct:
            return True
        else:
            dct[a] = i
    return False

arr = [0, 1, 2, 4]
print(checkIfExist(arr))

        
