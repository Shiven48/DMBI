import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Number of clusters (excluding noise)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print("Estimated clusters:", n_clusters)
print("Estimated noise points:", n_noise)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot DBSCAN clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='Accent', edgecolors='k')
plt.title("DBSCAN Clustering (PCA-Reduced)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.show()
