n=eval(input("请输入员工人数"))
money=[]
for j in range(n):
    Nums={}
    name=input("请输入员工姓名")
    month1=eval(input("请输入一月工资"))
    month2=eval(input("请输入二月工资"))
    month3=eval(input("请输入三月工资"))
    Nums['name']=name
    Nums['month1']=month1
    Nums['month2']=month2
    Nums['month3']=month3
    money.append(Nums)
for i in range(len(money)):
    iSum=money[i]['month1']+money[i]['month2']+money[i]['month3']
    average=iSum/3
    money[i]['iSum']=iSum
    money[i]['average']=average
iMoney=sorted(money,key= lambda x:x['average'],reverse=True)
print("%s\t%s\t%s\t%s\t%s\t%s\t"%("姓名","一月","二月","三月","总工资","平均工资"))
for item in iMoney:
    print("%s\t%d\t%d\t%d\t%d\t%.2f"%(item['name'],item['month1'],item['month2'],item['month3'],item['iSum'],item['average']))
