import xlrd
import os
# 获取文件路径
excel_path = os.path.dirname(__file__) + '/data.xls'

# 打开文件
readbook = xlrd.open_workbook(excel_path)

# 获取某一个sheet页
# 根据下标获取
sheet = readbook.sheet_by_index(0)
print(sheet)

# 根据名字获取
# sheet = readbook.sheet_by_name('sheet1')

# 获取所有sheet页的名字
name = readbook.sheet_names()
print(name)

# 获取最大行
max_row = sheet.nrows
print(max_row)

# 获取最大列
max_col = sheet.ncols
print(max_col)

# 获取某个单元格
cell_value = sheet.cell_value(0,0) #获取第一行第一列的数据
print(cell_value)

# 获取某一行的数据
row_value = sheet.row_values(0) # 获取第一行的数据
row_value1 = sheet.row_values(1)
print(row_value)
print(row_value1)

# 获取某一列的数据
col_value = sheet.col_values(0)
print(col_value)