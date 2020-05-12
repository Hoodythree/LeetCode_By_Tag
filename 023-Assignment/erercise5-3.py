'''
3、随机射箭。用随机过程模拟多次射箭行为并计算总分数，射箭次数由键盘输入。
1）请完成程序填空并运行以下代码，观察结果。把___删去换成代码。
'''
import random
import math
import turtle

def pointsGenerate():
   x = random.randint(-350, 350)      #产生随机x坐标
   y = random.randint(-350, 350)      #产生随机y坐标
   return x,y

def judge(x, y):         #参数是x坐标和y坐标
   distance=math.sqrt(x ** 2 + (y-30) ** 2)  #根据x,y坐标计算到靶心的距离
   score=0 if distance>300 else 11-math.ceil(distance/30)  #根据到靶心距离算分数
   return score     #返回分数

def shootingArrow():
     n=int(input("请输入射箭次数："))
     sum=0
     for i in range(n):
         x,y = pointsGenerate()            #调用函数获取随机x,y坐标
         turtle.penup()
         turtle.goto(x,y)
         turtle.pendown()
         turtle.dot(5,"black")     #在x,y坐标处画个黑点表示射箭结果
         turtle.write(judge(x,y))
         sum+= judge(x, y)          #调用函数计算单次分数并加和
     return sum

def drawTargetPlate():    #画靶盘
    turtle.setup(700,700)
    turtle.speed(100)
    for i in range(10):
        turtle.circle(30 + 30 * i)
        turtle.right(90)
        turtle.penup()
        turtle.fd(30)
        turtle.pendown()
        turtle.left(90)

def main():
    drawTargetPlate()
    print("最后总分数是：", shootingArrow())
    turtle.done()
main()







 

