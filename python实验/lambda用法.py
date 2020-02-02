from functools import reduce

a=[2,1,5,7,3,8]

# 使用reduce前要导入functiontools
# reduce_t=reduce(lambda x,y:'{}{}'.format(x,y),a)   #正序排列，而且不用填0、1
reduce_t=reduce(lambda x,y:'{1}{0}'.format(x,y),a) #逆序排列，{1}这个在前
print(list(reduce_t))   #转换成列表是字符，也可以直接输出，不是迭代器

reduce_t2=reduce(lambda x,y:x+y,['b','c','d'],'a') #最后一个参数是固定初始值
print(reduce_t2)

# 使用函数前可以先自行定义lambda函数
add=lambda x,y:x+y
print(add(2,3))
print(add(a,a)) #这表示两个列表的合并，而不是元素的和
print(list(map(lambda x,y:x+y,a,a))) #列表对应元素的相加可用MAP

map_t=list(map(lambda x:x+1,a))
print(map_t)

filter_t=list(filter(lambda x:x>3,a))
print(filter_t)

sorted_t=sorted(a,key=lambda x:abs(x-2))  #根据与2的距离排序
print(sorted_t)

#也可以不用lambda，自行定义函数
def f(x):
    return True if x==1 else False
map_t1=list(map(f, [1,2,3])) #[True, False, False]
print(map_t1)