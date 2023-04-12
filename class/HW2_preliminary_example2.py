import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def Cayley_tree(k,gmax):
    G = nx.Graph()
    Cayley = {}
    for g in range(gmax+1):
        Cayley[g] = []
    for g in range(gmax):
        if g==0:
            Cayley[g].append(g)
            g1 = g+1
            for i in range(1,k+1):
                G.add_edge(g,g+i)
                Cayley[g1].append(g+i)
        else:
            for i in Cayley[g]:
                for j in range(2,k+1):
                    G.add_edge(i, i*(k-1)+j)
                g1 = g+1
                for j in range(2,k+1):
                    Cayley[g1].append(i*(k-1)+j)
    return G, Cayley

k=3
gmax=5
G = Cayley_tree(k,gmax)[0]
Cayley = Cayley_tree(k,gmax)[1]

def Coordinate_Caylee_tree(k,gmax):
    pos = {}           
    ang = {}
    Cayley = Cayley_tree(k,gmax)[1]

    for g in range(1,gmax+1):
        ang[g] = []

    for g in range(1,gmax):
        if g==1:
            for node in Cayley[g]:
                ang[g].append(2*np.pi/len(Cayley[g])*Cayley[g].index(node))
        for node in Cayley[g]:
            g1 = g+1
            for i in range(k-1):
                ang[g1].append(ang[g][Cayley[g].index(node)] + (-1/2+i/(k-2))*2*np.pi/len(Cayley[g1]))

    radius = 0
    for g in range(gmax+1):
        if g==0:
            pos[0] = (0,0)
        else:
            radius = radius + 5*0.9**g
            for node in Cayley[g]:
                angle = ang[g][Cayley[g].index(node)]
                pos[node] = (radius*np.cos(angle), radius*np.sin(angle))

    return pos

head_nodes = [Cayley[i][0] for i in range(gmax+1)]
node_betweenness = [nx.betweenness_centrality(G,normalized=False,endpoints=False)[node] for node in head_nodes]

head_edges = [(Cayley[i][0], Cayley[i+1][0]) for i in range(gmax)]
edge_betweenness = [nx.edge_betweenness_centrality(G,normalized=False)[edge] for edge in head_edges]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))


ax1.axis('equal')
nx.draw(G, Coordinate_Caylee_tree(k,gmax), with_labels = False, node_size=23, ax=ax1)
ax2.plot([g for g in range(gmax+1)], np.array(node_betweenness), '.')
ax2.set_title('node betweenness centrality')
ax2.set_xlabel('node')

subscript = [11*g+1 for g in range(gmax)]
ax3.plot([r'$e_{{{:2s}}}$'.format(f'{s:0>2}') for s in subscript], np.array(edge_betweenness), '.')
ax3.set_title('edge betweenness centrality')
ax3.set_xlabel('edge')

fig.suptitle(f'Cayley tree with k={k}, ' + r'$g_{{{:3s}}}$'.format('max') + f'={gmax}')
fig.tight_layout()
fig.subplots_adjust(top=0.8)
plt.show()

print(node_betweenness)
print(edge_betweenness)