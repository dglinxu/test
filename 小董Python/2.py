import random 
import string
x=string.ascii_uppercase+string.digits+string.punctuation
print(x)
li=[random.choice(x) for i in range(50)]
s=''.join(li)
print(s)
dic={}
for i in s:
    dic[i]=dic.get(i,0)+1
for k,v in dic.items():
    print(k,v)