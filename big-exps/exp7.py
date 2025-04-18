import networkx as nx
import matplotlib.pyplot as plt

# Create a Bayesian Belief Network using a Directed Acyclic Graph (DAG)
G = nx.DiGraph()

# Example variables (simplified student scenario)
nodes = ["Study", "Sleep", "Exam", "Grade", "Pass"]
edges = [("Study", "Exam"), ("Sleep", "Exam"), ("Exam", "Grade"), ("Grade", "Pass")]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Visualize the network
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, edge_color='gray', arrowsize=20, font_size=12)
plt.title("Bayesian Belief Network Example")
plt.show()

# Simulate CPDs (Conditional Probability Distributions)
cpds = {
    "Study": {"T": 0.7, "F": 0.3},
    "Sleep": {"T": 0.6, "F": 0.4},
    "Exam": {
        ("T", "T"): 0.9,
        ("T", "F"): 0.7,
        ("F", "T"): 0.6,
        ("F", "F"): 0.2
    },
    "Grade": {"Pass": 0.85, "Fail": 0.15},
    "Pass": {"High": 0.9, "Low": 0.3}
}

print("Conditional probabilities (CPDs):")
for node, probs in cpds.items():
    print(f"{node}: {probs}")
