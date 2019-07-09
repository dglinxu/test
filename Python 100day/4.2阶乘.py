num= int(input('请输入需要求阶乘的数：'))
result=1
for i in range(1,num+1):
    result*=i
print('%d的阶乘是：%d'%(num,result))
result2=1
n=num
while n >=1:
    result2*=n
    n=n-1
print('%d的阶乘是：%d'%(num,result2))