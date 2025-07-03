from py2neo import Graph
import matplotlib.pyplot as plt
import networkx as nx

# Connessione a Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password123"))

# Query per estrarre nodi e relazioni
query = '''
MATCH (n)-[r]->(m)
RETURN n, type(r) as rel, m
LIMIT 100
'''
results = graph.run(query)

G = nx.MultiDiGraph()

for record in results:
    n = record['n']
    m = record['m']
    rel = record['rel']
    n_label = f"{list(n.labels)[0]}\n{n['id']}"
    m_label = f"{list(m.labels)[0]}\n{m['id']}"
    G.add_node(n_label)
    G.add_node(m_label)
    G.add_edge(n_label, m_label, label=rel)

plt.figure(figsize=(12,8))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Visualizzazione Grafo Neo4j (primi 100 archi)")
plt.axis('off')
plt.tight_layout()
plt.show()
