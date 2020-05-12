# p1 = {"姓名":"张三", "一月工资": 2010, "二月工资": 2020, "三月工资":2100}
# p2 = {"姓名":"李四", "一月工资": 2000, "二月工资": 3220, "三月工资":1100}
# p3 = {"姓名":"王五", "一月工资": 4000, "二月工资": 2090, "三月工资":4100}

# people = [p1, p2, p3]
# people.sort(key=lambda p: p['一月工资'] + p['二月工资'] + p['三月工资'], reverse=True)
# print("姓名\t一月\t二月\t三月\t总工资\t均工资")
# for p in people:
#     total = p["一月工资"] + p["二月工资"] + p["三月工资"]
#     average = total / 3
#     print(p["姓名"] + "\t" + str(p["一月工资"]) + "\t" + str(p["二月工资"]) + "\t" + str(p["三月工资"]) + "\t" + str(total) + "\t" + str(average))

people = []
n = input("输入员工数量：")
for i in range(int(n)):
    p = {}
    name = input("name:")
    Jan_salary = float(input("一月工资："))
    Feb_salary = float(input("二月工资："))
    Mar_salary = float(input("三月工资："))
    p['姓名'] = name
    p['一月工资'] = Jan_salary
    p['二月工资'] = Feb_salary
    p['三月工资'] = Mar_salary
    p['总工资'] = Jan_salary + Feb_salary + Mar_salary
    p['平均工资'] = p['总工资'] / 3
    people.append(p)

# p1 = {"姓名":"张三", "一月工资": 2010, "二月工资": 2020, "三月工资":2100}
# p2 = {"姓名":"李四", "一月工资": 2000, "二月工资": 3220, "三月工资":1100}
# p3 = {"姓名":"王五", "一月工资": 4000, "二月工资": 2090, "三月工资":4100}

# people = [p1, p2, p3]
people.sort(key=lambda p: p['平均工资'], reverse=True)
print("姓名\t一月\t二月\t三月\t总工资\t均工资")
for p in people:
    print(p["姓名"] + "\t" + str(p["一月工资"]) + "\t" + str(p["二月工资"]) + "\t" + str(p["三月工资"]) + "\t" + str(p["总工资"]) + "\t" + str(p["平均工资"]))

