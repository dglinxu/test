def list_extend(alist): 
    #把复合列表展开成单列表，采用迭代方式逐层剥离
    for a in alist: 
        if type(a)==list: 
            yield from list_extend(a)  #这里有from
        else: 
            yield a 
alist=[1,2,[3,4,[5,6],7],8,["python",6],9]
print(list(list_extend(alist)))