# *args and **kwargs

# 接受non-keyword的可变长度的变量
def foo1(a1, *args):
    print('first argument: {}'.format(a1))
    for a in args:
        print('other arguments: {}'.format(a))

# 接受带keyword(有命名)的可变长度的变量
def foo2(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('{} == {}'.format(key, value))

# Using *args and **kwargs to call a function
def test_func(arg1, arg2, arg3):
    print('arg1 : ', arg1)
    print('arg2 : ', arg2)
    print('arg3 : ', arg3)

# Order of using *args **kwargs and formal args
# some_func(fargs,*args,**kwargs)

# 1. 
foo1(1, 2, 3, 4)
# 2. 
# name == 1
# age == 29
foo2(name = 1, age = 29)
foo2(a1 = 1)
# 3.
# sargs = ('name', 2, 33)
kwargs = {'arg2': 21, 'arg3': 3, 'arg1': 44}
# test_func(*args)
test_func(**kwargs)