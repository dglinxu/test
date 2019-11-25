import openpyxl
wb=openpyxl.load_workbook('t1.xlsx')
ws=wb.sheetnames
lam
print(ws)