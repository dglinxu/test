class Descend: 
    def __init__(self,m,n):
        self.m=m
        self.n=n 
    def __iter__(self):
        return self
    def __next__(self): 
        while self.m>self.n:
            self.m-=1
            return self.m
        raise StopIteration  #通过 raise 中断程序，必须这样写
d=Descend(10,1)              #在这里就要实例化
print(list(d))