class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext
    
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head.next)
        self.head=temp

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            count=count.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    '''没考虑搜不到的情况'''
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current !=None and not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:                   #item是第一个，头的next是current.next
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

    #自己搞的
    def pop(self):
        current=self.head
        previous=None
        while current!=None:
            previous=current
            current=current.getNext()
        previous=None
        return current.getData()

    def append(self,item):
        



