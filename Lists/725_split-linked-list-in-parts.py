# Input:
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
from LinkedList.LinkedListPkg import Linkedlist, Node

def splitListToParts(nums, k):
    # nums = []
    # while root:
    #     nums.append(root.val)
    #     root = root.next
    l = len(nums)
    if k > l:
        iter = 0
        ans = []
        while iter < k:
            ans.append([nums[iter]] if iter < l else [])
            iter += 1
        return ans

    ans = []
    i = 0
    element_num, remainder = divmod(l, k)
    while i < l:
        num = element_num
        temp = []
        if remainder > 0:
            num += 1
            remainder -= 1
        for _ in range(num):
            temp.append(nums[i])
            i += 1
        ans.append(temp)
    return ans


def splitListToParts2(root, k):
    if not root:
            return [None] * k
    ans = []
    l = 1
    curr = root
    while curr.next:
        l += 1
        curr = curr.next
    element_num, remainder = divmod(l, k)
    curr = root
    for i in range(k):
        ans.append(curr)
        count = element_num + (1 if i < remainder else 0)
        for j in range(count):
            if j == element_num - 1:
                curr_next = curr.next
                curr.next = None
                curr = curr_next
            else:
                curr = curr.next
    return ans


def print_node(n):
    temp = n
    while temp:
        print(temp.data)
        temp = temp.next



if __name__ == '__main__':
    nums = [i for i in range(5)]
    l = Linkedlist(nums)
    splitListToParts2(l.head.next, 4)


