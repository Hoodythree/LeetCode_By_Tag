def TwoSum(arr, target):
    hash_map = {}
    for i in range(len(arr)):
        remainder = target - arr[i]
        if arr[i] in hash_map:
            return [hash_map[arr[i]], i]
        else:
            hash_map[remainder] = i
    return None


if __name__ == '__main__':
    arr = [2, 7, 11, 14]
    target = 9
    res = TwoSum(arr, target)
    print(res)
