class student(object):
    def input_score(self,number):
        student_number = int(input('请输入班级人数：'))
        print('**************')
        student_score = {}
        for i in range(student_number):
            name = str(input('第%d学生名字:' % (i+1)))
            student_score[name] = int(input('%s分数是：' % name))
            print('-----'*8)
        return student_score

    def score_average(self,score):
        sum = 0
        for i in score:
            sum += score[i]
        print('班级总分是：%d;班级平均分是：%.2f' % (sum, sum/len(score)))


if __name__ == '__main__':
    s=student()
    score = s.input_score(3)
    s.score_average(score)
