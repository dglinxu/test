#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/5 
#开发工具：PyCharm   文件名称：打印队列模拟.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
import random

class Printer:
    def __init__(self,ppm):
        self.Pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0

    def tick(self):
        if self.currentTask !=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask !=None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.Pagerate

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp

def simulatiom(numSeconds,pagesPerMinutes):

    labprinter=Printer(pagesPerMinutes)
    printQueue=[]
    waitingtimes=[]

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.append(task)
        if (not labprinter.busy()) and printQueue:
            nexttask=printQueue.pop()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("平均等待 %6.2f 秒 %3d tasks remaining."%(averageWait,len(printQueue)))

def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(10):
        simulatiom(3600,5)
