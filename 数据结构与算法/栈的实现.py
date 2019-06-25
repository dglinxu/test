class Stack(object):
    def __init__(self):
        self.__list=[]
    
    def push(self,item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()
    
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    
    def is_empty(self):
        return self.__list==[]

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    s=Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(6)
    print(s.size())
    print(s.peek())
    print(s.pop())





