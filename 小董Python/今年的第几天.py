import time
date=time.localtime()
year,month,day=date[:3]
month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year%400)==0 or (year%4==0 and ((year%100) !=0)):
    month_day[1]=29
if month==1:
    t=day
else:
    t=sum(month_day[:month-1])+day

print('今天是今年的第%d天！'%t)