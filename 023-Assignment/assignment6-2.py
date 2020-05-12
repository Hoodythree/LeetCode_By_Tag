idCards=["420821198411300017",\
"42082119680628004X",\
"422432197608280034",\
"420821196509095016",\
"441402196304056047",\
"420821196802056018",\
"420821199109136038",\
"420821196907246043",\
"441402196711030119",\
"42243219700222007X",\
"420821196302280513",\
"420821196401252323",\
"420821197403116020",\
"420821197208166030",\
"420821196610282318",\
"441402197805295552",\
"420821198211202359",\
"422432197207090045",\
"422432197101040517",\
"441402197601160515",\
"422432198107210526",\
"422432197009190096"]   

def comCheck(x):
    numbers=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    checkNumbers=['1','0','X','9','8','7','6','5','4','3','2']
    mySum=0
    for i in range(17):
       mySum=mySum+int(x[i])*numbers[i]
    myMod=mySum%11
    return  checkNumbers[myMod]

male=0
for x in range(len(idCards)):
    if int(idCards[x][16])%2==1:
        male=male+1
female=len(idCards)-male
print("男性有%d人，女性有%d人"%(male,female))


idCards1=sorted(idCards,reverse=True,key=lambda x:x[6:14])
print("按年龄排序: ",idCards1)

regions=[]
for x in range(len(idCards)):
    if idCards[x][:6] not in regions:
        regions.append(idCards[x][:6])
print("共来自%d个地区"%(len(regions)))

#利用集合
regions=[]
for x in range(len(idCards)):
    regions.append(idCards[x][:6])
print("共来自%d个地区"%(len(set(regions))))

errors,errorsChecked=[],[]
for x in range(len(idCards)):
    check=comCheck(idCards[x])
    beCheck=idCards[x][17]
    if check!=beCheck:
        errors.append(idCards[x])
        errorsChecked.append(idCards[x][:17]+check)
print("错误号码: ",errors)
print("正确号码: ",errorsChecked)
   