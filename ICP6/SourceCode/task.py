# Kmeans, Null values, elbow method and silhouette score
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

# reading the data from file
cc_dataset = pd.read_csv('CC.csv')

# finding the null values
nullvalues = cc_dataset.isnull().sum()
print(nullvalues)

# task1a: As null values are present removing them using mean
cc_dataset.fillna(cc_dataset.mean(), inplace=True)
print('checking null values after removing :',cc_dataset.isnull().sum())

x = cc_dataset.iloc[:,1:-1]
y = cc_dataset.iloc[:,-1]
print(x.shape,y.shape)

# task 1b: Use the elbow method to find a good number of clusters with the KMeans algorithm
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print('*************')
print(wcss)

plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

# building the model KMeans
km = KMeans(n_clusters=2)
km.fit(x)
y_cluster_kmeans = km.predict(x)

# task 2: the silhouette score for the above clustering
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('silhouette score: ', score)

