class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,val):
        return self.items.append(val)

    def  pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return  len(self.items)
''''在列表的头作为栈的尾'''
# class Stack:
#     def __init__(self):
#         self.items=[]
#
#     def isEmpty(self):
#         return self.items==[]
#
#     def push(self,val):
#         return self.items.insert(0,val)  #增加元素要用insert
#
#     def  pop(self):
#         return self.items.pop(0)         #弹出元素要用索引
#
#     def peek(self):
#         return self.items[0]             #此处是队列的开头
#
#     def size(self):
#         return  len(self.items)



# s=Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('True')
# print(s.peek())
# s.push(8.4)
# print(s.size())
# print(s.pop())