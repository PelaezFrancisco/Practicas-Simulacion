import random
import matplotlib.pyplot as plt
import numpy as np
import json

numlist = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
for i in range(1000):
  sum=0
  sum = random.randint(1,6)+random.randint(1,6)
  numlist[str(sum)] = numlist[str(sum)]+1
x = np.array(['2','3','4','5','6','7','8','9','10','11','12'])
plot_list=[]
for i in range(11): plot_list.append(numlist[str(i+2)])
y = np.array(plot_list)
plt.bar(x,y)
plt.show()