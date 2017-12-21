from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X=np.zeros([453,3])
Y=np.zeros([453,4])
#print(X)
month_dict={'Jan':1,'Feb':2,'Mar':'3','Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
csv_file=open('Final_data.csv','r')
data = list(csv.DictReader(csv_file))
i=0
for item in data:
    if(item['Latitide'] != 'Null'):
        X[i][0]=float(item['Latitide'])
        Y[i][0]=float(item['Latitide'])
    if(item['Longitude']!= 'Null'):
        X[i][1]=float(item['Longitude'])
        Y[i][1]=float(item['Longitude'])
    if(item['Start']!='Null'):
        X[i][2]=month_dict[item['Start']]
        Y[i][2]=month_dict[item['Start']]
    i=i+1
#print(X)
#print(X[:,0])
minlat=min(X[:,0])
maxlat=max(X[:,0])
minlong=min(X[:,1])
maxlong=max(X[:,1])
minmonth=1
maxmonth=12
#print(minlong)
#print(maxlong)
j=0
for item in X:
    X[j][0]=(X[j][0]-minlat)/(maxlat-minlat)
    X[j][1]=(X[j][1]-minlong)/(maxlong-minlong)
    X[j][2]=(X[j][2]-minmonth)/(maxmonth-minmonth)
    Y[j][0]=(Y[j][0]-minlat)/(maxlat-minlat)
    Y[j][1]=(Y[j][1]-minlong)/(maxlong-minlong)
    Y[j][2]=(Y[j][2]-minmonth)/(maxmonth-minmonth)
    j=j+1
#print('Below printing X')
print(X)
kmeans=KMeans()
kmeans.fit(X)
j=0
for i in X:
    lol = kmeans.predict([i])
    #print(lol)
    Y[j][3]=lol
    j=j+1
df = pd.DataFrame(Y, columns=['Feature1', 'Feature2','Feature3','Cluster'])
#print (df)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.array(df['Feature1'])
y = np.array(df['Feature2'])
z = np.array(df['Feature3'])
damn=['latitude','longitude','month']
ax.scatter(x,y,z, marker="s", c=df["Cluster"], s=40, label=damn,cmap="RdBu")
ax.set_xlabel('Latitide')
ax.set_ylabel('Longitude')
ax.set_zlabel('Month')
#start
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], centers[:,2],c='black', s=10, alpha=1)
#end
plt.show()