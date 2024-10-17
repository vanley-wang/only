import requests
import  re
url='https://www.weather.com.cn/weather1d/101010100.shtml'

resp=requests.get(url)
resp.encoding='utf-8'
print(resp.text)


city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)

print(city)
print(weather)
print(wd)
print(zs)
lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
for item in lst:
    print(item)