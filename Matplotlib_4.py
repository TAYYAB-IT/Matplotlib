import numpy as np
import matplotlib.pyplot as plt
######Draw a Histogram ######33
#To get random values for normal distribution
#np.random.normal(one_given_value,Standard Deviation,values required)
#x=np.random.normal(80,10,40)
#print(x)
# it will give 40 values ,closest to 80 with Standard Deviation=10
#plt.hist(x,color='green')
#plt.show()

#########Pie Chart #############
#x=np.random.randint(100,size=(5)) # will give 5 random values from 0 to 100 (integer)
#label=['PK','AUS','IND','AFG','BAN']
#for id,val in enumerate(x):
#    print(label[id],'=',val)
#color=['Green','Cyan','Yellow','magenta','Blue']
#explodes=[0.2,0,0,0,0]
#plt.pie(x,labels=label,colors=color,startangle=90,explode=explodes,shadow=True,autopct='%1.0f%%')
# autopct= is used to print %tage of every pie part
 #Angle of pie chart will be started from 90 degree
#plt.legend(title="5 Countries")
#plt.show()