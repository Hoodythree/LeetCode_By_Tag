# 输入样例1:
# 5 7
# 输出样例1:
# 53
# 输入样例2:
# 3 1.4
# 输出样例2:
# 2.4
# 输入样例3:
# 8 5
# 输出样例3:
# 4

def reverse_res(res):
    b = str(res)
    c = []
    for i in b:
        c.append(i)
    return c[::-1]


line = input()                #用户输入"1 22  33      5"
nums = line.split()  
res = float(nums[0]) * float(nums[1])
print(reverse_res(res))

#include <stdio.h>
main()
{
int x,y,m; /* 定义整型变量x，y，m */
printf("Please input x and y\n"); /* 输出提示信息 */
scanf("%d%d",&x,&y); /* 读入两个乘数，赋给x，y变量 */
m=x*y; /* 计算两个乘数的积，赋给变量m */
printf("%d * %d = %d\n",x,y,m); /* 输出结果 */
}
