#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/7 
#开发工具：PyCharm   文件名称：range类.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

#没有iter就能产生生成器
class Range:
    """自定义类"""

    def __init__(self,start,stop=None,step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        #要判断步长为零，及输入为负数的情况
        if step==0:
            raise ValueError('Step cannot be 0!')
        elif start<=0 and stop is None:
            raise  ValueError('输入参数错误！')


        if stop is None and start >0:
            start,stop=0,start

        #计算最大迭代次数
        self._length=max(0,(stop-start+step-1)//step)

        self._start=start
        self._step=step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k(using standard interpretation if negative)."""
        if k<0:
            k+=len(self)
        if not 0<=k<self._length:
            raise IndexError('索引越界。')

        return self._start+k*self._step

if __name__ == '__main__':
    myRange=Range(10)
    print(list(myRange))

    print(myRange[-1])   #getitem要用[]取数


