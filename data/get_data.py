import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from folium.plugins import  HeatMap

posi = pd.read_excel("test.xlsx")
num = 60

age = np.array(posi['年龄'][0:num])
weight = np.array(posi['体重'][0:num])

x = list(age)
y = list(weight)




plt.plot(x,y,'r--')
plt.xlim(10,25)
plt.ylim(40,60)
plt.xlabel('Age')
plt.ylabel('Weight')
plt.title("Weight By Age")

plt.show()
#print(type(age))


