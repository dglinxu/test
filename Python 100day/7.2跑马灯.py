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


if __name__ == '__main__':
    main()