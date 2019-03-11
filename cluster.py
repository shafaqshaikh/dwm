# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,[3,4]]



from sklearn.cluster import KMeans
WCSS=[]

for i in range(1,11):
    kMeans = KMeans(n_clusters= i,init = 'k-means++' , max_iter=300,n_init=10 ,
        random_state=0)
    kMeans.fit(X)
    WCSS.append(kMeans.inertia_)
    
plt.plot(range(1,11),WCSS)
plt.title('The Elbow Method')
plt.xlabel('Numbers of clusters')
plt.ylabel('WCSS')
plt.show()

 kMeans = KMeans(n_clusters= 5 ,init = 'k-means++' , max_iter=300,n_init=10 ,
        random_state=0)
       
 plt.scatter(X[y_kmeans==0,0],
 X[y_kmeans==0,1],s=100, c='blue',
 label='carefull')
           
 plt.scatter(X[y_kmeans==1,0],
 X[y_kmeans==1,1],s=100, c='red',
 label='Standard')
 
 plt.scatter(X[y_kmeans==2,0],
 X[y_kmeans==2,1],s=100, c='green',
 label='target')
 
 plt.scatter(X[y_kmeans==3,0],
 X[y_kmeans==3,1],s=100, c='cyan',
 label='careless')
 
 plt.scatter(X[y_kmeans==4,0],
 X[y_kmeans==4,1],s=100, c='magenta',
 label='Sensible')
 
 plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1]
 s=300, c='yellow' , label= 'centroids')
 
plt.title('clusters of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending Score(1-100)')
 
plt.legend()
plt.show()
 
 
 
 
   

