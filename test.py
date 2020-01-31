# -*- coding: utf-8 -*-
import re
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat,s)
for i in r:
    print(i.span()[0])











# import time
# def typewriting(n=250,delay=0.1):
#     for i in range(n):
#         # s='\r%d'%i
#         print('\r%d'%i,end='')
#         time.sleep(delay)
# typewriting()
        





# import time
# def movingpoint(cycle=20,delay=0.1):
#     for i in range(cycle):
#         for i in ['--','\\','|','/']:
#             print('\b%s'%i,end='',flush=True)
#             time.sleep(delay)
# movingpoint()






# import time

# def printer(text, delay=0.5):
#     """打字机效果"""
    
#     for ch in text:
#         print(ch, end='',flush=True)
#         time.sleep(delay)

# def printer2(ch,delay=0.5):
#     s=''
#     for i in ch:
#         # s='\b'*2+s+i
#         s=s+i       
#         print('\r%s'%s,end=' ')
#         time.sleep(delay)
        
# printer('飞雪连天射白鹿，笑书神侠倚碧鸳。')
# print()
# printer2('飞雪连天射白鹿，笑书神侠倚碧鸳！')




# for i in range(5): 
#     i=3
#     print(i)
#     i=10



# class TestClass: 
#     def __init__(self):
#         print('init')
#     def __del__(self): 
#         print('del')
# print(TestClass() is TestClass())

# print(id(TestClass())==id(TestClass()))


# a=[lambda x,i=i:x+i for i in range(5)]
# for f in a: 
#     print(f(2))


