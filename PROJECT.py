import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('IT-19-A_Students List.csv')
marks=data['Marks']
#print(marks)
Grades=np.array([0,0,0,0,0,0,0,0,0])
for i in marks:
    if(i>=84.5):
        Grades[0]+=1
    elif(i>=79.5):
        Grades[1]+=1
    elif (i >= 74.5):
        Grades[2] += 1
    elif (i >= 69.5):
        Grades[3] += 1
    elif (i >= 64.5):
        Grades[4] += 1
    elif (i >= 59.5):
        Grades[5] += 1
    elif (i >= 54.5):
        Grades[6] += 1
    elif (i >= 49.5):
        Grades[7] += 1
    else:
        Grades[8] += 1
lable=['A+','A','B+','B','B-','C+','C','D','F']
for id,gr in enumerate(lable):
    print(gr,'=',Grades[id])
plt.pie(Grades,labels=lable,explode=[0.2,0,0,0,0,0,0,0,0],startangle=90,autopct='%1.0f%%') # autopct is used to print % on pie cahrt
plt.suptitle("IT-19-A_Grades List")
plt.legend(title="Grades")
plt.show()
#plt.bar(lable,Grades)
#plt.xlabel('Grades')
#plt.ylabel('No.Of Students')
#plt.suptitle('IT-19-A_Result',color="Green",size=22)
#plt.show()
print("Students Gained A+ Grades ",Grades[0],' Students')
for i in data.index:
    if data.loc[i,"Marks"] >=84:
        print(data.loc[i,'Roll No#'])

