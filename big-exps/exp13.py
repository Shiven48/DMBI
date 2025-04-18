import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import Birch
from sklearn.decomposition import PCA

# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# BIRCH
birch_model = Birch(n_clusters=3)
birch_model.fit(X)
labels = birch_model.labels_

# PCA for plotting
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='tab10')
plt.title("BIRCH Clustering (PCA Projection)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.show()

print("Cluster labels assigned by BIRCH:", labels)
