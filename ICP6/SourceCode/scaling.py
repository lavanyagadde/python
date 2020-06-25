# scaling, PCA and bonus Questions
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
# reading the data from file
cc_dataset = pd.read_csv('CC.csv')

# finding the null values
nullvalues = cc_dataset.isnull().sum()
print(nullvalues)
print('***********')
cc_dataset.fillna(cc_dataset.mean(), inplace=True)
print(cc_dataset.isnull().sum())
print('*************')
x = cc_dataset.iloc[:, 1:-1]
y = cc_dataset.iloc[:, -1]
print(x.shape,y.shape)

# task 3: scaling
scaler = StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)
# predict the cluster for each data point
km = KMeans(n_clusters=2)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('Silhouette score:', score)

# task 4: Applying PCA
from sklearn.decomposition import PCA
pca = PCA(2)
X_pca = pca.fit_transform(X_scaled)
df2 = pd.DataFrame(data=X_pca)
finaldf = pd.concat([df2, cc_dataset[['TENURE']]],axis=1)
print(finaldf)
print(' ********************* ')

# bonus Questions1: kmeans algorithm on the PCA result
# finding null values
print(finaldf.isnull().sum())
x1 = finaldf.iloc[:,1:-1]
y1 = finaldf.iloc[:-1]
km1 = KMeans(n_clusters=3, random_state=0)
km1.fit(x1)
y_cluster_kmeans1 = km1.predict(x1)
print('Silhouette score after applying scale and PCA: ', metrics.silhouette_score(x1, y_cluster_kmeans1))

# bonus Questions2: Visualize the clustering of first bonus question
plt.scatter(finaldf.iloc[:, 0], finaldf.iloc[:, 1],finaldf.iloc[:, 2], c=y_cluster_kmeans1)
plt.show()
