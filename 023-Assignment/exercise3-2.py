# 2、生成一个n*n的随机数二维矩阵(n由键盘输入，矩阵元素是[0，9]范围内整数)
#    1) 求每一行的最大值，并添加进列表rowMax。
#    2) 求每一列的最大值，并添加进列表columnMax。
#    输出rowMax和columnMax。

# 输入n为3，随机生成矩阵
#    1  6  8
#    5  4  9
#    3  7  2
#    输出: 
#    行最大 [8, 9, 7]
#    列最大 [5, 7, 9]
import random
n = 3
nums = [[random.randint(0, 9) for j in range(n)] for i in range(n)]
for i in range(n):
    print(nums[i])
rowMax = [max(nums[i]) for i in range(n)]

for i in range(n):
    for j in range(i, n):
        nums[j][i], nums[i][j] = nums[i][j], nums[j][i]


for i in range(n):
    print(nums[i])
columnMax = [max(nums[i]) for i in range(n)]
print('maxRow : {}\nmaxColumn : {}'.format(rowMax, columnMax))

