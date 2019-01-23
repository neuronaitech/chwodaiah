# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:59:55 2018

@author: NANDAVARI
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
df=pd.read_csv('FB6.csv')

# Take useful feature and standardize them
X = df[['Open','High','Low','Close','Volume']]
n = preprocessing.StandardScaler()
np_scaled = n.fit_transform(X)
X_c = pd.DataFrame(np_scaled)
# reduce to 2 importants features
pca = PCA(n_components=2)
X_t = pca.fit_transform(X_c)
plt.scatter(X_t[:,0],X_t[:,1])
plt.show()

kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(X_c)
scores=kmeans.score(X_c)
print(scores)
#plt.scatter(kmeans,scores,color='orange')
#plt.show()

c1=kmeans.cluster_centers_
plt.scatter(X_t[:,0],X_t[:,1])
plt.scatter(c1[:,0],c1[:,1],color='r',marker='X')
#plt.scatter(X_t[:,0],X_t[:,1])
plt.show()

#calculate with different number of centroids to see the loss plot (elbow method)
n_cluster = range(1, 50)
kmeans = [KMeans(n_clusters=i).fit(X_c) for i in n_cluster]
scores = [kmeans[i].score(X_c) for i in range(len(kmeans))]
fig, ax = plt.subplots()
ax.scatter(n_cluster, scores,color='r')
plt.show()