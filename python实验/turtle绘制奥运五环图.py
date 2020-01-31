import turtle
def drawCircle(x,y,c='red'):
    p.pu()# 抬起画笔
    p.goto(x,y) # 绘制圆的起始位置
    p.pd()# 放下画笔
    p.color(c)# 绘制c色圆环
    p.circle(60,360) #绘制圆：半径，角度
p = turtle
p.pensize(6) # 画笔尺寸设置3
drawCircle(0,0,'blue')
drawCircle(120,0,'black')
drawCircle(240,0,'red')
drawCircle(180,-60,'green')
drawCircle(60,-60,'yellow')    

p.done()
