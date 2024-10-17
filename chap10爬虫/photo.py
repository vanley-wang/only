import requests
"""爬取网页照片，并存储成png形式"""
url='https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1sdhWU.img?w=768&h=510&m=6&x=230&y=102&s=513&d=122'
resp=requests.get(url)
with open('photo.png','wb')as file:
    file.write(resp.content)