import random
face=random.randint(1,6)
if face==1:
    result='唱首歌'
elif face==2:
    result='跳个舞'
elif face==3:
    result='学狗叫'
elif face==4:
    result='做俯卧撑'
elif face==5:
    result='讲笑话'
else:
    result='学猫叫'
print('你要做的是：%s'%result)