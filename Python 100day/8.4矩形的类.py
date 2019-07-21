class Rect(object):
    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    def perimeter(self):
        return (self.__height+self.__width)*2

    def area(self):
        return self.__height*self.__width

    def p_rect(self):
        print('矩形的长是%.1f,宽是%.1f' %(self.__width,self.__height))
    
    def __dele__(self):
        print('销毁创建的对象。')


if __name__ == '__main__':
    r1 = Rect(2, 3)
    r2 = Rect(5, 10)
    r1.p_rect()
    # print(r2)
    print(r1.perimeter(), r2.perimeter())
    print(r1.area(), r2.area())
    r1.__dele__()
