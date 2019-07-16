class Student(object):
    def __init__(self,grade,name,age):
        self.__grade=grade
        self.__name=name
        self.__age=age
    def study(self,book):
        print('%s班同学%s在看《%s》'%(self.__grade,self.__name,book))
    
    def watch_film(self):
        if self.__age>=18:
            print('%s已满18岁，可以看AV。'%self.__name)
        else:
            print('%s未满18岁，不能看AV。'%self.__name)
    
if __name__=='__main__':
    stu1=Student(1,'阿土仔',16)
    stu2=Student(2,'孙小美',24)
    stu3=Student(3,'钱夫人',60)
    stu1.study('高等数学')
    stu3.study('炒股秘籍')
    stu2.watch_film()
    stu1.watch_film()
