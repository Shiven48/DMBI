import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Combine into a DataFrame for training
train_df = X_train.copy()
train_df['class'] = y_train

# Function to compute class-wise statistics
def summarize_by_class(df):
    summaries = {}
    for class_value in df['class'].unique():
        class_df = df[df['class'] == class_value]
        summaries[class_value] = {
            'mean': class_df.iloc[:, :-1].mean(),
            'std': class_df.iloc[:, :-1].std(ddof=0) + 1e-6,  # add epsilon to avoid div by zero
            'prior': len(class_df) / len(df)
        }
    return summaries

# Gaussian probability density function
def gaussian_prob(x, mean, std):
    exponent = np.exp(- ((x - mean) ** 2) / (2 * std ** 2))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

# Prediction function
def predict(summaries, row):
    probabilities = {}
    for class_value, class_stats in summaries.items():
        prior = np.log(class_stats['prior'])
        likelihood = 0
        for feature in row.index:
            prob = gaussian_prob(row[feature], class_stats['mean'][feature], class_stats['std'][feature])
            likelihood += np.log(prob)
        probabilities[class_value] = prior + likelihood
    return max(probabilities, key=probabilities.get)

# Train
summaries = summarize_by_class(train_df)

# Predict on test set
y_pred = X_test.apply(lambda row: predict(summaries, row), axis=1)

# Evaluation
acc = accuracy_score(y_test, y_pred)
print(f"Manual Naive Bayes Accuracy: {acc:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap='YlGnBu', fmt='d',
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title("Confusion Matrix (Manual Naive Bayes)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
