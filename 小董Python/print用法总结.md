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
   