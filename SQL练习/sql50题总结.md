1、select *,c.*,c_id as cid,s_name '学生',s_score 分数，distinct t_name 有多种显示方式和别名形式。别名使用要注意范围，括号内与括号外的应用范围不同。
2、数据库连接有 join、left join、inner join 后面要加连接的关键字 on a.c_id=b.c_id
3、条件连接where，比较条件有=，like（s_name like '%风%')。
4、用统计（count，AVg）一定要用group by，where 要用在group by 之前。
5、group by s_id,s_name,c_id 可以用多个字段同时进行分组，主分组是第一个
6、在group by出现的字段可以被select 出来，如果select 中含有不是group by的字段，严格时会出错。
7、group by 的字段，查询后只保留不同的值，同值都给并掉。
8、order by c_id desc,s_scor asc 可以用多字段排序，默认asc(升序)，desc(降序)。
9、排序后由条件选择记录： limit 0,1(第一行，1条记录)，limit 1,2(第2，3行，2条记录)。
10、函数：max、avg、count。例子：sum(case when score>60 then 1 else 0 end)；count(case when score>60 then 1 else null end)用"null"其他值会被统计；max(case when sc.c_id='01' then sc.s_score else null end)'01'；max(case when m=1 then s_score else null end)'第一'（排序后选择第一的值）。
11、row_number()按顺序排序，值相等序号不等（90，89，89，78）（1，2，3，4);dense_rank()重复值后排序为3：（90，89，89，78）（1，2，2，3）;rank() 重复值后的数值序号为4，（90，89，89，78）（1，2，2，4)。
12、row_number() over(order by s_score desc)正常排序；row_number() over(partition by c_id order by s_score)，可分组后进行组内排序。
13、由于sqlite3不支持日期等其他高级函数，所以函数有待了解。