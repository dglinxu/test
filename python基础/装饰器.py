#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：装饰器.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
import time
import random


class retry:
    def __init__(self,max_times=3,wait_time=0,exceptions=Exception):
        self.max_times=max_times
        self.wait_time=wait_time
        self.exceptions=exceptions

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            for i in range(self.max_times):
                try:
                    print('正在尝试第%d次.....'%(i+1))
                    result=func(*args,**kwargs)
                except self.exceptions:
                    print('数值异常，等待%d秒继续尝试....'%self.wait_time)
                    print('-----------------')
                    time.sleep(self.wait_time)
                    continue
                else:
                    print('尝试%d次，找到需要的结果。'%(i+1))
                    return result
            print('超出尝试次数，无法找到正确的值！')

        return wrapper
@retry(5,1,ValueError)
def test():
    num=random.randint(-8,1)
    if num<0:
        print('%d 小于0,不符合要求。'%num)
        raise ValueError
    else:
        print("数值【%d】符合要求！"%num)


test()




def logger(message='无程序传入'):
    def run_time(func):

        def wrapper(*args,**kwargs):
            start = time.time()
            result=func(*args,**kwargs)
            end=time.time()
            print('[{}] 程序执行时间是：{}秒'.format(message,round(end-start,2)))
            return result
        return wrapper
    return run_time

# @logger('打印')
# def p():
#     time.sleep(2)
# @logger('分析')
# def f():
#     time.sleep(5)
#
# p()
# f()









def timer(func):
    def wrapper(*args,**kwargs):
        print('Sleep开始......')
        start=time.time()
        func(*args,**kwargs)
        print('Sleep结束！')
        stop=time.time()
        print('程序运行时间是：{}'.format(stop-start))
    return wrapper

# @timer
# def sleep(n):
#     time.sleep(n)
#
# sleep(5)

'''带参数的函数装饰器'''
def say_hello(country):
    def wrapper(func):
        def say(*args,**kwargs):
            func(*args, **kwargs)
            if country=='china':
                print('中国人，你好！')
            elif country=='american':
                print('American,hello!')
            else:
                return

            # func(*args, **kwargs)
        return say

    return wrapper

# @say_hello('china')
# def china():
#     print('我是中国人。')
#
# @say_hello('american')
# def american():
#     print("I'm a american.")
#
# china()
# american()

'''不带参数的类装饰器'''
class Say_hello():
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        print("Hello,I'm back!")
        print('正在执行{}程序'.format(self.func.__name__))
        return self.func(*args,**kwargs)

# @Say_hello
# def say(somthing):
#     print('say {}'.format(somthing))
#
# say('中国人，Hello！')


'''带传入参数的类装饰器'''
class info():
    def __init__(self,message='普通信息'):
        self.m=message

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            func(*args, **kwargs)
            print('信息发布：{}'.format(self.m))
        return wrapper

# @info('紧急信息，十二级台风！')
# def message(something):
#     print('今天发布的信息是：{}.........'.format(something))
#
# message('天气预报')

# class log:
#     def __init__(self,message):
#         self.m=message
#
#     def __call__(self, func):
#         print('-------')
#         def wrapper(*args,**kwargs):
#             print('{} is running!'.format(func.__name__))
#             print('信息是：{}'.format(self.m))
#             func(*args,**kwargs)
#             print('Game is over!')
#         return wrapper
#
# @log
# def test(message):
#     print('外部函数：test')
#
# test('我去麦当劳')
