import openpyxl

wb = openpyxl.load_workbook("E:/Code/Python/1stPythonEntry/venv/MyTestCode/Output/Sample.xlsx")

# 打印Workbook数据类型
#print(type(wb))

# 获取所有工作列表
#print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet1')

for i in range(1,8,1):
    print(sheet.cell(i, 2).value)
