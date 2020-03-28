def minTimeToVisitAllPoints(points):
    step = 0
    for i in range(len(points) - 1):
        pre = points[i]
        next = points[i+1]
        step += max(next[0] - pre[0], next[1] - pre[1])
    return step

def replaceElements(arr):
    max_so_far = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_so_far = max_so_far, max(max_so_far, arr[i])
    return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))