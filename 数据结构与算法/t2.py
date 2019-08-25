from random import randint
arr=[randint(1,200000) for i in range(100)]
dd=float('inf') /*正无穷大*/
arr.sort()
for i in range(1,len(arr)-1):
    if arr[i-1]==arr[i]:
        continue 
    d=abs(arr[i]-arr[i-1])
    if d<dd:
        a,b,dd=arr[i],arr[i-1],d 


# for i in arr:
#     for j in arr:
#         if i==j:
#             continue 
#         d=abs(j-i)
#         if d<dd: 
#             a,b,dd=i,j,d

print(a,b)