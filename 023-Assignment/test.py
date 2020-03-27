
lst=input("请输入字符串：")
Counter=0




for x in lst:
    for y in ["a","e","i","o","u"]:
        if y in x:
            Counter+=x.count(y)
print(Counter)
