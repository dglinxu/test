import sqlite3
conn=sqlite3.connect('50题测试数据库.db')
c=conn.cursor()

# 1.查询课程编号为“01”的课程比“02”的课程成绩高的所有学生的学号（重点）--inner join as on
# sql="select a.s_id,c.s_name,a.s_score,b.s_score from \
#     (select s_id,c_id,s_score from Score where c_id='01')as a inner join \
#         (select s_id,c_id,s_score from Score where c_id='02')as b on a.s_id=b.s_id \
#             inner join Student as c on c.s_id=a.s_id \
#                 where a.s_score>b.s_score"
# 第一题的扩展练习
# sql="select a.s_id,b.s_name,a.c_id,a.s_score from \
#     (select s_id,c_id,s_score from Score where c_id='01')as a inner join \
#        (select * from Student)as b where a.s_id=b.s_id"

#2、查询平均成绩大于60分的学生的学号和平均成绩（简单，第二道重点）--group by avg()
# sql="select s_id,avg(s_score) from Score group by s_id having avg(s_score)>60" 

# 3、查询所有学生的学号、姓名、选课数、总成绩（不重要）
# 有汇总、统计的情况要用group by,显示的字段就是gruop by字段
#注意sum的判断语句
# sql="select a.s_id,a.s_name,count(b.c_id),sum(b.s_score) from \
#     (select * from Student)as a inner join \
#         (select * from Score )as b on a.s_id=b.s_id group by a.s_id,a.s_name"
# sql="select a.s_id,a.s_name,count(b.c_id),\
#     sum(case when b.s_score is null then 0 else b.s_score end) from \
#     Student as a left join Score as b on a.s_id=b.s_id \
#         group by a.s_id,a.s_name"

# 4、查询姓“猴”的老师的个数（不重要）
# sql="select t_name,count(t_name) from Teacher \
#     where t_name like '张%' group by t_name"
# sql="select t_name,count(distinct t_name) from teacher \
#     where t_name like '张%'"  #distinct 是去重

# 5、查询没学过“张三”老师课的学生的学号、姓名（重点）
# sql="select c_id from course where \
#     t_id=(select t_id from teacher where t_name='张三')" #找到张三教的课
# sql="select s_id from score where \
#     c_id=(select c_id from course where \
#     t_id=(select t_id from teacher where t_name='张三'))" #学张三老师课的学生
# sql="select s_id,s_name from student where s_id not in \
#     (select s_id from score where \
#     c_id=(select c_id from course where \
#     t_id=(select t_id from teacher where t_name='张三')))"
# sql="select s.*,c.*,t.* from score as s inner join course as c on s.c_id=c.c_id \
#     inner join teacher as t on t.t_id=c.t_id where t.t_name='张三'" 
# sql="select s_id,s_name from student where s_id not in \
#     (select s.s_id from score as s inner join course as c on s.c_id=c.c_id \
#     inner join teacher as t on t.t_id=c.t_id where t.t_name='张三')"

# 6、查询学过“张三”老师所教的所有课的同学的学号、姓名（重点）
# sql="select s_id,s_name from student where s_id in (select s_id from score where c_id=\
#     (select c_id from course where t_id=\
#     (select t_id from teacher where t_name='张三')))" #用 in ?
# sql="select a.s_id,a.s_name from student as a \
#     inner join score as b on a.s_id=b.s_id \
#         inner join course as c on b.c_id=c.c_id \
#             inner join teacher as d on d.t_id=c.t_id where d.t_name='张三'"

# 7、查询学过编号为“01”的课程并且也学过编号为“02”的课程的学生的学号、姓名（重点）
# sql="select s_id,s_name from student where s_id in \
#     (select a.s_id from (select s_id from score where c_id='01') as a inner join \
#     (select s_id from score where c_id='02') as b on a.s_id=b.s_id)"
 
# 8、查询课程编号为“02”的总成绩（不重点）
# sql="select c_id,sum(s_score) from score where c_id='02' "
# sql="select c_id,sum(s_score) from score group by c_id having c_id='02'"

# 9、查询所有课程成绩小于60分的学生的学号、姓名
# sql="select s_id,s_name from student where s_id in \
    # (select s_id from score group by s_id having s_score<60)" #结果相同
# sql="select a.s_id,t.s_name from \
#     (select s_id,count(c_id) as cnt from score where s_score<60 group by s_id) as a \
#     inner join (select s_id,count(c_id) as cnt from score group by s_id) as b on a.s_id=b.s_id \
#         inner join student as t on a.s_id=t.s_id where a.cnt=b.cnt"

# 10.查询没有学全所有课的学生的学号、姓名(重点)
# sql="select s_id,s_name from student where s_id in \
#     (select s_id from score group by s_id having count(distinct c_id)<\
#         (select count(distinct c_id) from course))"
# sql="select st.s_id,st.s_name from student as st left join score as s on st.s_id=s.s_id \
#     group by s.s_id having count(distinct s.c_id)<\
#         (select count(distinct c_id) from course)"

# 11、查询至少有一门课与学号为“01”的学生所学课程相同的学生的学号和姓名（重点）
# sql="select s_id,s_name from student where s_id in (select distinct s_id from score where c_id in \
#     (select s_id from score where s_id='01')and s_id !='01')" #有AND 和 distinct 

# 12.查询和“01”号同学所学课程完全相同的其他同学的学号(重点)
# 错误做法
# sql="select s_id from score where s_id in (select s_id from score where c_id in \
#     (select c_id from score where s_id='01') and s_id!='01' \
#         group by s_id having count(distinct c_id)=\
#             (select count(distinct c_id) from score where s_id='01')) \
#                 group by s_id having count(distinct c_id)=\
#                     (select count(distinct c_id) from score where s_id='01')"
# sql="select s_id,s_name from student where s_id in \
#     (select s_id from score where s_id !='01' group by s_id having \
#         count(distinct c_id)=(select count(distinct c_id) from score where s_id='01'))\
#             and s_id not in\
#         (select s_id from score where c_id not in \
#     (select c_id from score where s_id='01'))"

# 13、查询没学过"张三"老师讲授的任一门课程的学生姓名 和47题一样（重点，能做出来）
# sql="select s_id,s_name from student where s_id not in \
#     (select s_id from score where c_id in \
#     (select c_id from course where t_id=\
#     (select t_id from teacher where t_name='张三')))"

# 15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩（重点）
# sql="select a.s_id,a.s_name,avg(b.s_score) from student as a inner join \
#     score as b on a.s_id=b.s_id where a.s_id in \
#     (select s_id from score where s_score<60 group by \
#         s_id having count(distinct c_id)>1) \
#             group by a.s_id,a.s_name"

# 16、检索"01"课程分数小于60，按分数降序排列的学生信息（和34题重复，不重点）
# sql="select a.s_id,a.s_name,b.s_score from student as a \
#     inner join score as b on a.s_id=b.s_id \
#         where b.c_id='01' and b.s_score<60 \
#             order by b.s_score desc" #升序asc 降序desc

# 17、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩(重重点与35一样)
# sql="select a.s_id,a.s_score,avg_score from score as a \
#     inner join (select s_id,avg(s_score) as avg_score from score \
#         group by s_id) as b on a.s_id=b.s_id\
#              order by avg_score desc"
# sql="select s_id'学号',\
#     max(case when c_id='01' then s_score else null end)'语文',\
#     max(case when c_id='02' then s_score else null end)'数学',\
#     max(case when c_id='03' then s_score else null end)'英语',\
#     avg(s_score)'平均分'\
#     from score group by s_id order by avg(s_score) desc"

# 18.查询各科成绩最高分、最低分和平均分：以如下形式显示：\
# 课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率\
# --及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90 (超级重点)
# sql="select s.c_id,c.c_name,max(s.s_score),min(s.s_score),avg(s.s_score),\
#     sum(case when s.s_score>=60 then 1 else 0 end)/count(s.s_id),\
#     sum(case when s.s_score>=70 and s.s_score<80 then 1 else 0 end)/count(s.s_id),\
#     sum(case when s.s_score>=80 and s.s_score<90 then 1 else 0 end)/count(s.s_id),\
#     sum(case when s.s_score>=90 then 1 else 0 end)/count(s.s_id) \
#     from score as s inner join course as c on s.c_id=c.c_id group by c.c_id "

# 19、按各科成绩进行排序，并显示排名(重点row_number)row_number(）over （order by 列）
# row_number()按顺序排序，值相等序号不等（90，89，89，78）（1，2，3，4）
# dense_rank()重复值后排序为3：（90，89，89，78）（1，2，2，3）
# rank() 重复值后的数值序号为4，（90，89，89，78）（1，2，2，4）
# sql="select s_id,c_id,s_score,\
#     row_number() over(order by s_score desc) from score"

# 20、查询学生的总成绩并进行排名（不重点）
# sql="select s_id,sum(s_score),rank() over(order by sum(s_score) desc) \
#     from score group by s_id"

#21 、查询不同老师所教不同课程平均分从高到低显示(不重点)
# sql="select t.t_name,c.c_id,c.c_name,avg(s.s_score) as avg_1 from score as s \
#     inner join course as c on c.c_id=s.c_id \
#     inner join teacher as t on t.t_id=c.t_id\
#     group by s.c_id order by avg_1 desc"

# 22、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩（重要 25类似）
# sql="select * from (select st.s_id,st.s_name,sc.c_id,sc.s_score,\
#     row_number() over(partition by c_id order by s_score) m \
#     from score as sc inner join student as st on st.s_id=sc.s_id) \
#     where m in (2,3) "

# 23、使用分段[100-85],[85-70],[70-60],[<60]来统计各科成绩，
# 分别统计各分数段人数：课程ID和课程名称(重点和18题类似)
# 如果用count，else 后跟null,不要为0，o也是要计数的
# sql="select s.c_id,c.c_name,\
#     sum(case when s.s_score<=100 and s.s_score>=85 then 1 else 0 end),\
#     sum(case when s.s_score<85 and s.s_score>=70 then 1 else 0 end),\
#     sum(case when s.s_score<70 and s.s_score>=60 then 1 else 0 end),\
#     count(case when s.s_score<60 then 1 else null end)\
#     from score as s inner join course as c on c.c_id=s.c_id \
#     group by c.c_id,c.c_name" 

# 24、查询学生平均成绩及其名次（同19题，重点）
# sql="select s_id,avg(s_score),\
#     row_number() over(order by avg(s_score) desc)\
#     from score"
# sql="select s_id,avg(s_score),\
#     row_number() over(order by avg(s_score) desc) \
#     from score group by s_id"

# 25、查询各科成绩前三名的记录（不考虑成绩并列情况）（重点 与22题类似）
# sql="select c_id,c_name,\
#     max(case when m=1 then s_score else null end)'第一',\
#     max(case when m=2 then s_score else null end)'第二',\
#     max(case when m=3 then s_score else null end)'第三'\
#     from (select s.c_id,s.s_score,c.c_name,\
#     row_number() over(partition by s.c_id order by s.s_score) m \
#     from score as s inner join course as c on s.c_id=c.c_id) \
#     where m in (1,2,3)\
#     group by c_id,c_name"
    
# 26、查询每门课程被选修的学生数(不重点)
# sql="select c.c_id,c.c_name,count(distinct s.s_id) ct \
#     from score as s inner join course as c on s.c_id=c.c_id \
#     group by c.c_id,c.c_name"

# 27、 查询出只有两门课程的全部学生的学号和姓名(不重点)
# sql="select st.s_id,st.s_name,count(distinct sc.c_id) ct from score as sc \
#     inner join student as st on st.s_id=sc.s_id \
#     group by st.s_id,st.s_name having ct=2"
# sql="select s_id,s_name,2 from student \
#     where s_id in \
#     (select s_id from score group by s_id having count(distinct c_id)=2)"

# 28、查询男生、女生人数(不重点)
# sql="select sum(case when s_sex='男' then 1 else 0 end)'男生',\
#     sum(case when s_sex='女' then 1 else 0 end)'女生'\
#     from student"
# sql="select s_sex,count(s_sex) from student group by s_sex"

# 29 查询名字中含有"风"字的学生信息（不重点）
# sql="select s_id,s_name,s_sex,s_birth from student where s_name like '%风%'"

# 30、查询同名同姓学生名单并统计同名人数
# sql="select s_name,count(*) from student group by s_name having count(*)>1"
# sql="select s_name,count(*) from student group by s_name having s_name like '赵%'"
# sql="update student set s_name='赵风' where s_name='孙风'"

# 31、查询1990年出生的学生名单（重点year）
# sql="select s_id,s_name,s_birth,s_sex from student \
#     where s_birth like '1990%'"
# sql="select * from student where YEAR(s_birth)=1990" #不支持YEAR

# 32、查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩（不重要）
# sql="select st.s_id,st.s_name,avg_s from student as st inner join \
#     (select sc.s_id,avg(sc.s_score) as avg_s from score as sc\
#     group by sc.s_id having avg_s>=85) as a on st.s_id=a.s_id"
# sql="select st.s_id,st.s_name,avg(sc.s_score) a from student as st \
#     inner join score as sc on st.s_id=sc.s_id \
#     group by st.s_id,st.s_name \
#     having a>=85 order by a desc"

# 33、查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列（不重要）
# sql="select c_id,avg(s_score) avg_score from score \
#     group by c_id order by avg_score desc,c_id desc"

# 34、查询课程名称为"数学"，且分数低于60的学生姓名和分数（不重点）
# sql="select c.c_id,c.c_name,st.s_name,sc.s_score from course as c \
#     inner join score as sc on sc.c_id=c.c_id \
#     inner join student as st on sc.s_id=st.s_id \
#     where sc.s_score<60 and c.c_name='数学'"
# sql="select st.s_name,a.s_score from student as st inner join \
#     (select s_id,s_score from score as sc where sc.s_score<60 and \
#     (sc.c_id=(select c.c_id from course as c where c.c_name='数学'))) as a\
#     on st.s_id=a.s_id"

# 35、查询所有学生的课程及分数情况（重点）
# sql="select s_id,\
#     max(case when c_id='01' then s_score else null end)'01',\
#     max(case when c_id='02' then s_score else null end)'02',\
#     max(case when c_id='03' then s_score else null end)'03'\
#     from score group by s_id order by s_id"
# 用left join 否则漏了无成绩的学生
# sql="select st.s_id,st.s_name,\
#     max(case when sc.c_id='01' then sc.s_score else null end)'01',\
#     max(case when sc.c_id='02' then sc.s_score else null end)'02',\
#     max(case when sc.c_id='03' then sc.s_score else null end)'03'\
#     from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#      group by st.s_id,st.s_name"

# 36、查询任何一门课程成绩在70分以上的姓名、课程名称和分数（重点）
# sql="select st.s_id,st.s_name,c.c_name,sc.s_score from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     inner join course as c on sc.c_id=c.c_id \
#     where sc.s_score>70"

# 37、查询不及格的课程并按课程号从大到小排列(不重点)
# sql="select st.s_id,st.s_name,c.c_name,sc.s_score from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     inner join course as c on sc.c_id=c.c_id \
#     where sc.s_score<60 order by sc.c_id desc,sc.s_score "

# 38、查询课程编号为03且课程成绩在80分以上的学生的学号和姓名（不重要）
# sql="select sc.c_id,st.s_id,st.s_name,sc.s_score from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     where sc.s_score>80 and sc.c_id='03'\
#     order by sc.s_id"

# 39、求每门课程的学生人数（不重要）
# sql="select c_id,count(distinct s_id) from score group by c_id"

# 40、查询选修“张三”老师所授课程的学生中成绩最高的学生姓名及其成绩（重要top）
# 降序排序后用 limit 0,1 选出第一行，一条记录，limit 0,2 第1，2 行两条记录
# sql="select sc.s_id,st.s_name,max(sc.s_score) from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     inner join course as c on c.c_id=sc.c_id \
#     inner join teacher as t on c.t_id=t.t_id \
#     where t.t_name='张三'"
# sql="select sc.s_id,st.s_name,max(sc.s_score) from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     inner join course as c on c.c_id=sc.c_id \
#     inner join teacher as t on c.t_id=t.t_id \
#     where t.t_name='张三' \
#     group by c.c_id"
# sql="select sc.s_id,st.s_name,sc.s_score from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     inner join course as c on c.c_id=sc.c_id \
#     inner join teacher as t on c.t_id=t.t_id \
#     where t.t_name='张三' \
#     order by sc.s_score DESC limit 0,1"

# 41、查询各个课程及相应的选修人数
# sql="select c.c_id,c.c_name,count(distinct s.s_id) from course as c \
#     left join score as s on c.c_id=s.c_id\
#     group by c.c_id,c.c_name"

# 42.查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩 （重点）
# 三门成绩都一样的学生，语数英成绩一样，不是不同学生的成绩一样
#留意只有一门成绩的情况
# sql="select * from (select sc.s_id,sc.s_score from score sc \
#     inner join (select s_id from score group by s_id having count(c_id)>1)a on sc.s_id=a.s_id\
#     group by sc.s_id,sc.s_score) b\
#     group by b.s_id having count(b.s_score)=1"

# 43、查询每门功成绩最好的前两名（同22和25题）
# sql="select c_id,c_name,\
#     max(case when m=1 then s_score else null end)'第一',\
#     max(case when m=2 then s_score else null end)'第二'\
#     from (select s.c_id,s.s_score,c.c_name,\
#     row_number() over(partition by s.c_id order by s.s_score desc) m \
#     from score as s inner join course as c on s.c_id=c.c_id) \
#     where m in (1,2)\
#     group by c_id,c_name"

# 44、统计每门课程的学生选修人数（超过5人的课程才统计）。
# 要求输出课程号和选修人数，查询结果按人数降序排列，
# 若人数相同，按课程号升序排列（不重要）
# sql="select c_id,count(distinct s_id) ct from score \
#     group by c_id having ct>5 \
#     order by ct desc,c_id asc"

# 45、检索至少选修两门课程的学生学号（不重要）
# sql="select s_id,count(distinct c_id)  ct from score \
#     group by s_id having ct>1 order by s_id"

# 46、 查询选修了全部课程的学生信息（重点划红线地方）
# sql="select s_id,count(distinct c_id) from score \
#     group by s_id \
#     having count(c_id)=(select count(distinct c_id) from course)"

# 47、查询没学过“张三”老师讲授的任一门课程的学生姓名
# （还可以，自己写的，答案中没有）
# sql="select s_id,s_name from student where s_id not in \
#     (select st.s_id from student as st \
#     left join score as sc on st.s_id=sc.s_id \
#     where sc.c_id  in \
#     (select c.c_id from course as c\
#     inner join teacher as t on c.t_id=t.t_id \
#     where t.t_name='张三'))"

# 48、查询两门以上不及格课程的同学的学号及其平均成绩
# （还可以，自己写的，答案中没有）
# sql="select * from score as a inner join (select b.s_id,avg(b.s_score) from score as b\
#     group by b.s_id \
#     having sum(case when b.s_score<60 then 1 else 0 end)>1) c\
#     on a.s_id=c.s_id"
# sql="select s_id as 学号, avg(s_score)as 平均成绩 from Score\
#     where s_score <60 \
#     group by s_id \
#     having count(c_id)>=2"

# 49、检索课程编号为“02”且分数小于60的学生学号，结果按按分数降序排列
# sql="select s_id,s_score from score where c_id='02' and s_score<60 order by s_score desc"

# 50、删除学生编号为“02”的课程编号为“01”的成绩
# sql="delete score where s_id='02' and c_id='01'"

# 46、查询各学生的年龄（精确到月份）
# sql="select s_id,s_name,s_birth,datediff(month,s_birth,'2020-02-08') \
#     from student"

c.execute(sql)
conn.commit()
datas=c.fetchall()
for data in datas: 
    print(data)
conn.close()

def create_table(): 
    # sql=r"CREATE TABLE IF NOT EXISTS Student(s_id VARCHAR(20),s_name VARCHAR(20) NOT NULL DEFAULT '',s_birth VARCHAR(20) NOT NULL DEFAULT '',s_sex VARCHAR(10) NOT NULL DEFAULT '',PRIMARY KEY(s_id))"
    # sql=r"CREATE TABLE IF NOT EXISTS Course(`c_id` VARCHAR(20),`c_name` VARCHAR(20) NOT NULL DEFAULT '',`t_id` VARCHAR(20) NOT NULL,PRIMARY KEY(`c_id`))"
    # sql="CREATE TABLE IF NOT EXISTS Teacher(`t_id` VARCHAR(20),`t_name` VARCHAR(20) NOT NULL DEFAULT '',PRIMARY KEY(`t_id`))"
    sql="CREATE TABLE IF NOT EXISTS Score(`s_id` VARCHAR(20),`c_id` VARCHAR(20),`s_score` INT(3),PRIMARY KEY(`s_id`,`c_id`))"
    c.execute(sql)
    conn.commit()
def data_entry(): 
    # sql="insert into Student values('01' , '赵雷' , '1990-01-01' , '男')"
    # sql="insert into Student values('02' , '钱电' , '1990-12-21' , '男')"
    # sql="insert into Student values('03' , '孙风' , '1990-05-20' , '男')"
    # sql="insert into Student values('04' , '李云' , '1990-08-06' , '男')"
    # sql="insert into Student values('05' , '周梅' , '1991-12-01' , '女')"
    # sql="insert into Student values('06' , '吴兰' , '1992-03-01' , '女')"
    # sql="insert into Student values('07' , '郑竹' , '1989-07-01' , '女')"
    # sql="insert into Student values('08' , '王菊' , '1990-01-20' , '女')"
    
    # sql0="insert into Course values('01' , '语文' , '02')"
    # sql1="insert into Course values('02' , '数学' , '01')"
    # sql2="insert into Course values('03' , '英语' , '03')"

    # sql3="insert into Teacher values('01' , '张三')"
    # sql4="insert into Teacher values('02' , '李四')"
    # sql5="insert into Teacher values('03' , '王五')"

    # sql6="insert into Score values('01' , '01' , 80)"
    # sql7="insert into Score values('01' , '02' , 90)"
    # sql8="insert into Score values('01' , '03' , 99)"
    # sql9="insert into Score values('02' , '01' , 70)"
    # sql10="insert into Score values('02' , '02' , 60)"
    # sql11="insert into Score values('02' , '03' , 80)"
    # sql12="insert into Score values('03' , '02' , 80)"
    # sql13="insert into Score values('03' , '03' , 80)"
    # sql14="insert into Score values('04' , '01' , 50)"
    # sql15="insert into Score values('04' , '02' , 30)"
    # sql16="insert into Score values('04' , '03' , 20)"
    # sql17="insert into Score values('05' , '01' , 76)"
    # sql18="insert into Score values('05' , '02' , 87)"
    # sql19="insert into Score values('06' , '01' , 31)"
    # sql20="insert into Score values('06' , '03' , 34)"
    # sql21="insert into Score values('07' , '02' , 89)"
    # sql22="insert into Score values('07' , '03' , 98)"
    c.execute(sql22)
    conn.commit()

# create_table()
# data_entry()
