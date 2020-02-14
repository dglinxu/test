'''根据提供的班级号及人数，分别生成10个学生的学号，4位班级号+2位学生号'''
import random
def g_student_no(cs):
    class_no=random.choice(list(cs.keys()))
    student_no=random.randint(1,cs[class_no])
    return "{}{:02}".format(class_no,student_no)
    

    

if __name__=="__main__":
    cs={"A001":32,"A002":47,"B001":39,"B002":42}
    data=set()
    while len(data)<11:
        data.add(g_student_no(cs))
    print(data)