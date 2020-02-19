def fizzbuzz(n): 
    return ['fizz'*(not i%3)+'buzz'*(not i%5) or str(i) for i in range(1,n+1)]

print(fizzbuzz(20))