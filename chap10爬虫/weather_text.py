import requests
import  re
""""创建两个函数，一个存储网页html，一个存储筛选的景区信息供后面使用"""
def get_html():
    url='https://www.weather.com.cn/weather1d/101010100.shtml'
    resp=requests.get(url)
    resp.encoding='utf-8'
    return resp.text
def html_parse(html):
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html)
    wd=re.findall('<span class="wd">(.*)</span>',html)
    zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html)
    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst



