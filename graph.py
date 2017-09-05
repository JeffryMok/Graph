try:

  import matplotlib.pyplot as plt

except:

  raise 
import networkx as nx




G=nx.Graph()


G.add_nodes_from(["a","b","c","d","e","f","g","h"])


G.add_edges_from([("a","b"),("a","c"),("a","d"),("a","f"),("a","g"),("a","h")],color='b')

G.add_edges_from([("b","c"),("b","d"),("b","e"),("b","f"),("b","g"),("b","h")],color='b')

G.add_edges_from([("c","d"),("c","e"),("c","g")],color='b')

G.add_edges_from([("d","e"),("d","f"),("d","g"),("d","h")],color='b')

G.add_edges_from([("e","f"),("e","g"),("e","h")],color='b')

G.add_edges_from([("f","g"),("f","h"),("g","h")],color='b')

G.add_edge("a","e",color='g')

G.add_edge("c","f",color='g')

G.add_edge("c","h",color='g')

nx.draw(G, edge_color='b')


plt.savefig("graph.png")

plt.show()


