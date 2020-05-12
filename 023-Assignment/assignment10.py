change={"010":"北京", "023":"重庆",
"021":"上海", "028":"成都",
"020":"广州"}

phoneNumbers=["023－66666666",
"028-77777777","010-88888888",
"023-55555555","010－99999999",
"023－11111111"]

dct = {}

for n in phoneNumbers:
    if change[n[:3]] not in dct:
        dct[change[n[:3]]] = 1
    else:
        dct[change[n[:3]]] += 1

print(dct)

