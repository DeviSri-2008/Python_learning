import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_node("Root")
G.add_node("Child 1")
G.add_node("Child 2")
G.add_node("Grandchild 1")
G.add_node("Grandchild 2")
G.add_edge("Root","Child 1")
G.add_edge("Root","Child 2")
G.add_edge("Root","Grandchild 1")
G.add_edge("Root","Grandchild 2")
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_size=2000,
        node_colour="skyblue",font_size=10,font_weight="bold")
plt.savefig("network.png")
plt.show()
