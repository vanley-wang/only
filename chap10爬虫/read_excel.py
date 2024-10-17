import openpyxl
"""从网页中爬取的景区天气中的excel读取信息"""
workbook=openpyxl.load_workbook('天气表.xlsx')
sheet=workbook['天气表']
lst=[]
for row in sheet.rows:
    sublst=[]
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)
print(lst)
