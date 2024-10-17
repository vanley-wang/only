import pandas as pd
import  matplotlib.pyplot as plt
df=pd.read_excel('天气表.xlsx')
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(10,6))
label=df['景区']
y=df['旅游人数']
plt.pie(y,labels=label,autopct='%1.1ff%%',startangle=90)
plt.axis('equal')
plt.title('2024-8各景区旅游人数')
plt.show()