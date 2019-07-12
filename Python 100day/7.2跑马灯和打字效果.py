import os
import time


def main():
    content = '>>>>>虎 门 人 民 欢 迎 您>>>>>'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.1)
        content = content[1:] + content[0]

def zmd(s='没有信息'):
    
    while True:
        os.system('cls')
        print(s)
        time.sleep(0.5)
        
        s=s[1:]+s[0]

# 打字效果
def yjxs(s='没有信息'):  
    while True:
        c=''
        for i in range(len(s)):
            os.system('cls')
            c+=s[i]
            print(c)
            time.sleep(0.2)



if __name__ == '__main__':
    s='虎门人民欢迎您！>>>>>>>>>>      '
    yjxs(s)

