import sqlite3
conn=sqlite3.connect('test.db')
c=conn.cursor()

def create_table(): 
    sql='CREATE TABLE IF NOT EXISTS students(rollno int,name text,class int) '
    c.execute(sql)


def data_entry(): 
    sql=r"INSERT INTO students values(2016002,'孙小美',50289)"
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry(): 
    sql=r"INSERT INTO students(rollno,name,class) values(?,?,?)"
    records = [(1, 'Alen', 8),
           (2, 'Elliot', 9),
           (3, 'Bob', 7)]

    c.executemany(sql,records)
    conn.commit()

def read_from_db(): 
    # sql=r"SELECT * FROM students WHERE name='孙悟空' AND class=50289"
    sql="SELECT name,rollno FROM students WHERE name='孙悟空' AND rollno=2016003"
    c.execute(sql)
    data=c.fetchall()
    for row in data: 
        print(row)
    print(c.lastrowid)

def del_update(): 
    sql="SELECT * FROM students"
    c.execute(sql)
    # sql="UPDATE students set rollno=2016005 where name='孙悟空'"
    # c.execute(sql)
    sql="DELETE FROM students where name='大老千'"
    c.execute(sql)
    conn.commit()

# create_table()
# data_entry()
# for n in ['钱夫人','大老千','孙悟空','猪八戒','唐僧','沙和尚']: 
#     no=2016002+1
#     class=50289c
#     dynamic_data_entry(no,n,class)
read_from_db()
# del_update()
# dynamic_data_entry()
c.close()
conn.close()
