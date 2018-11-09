import matplotlib.pyplot as plot
import numpy as np
import  pandas as pd

num = 10
posi = pd.read_excel('test2.xlsx')
man = np.array(posi['MALE'][0:10])
fman = np.array(posi['FEMALE'][0:num])

labels = ['MALE','FEMALE']
size = [man,fman]
colors = ['red','blue']
explode = (0.05,0)
patches, l_text, p_text = plot.pie(size, explode=explode, labels=labels, colors=colors,
                                       labeldistance=1.1, autopct='%2.0f%%', shadow=False,
                                       startangle=90, pctdistance=0.6)

plot.axis('equal')
plot.legend(loc="upper left", bbox_to_anchor=(-0.1, 1))
plot.grid()
plot.show()