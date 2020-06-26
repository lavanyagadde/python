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
# PCA before scaling
x_pca = pca.fit_transform(x)
# PCA after scaling
X_pca_scaled = pca.fit_transform(X_scaled)

# bonus Questions1: kmeans algorithm on the PCA result
# PCA+KMEANS
km = KMeans(n_clusters=3)
km.fit(x_pca)
# predict the cluster for each data point
y_cluster_kmeans1= km.predict(x_pca)
print('Silhouette score for PCA+KMEANS : ', metrics.silhouette_score(x_pca, y_cluster_kmeans1))

# SCALING+PCA+KMEANS
km = KMeans(n_clusters=3)
km.fit(X_pca_scaled)
# predict the cluster for each data point
y_cluster_kmeans2= km.predict(X_pca_scaled)
print('Silhouette score for SCALING+PCA+KMEANS : ', metrics.silhouette_score(X_pca_scaled, y_cluster_kmeans2))

# bonus Questions2: Visualize the clustering of first bonus question
# PCA+KMEANS
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_cluster_kmeans1)
plt.show()

# SCALING+PCA+KMEANS
plt.scatter(X_pca_scaled[:, 0], X_pca_scaled[:, 1], c=y_cluster_kmeans2)
plt.show()