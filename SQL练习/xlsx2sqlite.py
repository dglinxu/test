import openpyxl
import sqlite3

conn=sqlite3.connect('待装总表.db')
c=conn.cursor()


def creat_table(tb,title): 
    #由表头生成制定表名的字段名
    titles=','.join(title)
    sql='CREATE TABLE IF NOT EXISTS %s(%s)'%(tb,titles)
    c.execute(sql)
    conn.commit()

def entry_data(tb,data): 
    #输入数据，添加到表中
    sql=f"INSERT INTO {tb} values(?,?,?,?,?,?,?,?)"
    c.execute(sql,data)
    conn.commit()

def read_from_db(tb):
    #读取第一行数据并打印
    sql=f"SELECT * FROM {tb}"
    c.execute(sql)
    data=c.fetchone()
    print(data)

def del_update(tb): 
    # 删除或更新制定数据，未完善
    sql='select * from %s'%(tb)
    c.execute(sql)
    sql="delete from %s where 营销中心='营销中心'"%(tb)
    c.execute(sql)
    conn.commit()

def read_xlsx(fname): 
    wb=openpyxl.load_workbook(fname)
    ws=wb.worksheets[0]
    for index,row in enumerate(ws.rows): 
        if index==0: 
            # print('生成数据库')
            # title=tuple(map(lambda x:str(x.value)+' text',row))
            # with sqlite3.connect('待装总表.db') as conn: 
            #     c=conn.cursor()
            #     creat_table(tb,title)
            continue
        row_data=tuple(map(lambda x:x.value,row))
        yield row_data


def xlsx2SQL(fname,tb):
    # 打开目标电子表格，对第一个表的数据进行导入处理,用生成器输入数据效率较高
    
    # with sqlite3.connect('待装总表.db') as conn: 
    #     c=conn.cursor()
    #     sql=f"INSERT INTO {tb} values(?,?,?,?,?,?,?,?)"
    #     c.executemany(sql,read_xlsx(fname))
    wb=openpyxl.load_workbook(fname)
    ws=wb.worksheets[0]
    for i,row in enumerate(ws.rows): 
        ##第一行是表头，生成表头元组，要加字段属性TEXT,并提交生成数据表
        if i==0: 
            # continue
            title=tuple(map(lambda x:str(x.value)+' text',row))
            creat_table(tb,title)
            continue
        # 利用函数取单元格的数值，生成一行元组数据
        # row_data=tuple(map(lambda x:x.value,row))
        # entry_data(tb,row_data)        
    
    conn.close()

fname='待装测试数据.xlsx'
tb='待装设计回复'
xlsx2SQL(fname,tb)
# del_update(tb)
# read_from_db(tb)