#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/5/5
# 开发工具：PyCharm   文件名称：中序转后序表达式.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''

def infix_To_postfix(infixexpr):
    # 等级越高数值越大，‘（’不用处理，所以设为最低
    level = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    op_stack = []
    postfix_list = []
    infix_list = infixexpr.split()
    for c in infix_list:
        if c.isalpha() or c.isalnum():                 #是字母数字直接打入后序列表
            postfix_list.append(c)
        elif c == '(':                  #是括号打入操作符列表
            op_stack.append(c)
        elif c == ')':                  #右括号把操作符弹出来，存入后序列表，直到’('
            t_op = op_stack.pop()
            while t_op != '(':
                postfix_list.append(t_op)
                t_op = op_stack.pop()
        else:                           #是操作符就与操作符列表最后一个操作符比较，如果那个优先级那个先入，直到操作符列表最后一个优先级比它小或为空
            while op_stack and level[op_stack[-1]] >= level[c]:   #先判断op_stack是否为空，否则op_stack[-1]会出错
                postfix_list.append(op_stack.pop())
            op_stack.append(c)
    while op_stack:
        postfix_list.append(op_stack.pop())
    return ''.join(postfix_list)


def postfix_eval(postfixExpr):
    postfix_list=postfixExpr.split()
    operation=[]
    for c in postfix_list:
        if c.isdigit():
            operation.append(c)             #是数字直接压到列表
        else:
            op2=operation.pop()             #要注意操作数的顺序，先出的是第二个数
            op1=operation.pop()
            result=eval(op1+c+op2)          #用字符模拟运算，省去判断运算符
            operation.append(str(result))   #结果转回字符串再存起来

    return float(operation[-1])                #返回的是字符串，可以考虑转回浮点



if __name__ == '__main__':
    # s = "( A + 5 ) * ( C + D )"
    # print(infix_To_postfix(s))
    s1='7 8 + 3 2 + /'
    print(postfix_eval(s1))
