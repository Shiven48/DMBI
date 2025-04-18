import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Same dataset
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter'],
    ['bread'],
    ['milk', 'butter'],
    ['milk'],
]

# Encode
te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

# FP-Growth
frequent_itemsets = fpgrowth(df, min_support=0.4, use_colnames=True)
print("Frequent Itemsets (FP-Growth):\n", frequent_itemsets)

# Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("\nFP-Growth Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
