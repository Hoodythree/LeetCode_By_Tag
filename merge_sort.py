# [5, 7, 2, 9, 3] -> sort[5, 7, 2] + sort[9, 3]
# if l < r:
#     1. get mid index
#     2. mergeSort left : a[:mid]
#     3. mergeSort right : a[mid:]
#     4. merge left and right

def merge(a_left, a_right, a):
    i = j = k = 0
    while i < len(a_left) and j < len(a_right):
        if a_left[i] < a_right[j]:
            a[k] = a_left[i]
            i+=1
        else:
            a[k] = a_right[j]
            j+=1
        k+=1
    while i < len(a_left):
        a[k] = a_left[i]
        i+=1
        k+=1
    while j < len(a_right):
        a[k] = a_right[j]
        j+=1
        k+=1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print()

# # 两次merge
# def merge_sort(a):
#     if len(a) > 1 :
#         mid = len(a) // 2
#         merge_sort(a[:mid])
#         merge_sort(a[mid:])
#         merge(a[:mid], a[mid:], a)

def Quick_Sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater)

def SelectSort(arr):
    n_iter = len(arr)
    for i in range(n_iter - 1):
        min_index = i
        for j in range(i + 1, n_iter):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(a):
    res = []
    mid = len(a) // 2
    left = SelectSort(a[:mid])
    right = SelectSort(a[mid:])
    res.append(left)
    res.append(right)
    return res

    

if __name__ == '__main__': 
    arr = [12, 2, 51, 4, 9, 1, 20, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    merge_sort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


