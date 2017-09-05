import networkx as nx

G=nx.Graph()
G.add_nodes_from(["a","b","c","d","e","f","g","h"])

G.add_edges_from([("a","b"),("a","c"),("a","d"),("a","e"),("a","f"),("a","g"),("a","h")])
G.add_edges_from([("b","c"),("b","d"),("b","e"),("b","f"),("b","g"),("b","h")])
G.add_edges_from([("c","d"),("c","e"),("c","f"),("c","g"),("c","h")])
G.add_edges_from([("d","e"),("d","f"),("d","g"),("d","h")])
G.add_edges_from([("e","f"),("e","g"),("e","h")])
G.add_edges_from([("f","g"),("f","h"),("g","h")])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())