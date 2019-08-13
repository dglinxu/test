def sqr(x):
    y=0.1
    n=0
    while abs(y*y-x)>1e-2:
        y=(y+x/y)/2
        n+=1 
    print(n)
    return y 
print(sqr(88888888888))
print(sqr(4))
