# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
def maxArea(height):
    i, j = 0, (len(height) - 1)
    res = 0
    while i < j:
        volume = (j - i) * min(height[i], height[j])
        res = max(res, volume)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res


if __name__ == '__main__':
    nums = [1,8,6,2,5,4,8,3,7]
    print(maxArea(nums))


