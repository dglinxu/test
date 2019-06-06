nums=[0,0,0,1,2,2,5,6,7,8,8]
l=len(nums)
t=[nums[0]]
for i in range(1,l):
    if nums[i-1]!=nums[i]:
        t.append(nums[i])
print(t)