import sqlite3
conn=sqlite3.connect('测试数据库.db')
c=conn.cursor()

def create_table(): 
    sql='CREATE TABLE IF NOT EXISTS students(rollno int,name text,class int) '
    c.execute(sql)
create_table()
