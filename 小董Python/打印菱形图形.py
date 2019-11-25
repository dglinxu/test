def p_picture(n):
    p=
    h=n*2-1
    for i in range(h):
        if i<n:
            s='*'+' *'*i
        else:
            s='*'+' *'*(h-i)
        print(' '*(abs(n-i))+s)


p_picture(6)