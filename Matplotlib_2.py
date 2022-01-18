import matplotlib.pyplot as plt
import numpy as np
 # Two line points (x1,y1) &(x2,y2)
#x1 = np.array([0, 1, 2, 3])
#y1 = np.array([3, 8, 1, 10])
#x2 = np.array([0, 1, 2, 3])
#y2 = np.array([6, 2, 7, 11])
#plt.plot(x1, y1, x2, y2)
#plt.show()
# Lables
#x_y_font={'family':'Serif','color':'blue','size':12}
#title_font={'family':'Serif','color':'green','size':18}
#x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt.plot(x, y,color='green',lw=6)
#plt.xlabel("Average Pulse",fontdict=x_y_font)
#plt.ylabel("Calorie Burnage",fontdict=x_y_font)
#plt.title("Pulse-Calories",fontdict=title_font,loc='left')
#Gridding
#plt.grid()
#plt.grid(axis='x')
#plt.grid(axis='y')
#plt.grid(lw=3,ls='dashdot',color='magenta')
#plt.show()


########## Subplots( more than one plots in one figure)
#plt.subplot(total rows , total coloumns, plot number)
#Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(3, 2, 1)
plt.plot(x,y)
plt.title('Pakistan')
#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(3, 2, 2)
plt.plot(x,y)
plt.title('India')
#Plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(3, 2, 3)
plt.plot(x,y)
plt.title('Bangladash')
#Plot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(3, 2, 4)
plt.plot(x,y)
plt.title('Srilanka')
# Plot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(3, 2, 5)
plt.plot(x,y)
plt.title('Afghanistan')
#Plot 6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(3, 2, 6)
plt.plot(x,y)
plt.title('Nepal')
plt.suptitle('Asian Countries')
plt.show()
