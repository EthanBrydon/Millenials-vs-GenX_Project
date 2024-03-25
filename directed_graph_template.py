import networkx as nx
import matplotlib.pyplot as plt

def create_graph(players):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges
    for player in players:
        G.add_node(player['name'], color='lightcoral' if player['tribe'] == 'red' else 'thistle')
        for relationship in player['relationships']:
            G.add_edge(player['name'], relationship['name'], label=relationship['label'])

    # Define positions for nodes
    red_nodes = [player['name'] for player in players if player['tribe'] == 'red']
    purple_nodes = [player['name'] for player in players if player['tribe'] == 'purple']
    pos = nx.shell_layout(G, [red_nodes, purple_nodes])

    # Draw the graph
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1500, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True, node_size=1500)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.33, rotate=True)

    # Adjust plot limits
    padding = 0.15  # Padding ratio
    x_values, y_values = zip(*pos.values())
    x_max = max(x_values)
    x_min = min(x_values)
    y_max = max(y_values)
    y_min = min(y_values)

    plt.xlim(x_min - padding, x_max + padding)
    plt.ylim(y_min - padding, y_max + padding)

    plt.show()

# Example usage
episode1_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '2'}, {'name': 'Taylor', 'label': '2'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '1'}, {'name': 'Mari', 'label': '1'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
    {'name': 'Will', 'tribe': 'red', 'relationships': []},
    {'name': 'Adam', 'tribe': 'red', 'relationships': []},
]

episode1_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]}, 
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Rachel', 'label': '-2'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-4'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-3'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Bret', 'label': '1'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-2'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
]

episode2_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '4'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '3'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Michelle', 'label': '3'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '-1'}, {'name': 'Figgy', 'label': '0'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}, {'name': 'Figgy', 'label': '-4'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},      
    {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-1'}, {'name': 'Figgy', 'label': '-4'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '1'}, {'name': 'Mari', 'label': '1'}]},   
    {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
    {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-2'}, {'name': 'Mari', 'label': '1'}, {'name': 'Zeke', 'label': '1'}]},
]

episode2_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]}, 
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '-2'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-4'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Rachel', 'label': '-3'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Bret', 'label': '1'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-2'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '0'}, {'name': 'Chris', 'label': '1'}, {'name': 'CeCe', 'label': '-1'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Paul', 'label': '-1'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '3'}, {'name': 'Paul', 'label': '-1'}, {'name': 'Chris', 'label': '1'}]},
]


episode1_pn_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '+'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
    {'name': 'Will', 'tribe': 'red', 'relationships': []},
    {'name': 'Adam', 'tribe': 'red', 'relationships': []},
]

episode1_pn_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]}, 
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Rachel', 'label': '-'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Paul', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
]

episode2_pn_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},      
    {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}, {'name': 'Figgy', 'label': '-'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Mari', 'label': '+'}]},   
    {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
    {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Mari', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
]

episode2_pn_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]}, 
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '-'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Paul', 'label': '-'}, {'name': 'Chris', 'label': '+'}]},
]

# create_graph(episode1_purple)
# create_graph(episode1_red)
# create_graph(episode2_purple)
# create_graph(episode2_red)

create_graph(episode1_pn_purple)
create_graph(episode1_pn_red)
create_graph(episode2_pn_purple)
create_graph(episode2_pn_red)
