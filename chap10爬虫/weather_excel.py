import weather_text
import openpyxl
"""从网页爬取的景区天气信息提取到创建的excel表中"""
html=weather_text.get_html()
lst=weather_text.html_parse(html)
workbook=openpyxl.Workbook()
sheet=workbook.create_sheet('天气表')
for item in lst:
   sheet.append(item)
workbook.save('天气表.xlsx')