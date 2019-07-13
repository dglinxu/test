import math
def ss(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True if num != 1 else False

num = int(input('请输入需要判断的自然数：'))
print(ss(num))