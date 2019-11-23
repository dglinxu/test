score=[]
flag='yes'
while flag=='yes':
    num=input('请输入学生分数：')
    try:
        i=float(num)
    except:
        print('输入不是合法分数，请重新输入')
    if (0<=i<=100):
            score.append(i)
    else:
        print('输入的分数不在0-100的范围，请重新输入！')
        continue #后面的语句不执行，重新回到输入

    while True:
        flag=input('还继续输入吗？(Yes or No):').lower()
        if flag not in ('yes', 'no'):
            print('选择错误，请重新输入！')
        else:
            break


print('全班共%d人，平均分是：%4.2f'%(len(score),sum(score)/len(score)))