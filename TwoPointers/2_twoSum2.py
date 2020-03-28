# two points: left and right

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i, j = 1, len(numbers)
    while i < j:
        sum_of_two_nums = numbers[i - 1] + numbers[j - 1]
        if sum_of_two_nums == target:
            return [i, j]
        elif sum_of_two_nums > target:
            j -= 1
        else:
            i += 1
    return None