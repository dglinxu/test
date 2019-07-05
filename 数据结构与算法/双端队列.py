class Dqueue(object):
    def __init__(self):
        self.__list=[]
    
    def add_front(self,item):
            self.__list.insert(0,item)
    
    def add_rear(self,item):
            self.__list.append(item)
        
    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list==[]

    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s=Dqueue()
    print(s.is_empty())
    s.add_front('f1')
    s.add_front('f2')
    s.add_rear('r1')
    s.add_rear('r2')
    s.add_rear('r3')
    print(s.pop_front())
    print(s.pop_rear())
    print(s.size())
    print(s.is_empty())