# def lengthOfLongestSubstring(self, s: str):
#     if not s:
#         return 0
#     left = 0
#     lookup = set()
#     n = len(s)
#     max_len = 0
#     cur_len = 0
#     for i in range(n):
#         cur_len += 1
#         while s[i] in lookup:
#             lookup.remove(s[left])
#             left += 1
#             cur_len -= 1
#             print(lookup)
#         if cur_len > max_len:
#             max_len = cur_len
#         lookup.add(s[i])
#     return max_len


# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))

# def add(sum,x,y):
    
#     if sum<10:
#         x +=3
#         y +=2
#         sum=x+y
#         sum=add(sum,x,y)
#         return sum
#     else:
#         sum=sum+x+y
#         print(sum)
#         return '两数之和：',sum

# print(add(0,0,0)[0],add(0,0,0)[1])

# 

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: liang 
# date={
#     '北京':{
#         "昌平":{
#         "沙河":["oldboy","test"],
#         "天通往":["我爱我家","liang"]
#     },
#     "朝阳":{
#         "望经":["本词","默默"],
#         "国贸":["CICC","HP"],
#         "东之梦":["Advent","飞信"]
#     }
#     },
#     "江西":{
#         "南昌":{
#             "南昌县":["现代学院","江西师范大学"],
#             "新建县":["江西南昌大学","江西农业大学"]
#         },
#         "抚州":{
#             "东乡县":["小黄","浴缸"],
#             "临川区":["临川二中","临川一中"]
#         }

#     },
#     "湖南":{
#         "长沙":{
#             "aaaa":["vvv","aaaa"],
#             "cccc":["cada","cada"]
#         }
#     }
# }

# while True:
#     for i in date:
#         print(i)
#     choie=input("你要选择那个城市？1>>>>>")
#     if choie in date:
#         while True:
#             for i2 in date[choie]:
#                 print(i2)
#             choie2=input("你要选择那个城市？2>>>>>")
#             if choie2 in date[choie]:
#                 while True:
#                     for i3 in date[choie][choie2]:
#                         print(i3)
#                     choie3 = input("你要选择那个城市？3>>>>>")
#                     if choie3 in date[choie][choie2]:
#                         for i4 in date[choie][choie2][choie3]:
#                             print(i4)
#                         choie4=input("已经是最后一层！按b退出>>>>>")
#                         if choie4 == 'b':
#                             pass
#                         elif choie4 =='q':
#                             exit("bye!!!!")
#                         else:
#                             print("你输入的有误")
#                     if choie3== 'b':
#                         break
#                     elif choie3 =='q':
#                         exit("bye !!!")
#                     else:
#                         print("你输入的有误")
#             if choie2=='b':
#                 break
#             elif choie2=='q':
#                 exit("bye!!!!")
#             else:
#                 print("你输入的有误")
#     if choie=='b':
#         print("如果退出请按q")
#     elif choie =='q':
#         exit("bye !!!")
#     else:
#         print("你输入的有误")
# step=0
# def move(n, a, buffer, c):
#     global step
#     if(n == 1):
#         step+=1
#         print('第%d步：'%step,a,"->",c)
#         return
#     move(n-1, a, c, buffer)
#     move(1, a, buffer, c)
#     move(n-1, buffer, a, c)

# move(6, "a", "b", "c")

def mergsort(alist):
    n=len(alist)//2
    if n==1:
        print(alist)
        return 
    li=mergsort(alist[:n])
    lh=mergsort(alist[n:])
    

if __name__=='__main__':
    alist=[2,1,8,5,6,0,2,7,3,9]
    print(mergsort(alist))


    