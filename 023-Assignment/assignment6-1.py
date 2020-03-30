# 从键盘获取输入并将其转化为字符列表
input_string = input('please input:').split()

# 将字符数组转化为int列表（如果不是要求输入整数的话可以不要这一句）
input_string_int = [int(i) for i in input_string]

# 将int列表转化为set,去除重复元素（set中的元素是无序的，因此每次输出的顺序可能不一样）
input_string = set(input_string_int)

# 格式化输出，用空格隔开
# 1. 不要求输入整数时：
# print(' '.join(input_string))
# 2. 要求输入整数时：
output_string = [str(i) for i in input_string]
print(' '.join(output_string))
