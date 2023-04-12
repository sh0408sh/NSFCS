import networkx as nx
import matplotlib.pyplot as plt

# Initiating networkx.Graph object G
G = nx.Graph()

# First method to add nodes
G.add_node(1)  # add "node 1" into G
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Second method to add nodes
G.add_nodes_from([5, 6, 7, 8])  # add "node 5" ~ "node 8" into G

# First method to add edges
G.add_edge(1, 2)  # make an edge between "node 1" and "node 2" in G
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(2, 4)

# Second method to add edges
G.add_edges_from([(2, 5), (3, 6), (7, 8)])

# A method to visualize the G
nx.draw(G, with_labels=True, font_weight='bold')  # For your homework, it would be better to change the keyword arguments given here.
plt.show()
