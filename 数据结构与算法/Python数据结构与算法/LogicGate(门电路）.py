#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/5/4
# 开发工具：PyCharm   文件名称：LogicGate(门电路）.py
# E-mail: humen@189.cn
'''说明： 门电路连接后，连接部分末端输入是开始端的输出（return self.pinB.getFrom().getOutput()）。
没有连接的就要输入。注意要处理空脚。
----------------------------'''


class LogicGate:
    # 逻辑门
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    # 双输入逻辑电路，有A、B两个输入
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA==None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + ' --> '))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB==None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + ' --> '))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA==None:
            self.pinA=source
        else:
            if self.pinB==None:
                self.pinB=source
            else:
                raise RuntimeError('Error:NO EMPTY PINS !')



class AndGate(BinaryGate):
    # 与门，继承双输入逻辑门
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    # 单输入逻辑电路，如‘非门’

    def __init__(self, n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin==None:
            return int(input("Enter Pin input for gate " + self.getLabel() + ' --> '))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin==None:
            self.pin=source
        else:
            raise RuntimeError('Error:NO EMPTY PIN! ')

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:
    def __init__(self,from_gate,to_gate):
        self.from_gate=from_gate
        self.to_gate=to_gate

        to_gate.setNextPin(self)

    def getFrom(self):
        return self.from_gate

    def getTo(self):
        return self.to_gate


# g1 = AndGate('G1')
# print(g1.getOutput())
# g2=OrGate('G2')
# print(g2.getOutput())

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.getOutput())