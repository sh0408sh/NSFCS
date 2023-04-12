import networkx as nx
import matplotlib.pyplot as plt

# Clustering Coeffcient
N = 100
kset = [2*i for i in range(2,N//2)]
p = 0.
Cset = []

for k in kset:
    G = nx.watts_strogatz_graph(n=N, k=k, p=p)
    C = nx.clustering(G, nodes=0, weight=None)
    Cset.append(C)

fig, ax = plt.subplots()
for i in range(len(kset)):
    ax.plot(kset[i], Cset[i], marker='o', linestyle='', color='blue')
ax.set_xlabel('k')
ax.set_title('Clustering coefficient')
ax.legend()
plt.show()


# The Watts-Strogatz Model
N = 100
kavg = 10
pset = [0.]
for i in range(1,10):
    pset.append(0.0001*i)
    pset.append(0.001*i)
    pset.append(0.01*i)
    pset.append(0.1*i)
pset.append(1.)
pset.sort()

Cavgset = []
davgset = []

for p in pset:
    G = nx.watts_strogatz_graph(n=N, k=kavg, p=p)
    Cavg = nx.average_clustering(G, nodes=None, weight=None, count_zeros=True)
    Cavgset.append(Cavg)
    davg = nx.average_shortest_path_length(G, weight=None, method=None)
    davgset.append(davg)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
for i in range(len(pset)):
    ax1.plot(pset[i], Cavgset[i], marker='o', linestyle='', color='green')
    ax2.plot(pset[i], davgset[i], marker='o', linestyle='', color='blue')
ax1.set_xscale('log')
ax1.set_xlabel('p')
ax1.set_title('Clustering coefficient')
ax2.set_xscale('log')
ax2.set_xlabel('p')
ax2.set_title('Path length')

plt.show()