import openpyxl
wb=openpyxl.load_workbook(r'D:\Git\待装测试\test.xlsx')
ws=wb.worksheets[0]
for i,row in enumerate(ws.rows):
    
    print(s)
