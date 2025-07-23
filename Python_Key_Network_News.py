"""
Keyword Network from News Headlines
-----------------------------------
Builds a co-occurrence network from a list of news headlines.

Skills:
- Text preprocessing (tokenization, filtering)
- Counting co-occurrences
- Network graph creation with networkx
- Visualization with matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations

# Simulated news headlines list
headlines = [
    "Global markets rally on economic recovery",
    "Economic recovery boosts global stock markets",
    "New policies impact global economic growth",
    "Markets respond to new trade policies",
    "Stock markets face uncertainty amid trade tensions"
]

# Preprocess headlines: tokenize and lowercase
def preprocess(text):
    return [word.lower() for word in text.split()]

tokenized_headlines = [preprocess(h) for h in headlines]

# Build co-occurrence pairs within each headline
co_occurrence = Counter()
for tokens in tokenized_headlines:
    # Unique pairs without repetition
    pairs = combinations(set(tokens), 2)
    co_occurrence.update(pairs)

# Create NetworkX graph
G = nx.Graph()

# Add edges with weights (co-occurrence counts)
for (word1, word2), weight in co_occurrence.items():
    G.add_edge(word1, word2, weight=weight)

# Draw the network graph
plt.figure(figsize=(10, 7))

pos = nx.spring_layout(G, k=0.5, seed=42)
weights = [G[u][v]['weight'] for u,v in G.edges()]

nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=[w for w in weights])
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("Keyword Co-occurrence Network from News Headlines")
plt.axis('off')
plt.tight_layout()
plt.show()
