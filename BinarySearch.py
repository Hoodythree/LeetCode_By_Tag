def BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = int((high + low) / 2)
        if target == arr[mid]:
            return target
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


def BinarySearchV2(arr, target, low, high):
    if high >= low:

        mid = int((low + high) / 2)
        if target == arr[mid]:
            return target
        if target < arr[mid]:
            return BinarySearchV2(arr, target, low, mid - 1)
        else:
            return BinarySearchV2(arr, target, mid + 1, high)
    else:
        return -1


def find_smallest(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index


def SelectSortV2(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def SelectSort(arr):
    n_iter = len(arr)
    for i in range(n_iter - 1):
        min_index = i
        for j in range(i + 1, n_iter):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


def elements_num(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + elements_num(arr[1:])


def Quick_Sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater)


if __name__ == "__main__":
    arr = [1, 2, 1, 4]
    print('bin_search', Quick_Sort(arr))
