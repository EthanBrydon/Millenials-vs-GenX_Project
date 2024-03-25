import networkx as nx
import matplotlib.pyplot as plt

def create_graph(players):
    # Create an undirected graph
    G = nx.Graph()

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
    nx.draw_networkx_edges(G, pos, edge_color='k', node_size=1500)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=8)

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
episode1_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '1'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '1'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '4'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '2'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '2'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
    {'name': 'Will', 'tribe': 'red', 'relationships': []},
    {'name': 'Adam', 'tribe': 'red', 'relationships': []},
]

episode1_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-3'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-3'}, {'name': 'Chris', 'label': '-3'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Bret', 'label': '-4'}, {'name': 'Paul', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '-2'}]},
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '0'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Rachel', 'label': '-2'}, {'name': 'Paul', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Rachel', 'label': '-4'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Rachel', 'label': '-3'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Jessica', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Paul', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
]

episode2_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '6'}, {'name': 'Figgy', 'label': '8'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Michaela', 'label': '0'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '6'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '6'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '8'}, {'name': 'Jay', 'label': '6'}, {'name': 'Michaela', 'label': '-6'}, {'name': 'Mari', 'label': '-6'}, {'name': 'Zeke', 'label': '-3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Adam', 'label': '-2'}, {'name': 'Will', 'label': '2'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '4'}, {'name': 'Mari', 'label': '0'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '0'}, {'name': 'Figgy', 'label': '-6'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Will', 'label': '-2'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '0'}, {'name': 'Figgy', 'label': '-6'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Mari', 'label': '2'}]},
    {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
    {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-2'}, {'name': 'Mari', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
]

episode2_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Paul', 'label': '-2'}, {'name': 'Ken', 'label': '4'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '0'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '-2'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '-2'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Jessica', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}, {'name': 'Paul', 'label': '-2'}]},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '0'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '4'}, {'name': 'Chris', 'label': '2'}]},
]

episode1_sw_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 'w'}, {'name': 'Mari', 'label': 'w'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
    {'name': 'Will', 'tribe': 'red', 'relationships': []},
    {'name': 'Adam', 'tribe': 'red', 'relationships': []},
]

episode1_sw_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
    {'name': 'Rachel', 'tribe': 'purple', 'relationships': []},
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}, {'name': 'David', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}, {'name': 'David', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
]

episode2_sw_red = [
    {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 's'}, {'name': 'Will', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 's'}, {'name': 'Michaela', 'label': 'w'}, {'name': 'Will', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}, {'name': 'Michelle', 'label': 's'}, {'name': 'Will', 'label': 'w'}]},
    {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}, {'name': 'Hannah', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michaela', 'label': 'w'}, {'name': 'Will', 'label': 'w'}]},
    {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 's'}, {'name': 'Michaela', 'label': 'w'}, {'name': 'Taylor', 'label': 'w'}, {'name': 'Will', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}]},
    {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}, {'name': 'Zeke', 'label': 'w'}]},
    {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 'w'}, {'name': 'Will', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}, {'name': 'Mari', 'label': 'w'}]},
    {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': 'w'}, {'name': 'Michaela', 'label': 'w'}, {'name': 'Michelle', 'label': 'w'}, {'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
    {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': 'w'}, {'name': 'Zeke', 'label': 'w'}]},
]

episode2_sw_purple = [
    {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Jessica', 'label': 'w'}]},
    {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}]},
    {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
    {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
    {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
    {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
    {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
    {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
    {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 'w'}, {'name': 'David', 'label': 's'}, {'name': 'Chris', 'label': 'w'}]},
]



# create_graph(episode1_red)
# create_graph(episode1_purple)
# create_graph(episode2_red)
create_graph(episode2_purple)

# create_graph(episode1_sw_red)
# create_graph(episode1_sw_purple)
# create_graph(episode2_sw_red)
create_graph(episode2_sw_purple)
