try:
	import matplotlib.pyplot as plt
except:
	raise 
import networkx as nx

G=nx.house_graph()
nodes = {'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h'}
post = {'a':(1.2,0),'b':(0.8,0.7),'c':(0,1),'d':(-0.8,0.7),'e':(-1.2,0),'f':(-0.8,-0.7),'g':(0,-1),'h':(0.8,-0.7)}

plt.axis('equal')

G.add_edges_from([('a','b'),('a','c'),('a','d'),('a','f'),('a','g'),('a','h')])
G.add_edges_from([('b','c'),('b','d'),('b','e'),('b','f'),('b','g'),('b','h')])
G.add_edges_from([('c','d'),('c','e'),('c','g')])
G.add_edges_from([('d','e'),('d','f'),('d','g'),('d','h')])
G.add_edges_from([('e','f'),('e','g'),('e','h')])
G.add_edges_from([('f','g'),('f','h'),('g','h')])
G.add_edge('a','e')
G.add_edge('c','f')
G.add_edge('c','h')
	 

nx.draw_networkx_labels(G,post, nodes)	 
nx.draw_networkx_nodes(G,post,nodelist= ['a','b','c','d','e','f','g','h'])
nx.draw_networkx_edges(G,post,edgelist=[('a','b'),('a','c'),('a','d'),('a','f'),('a','g'),('a','h'),('b','c'),('b','d'),('b','e'),('b','f'),('b','g'),('b','h'),('c','d'),('c','e'),('c','g'),('d','e'),('d','f'),('d','g'),('d','h'),('e','f'),('e','g'),('e','h'),('f','g'),('f','h'),('g','h')],edge_color='b',width=2)
nx.draw_networkx_edges(G,post,edgelist=[('a','e'),('c','f'),('c','h')],edge_color='g',width=4)

plt.savefig("grafik.png")

plt.show()