class Deque:
    def __init__(self):
        self.items=[]
    
    def isEmpte(self):
        return self.items==[]
    
    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

'''回文字的判断'''
def palchecker(aString):
    chardeque=Deque()
    for ch in aString:
        chardeque.addFront(ch)
    stillEqual=True
    
    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        
        if first != last:
            stillEqual=False
    return stillEqual

print('上海自来水来自海上',palchecker('上海自来水来自海上'))
print('北京输油管油输京北',palchecker('北京输油管油输京北'))
print('山东落花生花落东山',palchecker('山东落花生花落东山'))
    

