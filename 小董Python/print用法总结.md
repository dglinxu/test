Print用法总结
1. **\r 表示将光标的位置回退到本行的开头位置**
```
   import time
   li = ["\\", "|", "/", "—"]  #第一个两个斜杠是为了转义
   for i in range(50):
    # print('\r%d'%i,end='') #光标在字符后面
    # print(i,end='\r') #光标在字符前面
    # print('\r'+'*'*i,end=' ')
    # j = i % 4
    # print('\r'+li[j], end='') #转圈
    print('\r' + '※' * i, end='')  #进度条
    time.sleep(0.2)
```
2. **\b表示将光标的位置回退一位**
3. **删除效果**
   import time
   print('\r'+s[:l-i],end=' ')  #end后面是空格
   print('\r'+'离程序退出还有%d秒！'%(10-i),end=' ') 
   time.sleep(0.5)

   >>> pi = 3.141592653  
>>> print('%10.3f' % pi) #字段宽10，精度3  
     3.142  
>>> print("pi = %.*f" % (3,pi)) #用*从后面的元组中读取字段宽度或精度  
pi = 3.142  
>>> print('%010.3f' % pi) #用0填充空白  
000003.142  
>>> print('%-10.3f' % pi) #左对齐  
3.142       
>>> print('%+f' % pi) #显示正负号  
+3.141593