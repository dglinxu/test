class Queue:
    def __init__(self):          #初始化
        self.items=[]
    
    def isEmpty(self):           #判断是否为空
        return self.items==[]    
    
    def enQueue(self,item):       #入队
        self.items.insert(0,item)
    
    def deQueue(self):            #出队
        return self.items.pop()
    
    def size(self):               #队列大小
        return len(self.items)

# 热土豆、约瑟夫、击鼓传花问题，每隔几个消失一个，如此反复，直至最后一个

#n是参与人数，也可以是队列，m是间隔
def hotPotato(n,m):
    td_queue=Queue()
    for i in range(n):
        td_queue.enQueue(i+1)
    while td_queue.size()>1:
        #在为到间隔m之前，弹出再压进
        for i in range(m):
            td_queue.enQueue(td_queue.deQueue())
        # 到间隔后，弹出不再压进
        td_queue.deQueue()
    return td_queue.deQueue()

print(hotPotato(6,7))



