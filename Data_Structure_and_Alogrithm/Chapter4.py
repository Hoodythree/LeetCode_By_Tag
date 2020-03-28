# 4-1, 4-3, 4-6, 4-9, 4-10, 4-13, 4-14

# 4-1
# s2 = [] 
# s2.extend(['a','b']) 
# s2.append(['c','d']) 
# print("s2=",s2)

# # 4-2
# lst=[23,56,8,900,24] 
# lst.remove(8) 
# lst.append(30) 
# lst.insert(1,22) 
# lst.extend([66,90]) 
# lst.pop(2) 
# print('lst : {}'.format(lst))
# lst.pop(0) 
# print('lst : {}'.format(lst))
# lst.sort() 
# lst.reverse() 
# print(lst)

# 4-6
# 使用快速列表生成方法生成一个长度为10的列表。然后，借助于for循环，将列表元素循环左移一个位 置。
# 举例：['a','b','c','d']循环左移一个位置的结果是['b','c','d','a']
# 
import random

def move_left(nums, step=0):
    end = nums[:step]
    front = nums[step::]
    return front + end

a = [i for i in range(10)]
print('a : {}'.format(a))
# temp = a[0]
# for i in range(1, len(a)):
#     a[i - 1] = a[i]
# a[len(a) - 1] = temp
print('lefted a : {}'.format(move_left(a, 1)))

# 4-9 生成一个8行6列的矩阵，其元素值等于该元素所在位置的行号+列号，其中，行列号从1开始计。
row, column = 8, 6
res = []
for i in range(row):
    temp = []
    for j in range(column):
        temp.append(i + j + 2)
    res.append(temp)
print('res : {}'.format(res))



# 4-20 生成一个6行12列的矩阵，其元素值等于小于20的随机数。
row, column = 6, 12
res = []
for i in range(row):
    temp = []
    for j in range(column):
        temp.append(random.randint(0, 20))
    res.append(temp)
print('res : {}'.format(res))




