# **Python类的解析**

## 一、self与cls，静态方法（@staticmethod）与类方法（@classmethod）

1. #### self表示实例方法的第一个参数。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。

2. #### cls表示这个类方法的第一个参数。

3. 类在使用@staticmethod或@classmethod，就可以不需要实例化，直接用类名（实例化）+方法名()来调用；没有定义的方法，要实例化后，用实例化+方法名（）调用。

   ```python
   class A:
       a = 'a'
       
       @staticmethod
       def foo1(name):          #静态方法，参数无self\cls，无实例化也可调用
           print('hello', name)
       
       def foo2(self, name):    #用cls\self貌似都可以，要实例化后才能调用
           print('hello', name)
       
       @classmethod                 
       def foo3(cls, name):     #类方法，用cls\self貌似都可以,无实例化也可调用
           print('hello', name
   ```

   ```python
   a=A()
   a.foo1('阿土仔') #hello 阿土仔
   A.foo1('阿土仔') #hello 阿土仔
   ```

   ```python
   a.foo2('阿土仔') #hello 阿土仔
   A.foo2('阿土仔') #抛出异常
   ```

   ```python 
   a.foo3('阿土仔') #hello 阿土仔
   A.foo3('阿土仔') #hello 阿土仔、
   ```



4. 的地方

## 二、init  new 方法的次序

首先执行new(第一个参数要用cls) ,再到init

```python
class A:
    '''This is a class.'''
    def __init__(self,n):
        self.n=n
        print('This is init.')
    
    def __new__(cls,n):          #此处要用cls,不能用self
        print('This is new！')
        print('input number is :',n)
        return super().__new__(cls)  
    #不用第二参数，return None或0，new不成功，不往下执行（init），退出。
     
    def __del__(self):
        print('This is del.')
.

a=A(1)
del a
# This is new！
# input number is : 1
# This is init.
# This is del.`
```

## 三、类属性、实例属性及共有属性和私有属性



```python
class Student():
    i = 1    #类属性
    __j = 2  #类私有属性
    
    def __init__(self,name,age):  
        self.name = name   #实例属性
        self.__age = age   #实例私有属性，避免被直接调用
        
    def pt_age(self):
        print(self.__age)
        
print('类属性：Student.i-->',Student.i)
print('类私有属性：Student._Student__j-->',Student._Student__j)
 
st1 = Student('tao',24)
st2 = Student('阿土仔',25)
print('类属性可以实例调用：st1.i-->',st1.i)
print('类属性：Student.i-->',Student.i)

st1.pt_age()
print('类私有属性的实例化调用：st1._Student__age-->',st1._Student__age)

# 类属性：Student.i--> 1
# 类私有属性：Student._Student__j--> 2
# 类属性可以实例调用：st1.i--> 1
# 类属性：Student.i--> 1
# 24
# 类私有属性的实例化调用：st1._Student__age--> 24



```

## 四、各种定义

一：属性：

　　尽量把需要用户传入的属性作为实例属性，而把同类都一样的属性作为类属性。实例属性在每创造一个实例时都会初始化一遍，不同的实例的实例属性可能不同，不同实例的类属性都相同。从而减少内存。

　　1：实例属性：

　　　　最好在__init__(self,...)中初始化

　　　　内部调用时都需要加上self.

　　　　外部调用时用instancename.propertyname

　　2:类属性：

　　　　在__init__()外初始化

　　　　在内部用classname.类属性名调用

　　　　外部既可以用classname.类属性名又可以用instancename.类属性名来调用

　　3：私有属性：

　　　　1）：单下划线_开头：只是告诉别人这是私有属性，外部依然可以访问更改

　　　　2）：双下划线__开头：外部不可通过instancename.propertyname来访问或者更改

　　　　　　实际将其转化为了_classname__propertyname

二：方法

　　1：普通类方法：

　　　　def fun_name(self,...):

　　　　　　pass

　　　　外部用实例调用

　　2：静态方法：@staticmethod       

　　　　　　不能访问实例属性！！！  参数不能传入self！！！

　　　　　　与类相关但是不依赖类与实例的方法！！

　　3:类方法：@classmethod

　　　　　　不能访问实例属性！！！  参数必须传入cls！！！

　　　　　　必须传入cls参数（即代表了此类对象-----区别------self代表实例对象），并且用此来调用类属性：cls.类属性名

　　*静态方法与类方法都可以通过类或者实例来调用。其两个的特点都是不能够调用实例属性
