try:

  import matplotlib.pyplot as plt

except:

  raise 
import networkx as nx




G=nx.Graph()


G.add_nodes_from(['a','b','c','d','e','f','g','h'])


G.add_edges_from([('a','b'),('a','c'),('a','d'),('a','f'),('a','g'),('a','h')])

G.add_edges_from([('b','c'),('b','d'),('b','e'),('b','f'),('b','g'),('b','h')])

G.add_edges_from([('c','d'),('c','e'),('c','g')])

G.add_edges_from([('d','e'),('d','f'),('d','g'),('d','h')])

G.add_edges_from([('e','f'),('e','g'),('e','h')])

G.add_edges_from([('f','g'),('f','h'),('g','h')])

G.add_edge('a','e')

G.add_edge('c','f')

G.add_edge('c','h')

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G,pos,edgelist=[('a','b'),('a','c'),('a','d'),('a','f'),('a','g'),('a','h'),('b','c'),('b','d'),('b','e'),('b','f'),('b','g'),('b','h'),('c','d'),('c','e'),('c','g'),('d','e'),('d','f'),('d','g'),('d','h'),('e','f'),('e','g'),('e','h'),('f','g'),('f','h'),('g','h')],edge_color='b',width=2)
nx.draw_networkx_edges(G,pos,edgelist=[('a','e'),('c','f'),('c','h')],edge_color='g',width=4)

plt.savefig("graph.png")

plt.show()


