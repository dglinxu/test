score=float(input('请输入成绩：'))
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='E'
print('你的分数是%.2f，等级是：%c'%(score,grade))
