def get_value(ls):
    ls.sort()
    return ls[-1],ls[-2]

def max(ls):
    # if ls[0]>ls[1]:
    #     m1=ls[0]
    #     m2=ls[1]
    # else:
    #     m1,m2=ls[1],ls[0]
    m1,m2=(ls[0],ls[1]) if ls[0]>=ls[1] else (ls[1],ls[0])
    for i in range(2,len(ls)):
        if ls[i]>m1:
            m1,m2=ls[i],m1
        elif ls[i]>m2:
            m2=ls[i]
    return m1,m2
        

ls=[1,5,9,2,3,5,6,0]
print(get_value(ls)[0])
print(max(ls))
