# from random import randint
# a=["flower","flow","flight"]
# print(min(len(i) for i in a))
# li=[randint(1,10) for i in range(25)]
# s=set(li)
# for i in s:
#     print('%d数字的次数是：%d'%(i,li.count(i)),end='\n')
import time
li = ["\\", "|", "/", "—"]  #第一个两个斜杠是为了转义

for i in range(50):
    # \r 表示将光标的位置回退到本行的开头位置
    # \b表示将光标的位置回退一位
    # print('\r%d'%i,end='') #光标在字符后面
    # print(i,end='\r') #光标在字符前面pip
    # print('\r'+'*'*i,end=' ')
    # j = i % 4
    # print('\r'+li[j], end='')
    print('\r' + '※' * i, end='')  #进度条
    time.sleep(0.2)
