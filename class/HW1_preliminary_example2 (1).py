import matplotlib.pyplot as plt
import networkx as nx

k_avg = 1
N = 500
P = k_avg / (N - 1)

# nx.gnp_random_graph method directly generates G(n, p) random network.
G = nx.gnp_random_graph(N, P)

# After G is made, below lines will plot it.
# It's okay to copy and paste all the lines below
layouts = {'spring': nx.spring_layout(G),
           'circular': nx.circular_layout(G),
           'kamada_kawai': nx.kamada_kawai_layout(G),
           'random': nx.random_layout(G)}
size = [degree * 15 for node, degree in G.degree]
color = [degree * 5 for node, degree in G.degree]

fig, axes = plt.subplots(2, 2)
fig.set_size_inches(15, 15)
for (title, position), axis in zip(layouts.items(), axes.flatten()):
    nx.draw_networkx(G, pos=position, ax=axis, with_labels=False, node_size=size, node_color=color, cmap=plt.cm.Greens, edge_color='grey')
    axis.set_title(f'{title} layout', fontsize=20)
    axis.axis('off')
plt.tight_layout()
plt.show()


'''
Generating the network is a part of the question 4.
You should faithfully work on all requirements of the question to fullfill assigned points.
''' 