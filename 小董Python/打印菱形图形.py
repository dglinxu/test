def p_picture(n):
    h=n*2-1
    for i in range(n*2-1):
        s='*'+' *'*(i if i<n else 2*n-2-i)
        # else: 
        #     s='*'+' *'*(2*n-2-i)
        
        print(' '*(abs(n-i-1))+s)



p_picture(7)