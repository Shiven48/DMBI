import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Save to CSV
df.to_csv("iris_powerbi.csv", index=False)
print("Dataset saved as 'iris_powerbi.csv'. You can now import it into Power BI.")

# Instructions (in comments):
# 1. Open Power BI Desktop.
# 2. Click on 'Get Data' → 'Text/CSV'.
# 3. Load 'iris_powerbi.csv'.
# 4. Use 'target' as your dimension.
# 5. Use visual tools to create reports, charts, and dashboards.
