def sum_num(n):
    if n==0:
        return 1 
    return sum_num(n-1)+(2*n+1)
     
print(sum_num(4))
