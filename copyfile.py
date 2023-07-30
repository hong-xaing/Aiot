# import pandas as pd

# # 讀取CSV文件
# df = pd.read_csv('//Users//lvhongxiang//Documents//毒品分析//a85eb04185242dd82bf3db71756eb6da_export.csv', encoding='utf-8')



# # 將數據保存為XLSX文件
# df.to_excel('output.xlsx', index=False, encoding='utf-8')


import csv
from openpyxl import Workbook

# 讀取CSV文件
# a= "111"
with open('//Users//lvhongxiang//Documents//大專分析//A17000000J-030144-MKw.csv', 'r', encoding='utf-8') as file:
    csv_data = list(csv.reader(file))

# 創建一個新的XLSX文件
workbook = Workbook()
sheet = workbook.active

# 寫入CSV數據到XLSX文件
for row in csv_data:

    sheet.append(row)

# 保存XLSX文件
workbook.save('職場分析3.xlsx')