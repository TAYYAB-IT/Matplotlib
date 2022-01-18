import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
#x=np.array([2,4,6,8,10])
#y=np.array([4,16,36,64,100])
#pl.plot(x,y) #will draw graph
#pl.plot(x,y,'o') #will represent points
#pl.show()
#y=np.array([4,5,8,10])
#pl.plot(y) #just passing y axis values will take default consective values in x-axis starting from 0
#pl.show()

#z=pd.read_csv('data.csv')
#z.dropna(inplace=True)
#z.plot()
#pl.show()
########### Marker #################
#x=np.array([2,4,6,8,10])
#y=np.array([4,16,36,64,100])
#pl.plot(x,y,marker='o',ms=10,mec='red',mfc='cyan') # marker for marker # ms is marker size # mec is marker edge(outline) color # mfc is marker fill color
#pl.show()

############## Line ##################################
#x=np.array([2,4,6,8])
#y=np.array([3,6,9,12])
#pl.plot(x,y,ls='dashdot',lw=5,c='cyan')  # ls=line style(dashed,dotted,dashdot) #lw=line width # c=color of line
#pl.show()
data=pd.read_csv('data.csv')
data.dropna(inplace=True)
x=data['Duration']
y=data['Calories']
pl.plot(x,y,color='green',lw=3)
pl.xlabel("Duration")
pl.ylabel("Calories")
pl.suptitle("Calories Burnt-Duration")
pl.show()