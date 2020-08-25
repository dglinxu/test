#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/11 
#开发工具：PyCharm   文件名称：标尺draw函数.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def draw_line(tick_length,tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line='-'*tick_length
    if tick_label:
        line+=' '+tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""

    if center_length>0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
    """Draw English ruler with given number of inches,major tick length."""
    draw_line(major_length,'0')
    for i in range(1,num_inches+1):
        draw_interval(major_length)
        draw_line(major_length,str(i))

if __name__ == '__main__':
    length=3
    nums=3
    draw_ruler(nums,length)