
"""产生一个灰度图片"""
import numpy as np
import matplotlib.pyplot as plt
n1=plt.imread('logo2.jpg')
plt.imshow(n1)
n2=np.array([0.299,0.587,0.114,0])
x=np.dot(n1,n2)
plt.imshow(x,cmap='gray')
plt.show()