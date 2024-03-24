import networkx as nx
import matplotlib.pyplot as plt

def create_graph(players):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges
    for player in players:
        G.add_node(player['name'], color='lightcoral' if player['tribe'] == 'red' else 'thistle')
        for relationship in player['relationships']:
            G.add_edge(player['name'], relationship)

    # Define positions for nodes
    red_nodes = [player['name'] for player in players if player['tribe'] == 'red']
    purple_nodes = [player['name'] for player in players if player['tribe'] == 'purple']
    pos = nx.shell_layout(G, [red_nodes, purple_nodes])

    # Draw the graph
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=2000, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True, node_size=2000)

    # Adjust plot limits
    padding = 0.2  # Padding ratio
    x_values, y_values = zip(*pos.values())
    x_max = max(x_values)
    x_min = min(x_values)
    y_max = max(y_values)
    y_min = min(y_values)

    plt.xlim(x_min - padding, x_max + padding)
    plt.ylim(y_min - padding, y_max + padding)

    plt.show()

# Example usage
players = [
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': ['Paul', 'Lucy']},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': []},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': []},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': []},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': ['Sunday']},
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': ['Jessica']},
    {'name': 'Brett', 'tribe': 'purple', 'relationships': []},
    {'name': 'David', 'tribe': 'purple', 'relationships': []},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
    {'name': 'Mari', 'tribe': 'red', 'relationships': []},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': []},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': ['Taylor', 'Zeke']},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
    {'name': 'Taylor', 'tribe': 'red', 'relationships': []},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': ['Taylor']},
    {'name': 'Will', 'tribe': 'red', 'relationships': []},
    {'name': 'Jay', 'tribe': 'red', 'relationships': ['Hannah', 'Adam']},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': ['Jay', 'Adam']},
    {'name': 'Adam', 'tribe': 'red', 'relationships': ['Hannah', 'Jay']},
]

create_graph(players)