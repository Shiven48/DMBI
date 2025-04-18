import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.rand(200),
    'y': np.random.rand(200)
})

# Parameters
grid_size = 10
threshold = 5

# Bin data
data['x_bin'] = pd.cut(data['x'], bins=grid_size, labels=False)
data['y_bin'] = pd.cut(data['y'], bins=grid_size, labels=False)

# Count points in each grid cell
grid_counts = data.groupby(['x_bin', 'y_bin']).size().reset_index(name='count')

# Identify dense units
dense_units = grid_counts[grid_counts['count'] >= threshold]
print("Dense units (grid cells with ≥ threshold points):")
print(dense_units)

# Visualize data and grid
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(data['x'], data['y'], alpha=0.6)

# Plot grid
for i in range(1, grid_size):
    ax.axhline(i / grid_size, color='gray', linestyle='--', linewidth=0.5)
    ax.axvline(i / grid_size, color='gray', linestyle='--', linewidth=0.5)

plt.title("CLIQUE-style Grid Binning")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
