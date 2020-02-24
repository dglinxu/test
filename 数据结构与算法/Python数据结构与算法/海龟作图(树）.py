'''海龟作图'''
import turtle
t=turtle.Turtle()
def tree(branch_len):
    if branch_len>5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15)
        t.left(40)
        tree(branch_len-15)
        t.right(20)
        t.backward(branch_len)
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(100)
t.hideturtle()
turtle.done()