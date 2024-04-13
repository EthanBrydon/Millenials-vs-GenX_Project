import networkx as nx
import matplotlib.pyplot as plt

def create_graph(players, graph_title, graph_filename):
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
    # pos = nx.circular_layout(G)
    # pos = nx.spring_layout(G)
    # pos = nx.shell_layout(G, [red_nodes, purple_nodes])
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spectral_layout(G)
    pos = nx.random_layout(G)

    # Draw the graph
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1000, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=6)
    edge_labels = nx.get_edge_attributes(G, 'label')
    ### edge coloring based on the label ###
    edge_colors = ['black'] * len(edge_labels)
    # edge_colors = ['red' if int(label) < 0 else 'blue' if int(label) > 0 else 'black' for label in edge_labels.values()]
    # edge_colors = ['red' if label[0] == '-' else 'blue' for label in edge_labels.values()]
    # edge_colors = ['green' if label[0] == 's' else 'blue' for label in edge_labels.values()]
    # change transparency based on the label
    for edge, label in edge_labels.items():
        if str(label) == 's':
            alpha = 1
            width = 1.5
        else:
            alpha = 0.5
            width = 1
        nx.draw_networkx_edges(G, pos, edgelist={(edge[0], edge[1])}, alpha=alpha, width=width, edge_color='black', node_size=900)
    # nx.draw_networkx_edges(G, pos, edge_color=edge_colors, node_size=900, width=width, alpha=0.5, edgelist=G.edges())
    # color the labels based on vlaue
    # for edge, label in edge_labels.items():
    #     if int(label) < 0:
    #         color = 'red'
    #     elif int(label) > 0:
    #         color = 'blue'
    #     else:
    #         color = 'black'
    #     nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): label}, font_size=5, rotate=True, font_color=color)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=8, rotate=True)

    # Adjust plot limits
    padding = 0.1  # Padding ratio
    x_values, y_values = zip(*pos.values())
    x_max = max(x_values)
    x_min = min(x_values)
    y_max = max(y_values)
    y_min = min(y_values)

    plt.xlim(x_min - padding, x_max + padding)
    plt.ylim(y_min - padding, y_max + padding)

    # Set the title
    plt.title(graph_title)

    # Incerase the figure size
    plt.gcf().set_size_inches(13, 7.5)

    # fit the plot to the size
    plt.tight_layout()

    # save the graph
    plt.savefig(graph_filename + '.png')

    plt.show()


# *** Relationship Strengths Undirected ***
# First 1 Episodes Relationship Strengths (Undirected):

episode1_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-3'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Rachel', 'label': '-4'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Rachel', 'label': '-3'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '0'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Rachel', 'label': '-2'}, {'name': 'Paul', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Paul', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-3'}, {'name': 'Chris', 'label': '-3'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Bret', 'label': '-4'}, {'name': 'Paul', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '-2'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Jessica', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
]

episode1_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '4'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strengths Undirected ***
# First 2 Episodes Relationship Strengths (Undirected):

episode2_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Paul', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Paul', 'label': '-2'}, {'name': 'Ken', 'label': '4'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '0'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '4'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '0'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '-2'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '-2'}]}, 
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Jessica', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}, {'name': 'Paul', 'label': '-2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
]

episode2_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-2'}, {'name': 'Mari', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '0'}, {'name': 'Figgy', 'label': '-6'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Will', 'label': '-2'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '0'}, {'name': 'Figgy', 'label': '-6'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '6'}, {'name': 'Figgy', 'label': '8'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Michaela', 'label': '0'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '4'}, {'name': 'Mari', 'label': '0'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '6'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '6'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '8'}, {'name': 'Jay', 'label': '6'}, {'name': 'Michaela', 'label': '-6'}, {'name': 'Mari', 'label': '-6'}, {'name': 'Zeke', 'label': '-3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Adam', 'label': '-2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Mari', 'label': '2'}]},
]



# *** Relationship Strengths Undirected ***
# First 3 Episodes Relationship Strengths (Undirected):

episode3_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-1'}, {'name': 'Lucy', 'label': '4'}, {'name': 'Jessica', 'label': '6'}, {'name': 'Ken', 'label': '3'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'Paul', 'label': '-1'}, {'name': 'David', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Paul', 'label': '4'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '6'}, {'name': 'Jessica', 'label': '1'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Paul', 'label': '4'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '6'}, {'name': 'Jessica', 'label': '1'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Jessica', 'label': '1'}, {'name': 'CeCe', 'label': '0'}, {'name': 'Paul', 'label': '-6'}, {'name': 'Ken', 'label': '5'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '0'}, {'name': 'Jessica', 'label': '5'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Paul', 'label': '-3'}, {'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '-4'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '5'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '2'}, {'name': 'Jessica', 'label': '3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Lucy', 'label': '2'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '-4'}, {'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '-6'}, {'name': 'Chris', 'label': '4'}, {'name': 'CeCe', 'label': '-8'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '-1'}, {'name': 'Lucy', 'label': '-3'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '0'}, {'name': 'David', 'label': '0'}, {'name': 'Jessica', 'label': '0'}, {'name': 'Sunday', 'label': '-1'}, {'name': 'Paul', 'label': '-8'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '-3'}, {'name': 'Bret', 'label': '-3'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '1'}, {'name': 'CeCe', 'label': '0'}, {'name': 'Lucy', 'label': '5'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Ken', 'label': '3'}, {'name': 'Chris', 'label': '1'}, {'name': 'Paul', 'label': '-1'}, {'name': 'Bret', 'label': '1'}]},
]

episode3_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-4'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Hannah', 'label': '-2'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '0'}, {'name': 'Figgy', 'label': '-7'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Zeke', 'label': '-1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '7'}, {'name': 'Figgy', 'label': '11'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Michaela', 'label': '0'}, {'name': 'Will', 'label': '3'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Taylor', 'label': '3'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '4'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'Adam', 'label': '-2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '7'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '6'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '11'}, {'name': 'Jay', 'label': '6'}, {'name': 'Michaela', 'label': '-7'}, {'name': 'Zeke', 'label': '-5'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Adam', 'label': '-4'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-5'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '4'}, {'name': 'Hannah', 'label': '-2'}, {'name': 'Michelle', 'label': '-1'}]},
]



# *** Relationship Strengths Undirected ***
# First 4 Episodes Relationship Strengths (Undirected):

episode4_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-1'}, {'name': 'Lucy', 'label': '6'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Ken', 'label': '5'}, {'name': 'Bret', 'label': '3'}, {'name': 'Chris', 'label': '3'}, {'name': 'David', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '4'}, {'name': 'Chris', 'label': '8'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Lucy', 'label': '2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '4'}, {'name': 'Bret', 'label': '8'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Lucy', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Jessica', 'label': '5'}, {'name': 'CeCe', 'label': '3'}, {'name': 'Ken', 'label': '6'}, {'name': 'Lucy', 'label': '0'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '6'}, {'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '3'}, {'name': 'Chris', 'label': '2'}, {'name': 'Bret', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '6'}, {'name': 'Chris', 'label': '4'}, {'name': 'CeCe', 'label': '2'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Lucy', 'label': '3'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-2'}, {'name': 'David', 'label': '3'}, {'name': 'Jessica', 'label': '-2'}, {'name': 'Sunday', 'label': '-1'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '-3'}, {'name': 'Bret', 'label': '-3'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '5'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Ken', 'label': '-1'}, {'name': 'Chris', 'label': '-3'}, {'name': 'Bret', 'label': '-3'}]},
]

episode4_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-4'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Hannah', 'label': '-2'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '0'}, {'name': 'Figgy', 'label': '-7'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Zeke', 'label': '-1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '7'}, {'name': 'Figgy', 'label': '11'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Michaela', 'label': '0'}, {'name': 'Will', 'label': '3'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '2'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Taylor', 'label': '3'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '4'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'Adam', 'label': '-2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '7'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '6'}, {'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '11'}, {'name': 'Jay', 'label': '6'}, {'name': 'Michaela', 'label': '-7'}, {'name': 'Zeke', 'label': '-5'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '4'}, {'name': 'Adam', 'label': '-4'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-5'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '4'}, {'name': 'Hannah', 'label': '-2'}, {'name': 'Michelle', 'label': '-1'}]},
]



# *** Relationship Strengths Undirected ***
# First 5 Episodes Relationship Strengths (Undirected):

episode5_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-5'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '12'}, {'name': 'Adam', 'label': '-5'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '12'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
]

episode5_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'CeCe', 'label': '-5'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '2'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '2'}, {'name': 'Chris', 'label': '-5'}, {'name': 'Zeke', 'label': '-3'}, {'name': 'Michelle', 'label': '-4'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'David', 'label': '1'}, {'name': 'CeCe', 'label': '-4'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '0'}, {'name': 'CeCe', 'label': '2'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '4'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'David', 'label': '1'}]},
]

episode5_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '3'}]},
]



# *** Relationship Strengths Undirected ***
# First 6 Episodes Relationship Strengths (Undirected):

episode6_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-6'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Ken', 'label': '3'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '17'}, {'name': 'Adam', 'label': '-6'}, {'name': 'Ken', 'label': '-4'}, {'name': 'Jessica', 'label': '-2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '17'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Ken', 'label': '-2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '4'}, {'name': 'Figgy', 'label': '-2'}, {'name': 'Adam', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '4'}, {'name': 'Adam', 'label': '3'}, {'name': 'Figgy', 'label': '-4'}, {'name': 'Taylor', 'label': '-2'}]},
]

episode6_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '0'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '4'}, {'name': 'David', 'label': '1'}]},
]

episode6_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '3'}]},
]



# *** Relationship Strengths Undirected ***
# First 7 Episodes Relationship Strengths (Undirected):

episode7_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-2'}, {'name': 'Ken', 'label': '3'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '-2'}, {'name': 'Ken', 'label': '-1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '4'}, {'name': 'Adam', 'label': '2'}, {'name': 'Taylor', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '4'}, {'name': 'Adam', 'label': '3'}, {'name': 'Taylor', 'label': '-1'}]},
]

episode7_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '0'}, {'name': 'Zeke', 'label': '3'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '4'}, {'name': 'David', 'label': '3'}]},
]

episode7_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Bret', 'label': '-4'}, {'name': 'Sunday', 'label': '-2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Bret', 'label': '0'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '2'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '6'}, {'name': 'Will', 'label': '4'}, {'name': 'Jay', 'label': '4'}, {'name': 'Bret', 'label': '-3'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '7'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '7'}, {'name': 'Hannah', 'label': '-3'}, {'name': 'Jay', 'label': '0'}, {'name': 'Will', 'label': '1'}, {'name': 'Michaela', 'label': '-4'}]},
]



# *** Relationship Strengths Undirected ***
# First 8 Episodes Relationship Strengths (Undirected):

episode8_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '6'}, {'name': 'Hannah', 'label': '-1'}, {'name': 'Taylor', 'label': '-6'}, {'name': 'Ken', 'label': '5'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Will', 'label': '-5'}, {'name': 'Jay', 'label': '-4'}, {'name': 'Michelle', 'label': '-4'}, {'name': 'David', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '9'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Ken', 'label': '8'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Bret', 'label': '-1'}, {'name': 'Adam', 'label': '4'}, {'name': 'Taylor', 'label': '0'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '12'}, {'name': 'Chris', 'label': '6'}, {'name': 'Jessica', 'label': '8'}, {'name': 'Sunday', 'label': '7'}, {'name': 'Adam', 'label': '5'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '3'}, {'name': 'Jessica', 'label': '9'}, {'name': 'Ken', 'label': '12'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Zeke', 'label': '7'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '3'}, {'name': 'Jay', 'label': '4'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '6'}, {'name': 'Taylor', 'label': '5'}, {'name': 'Jay', 'label': '11'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Adam', 'label': '-5'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '6'}, {'name': 'Ken', 'label': '7'}, {'name': 'Bret', 'label': '10'}, {'name': 'Chris', 'label': '6'}, {'name': 'David', 'label': '4'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '3'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '6'}, {'name': 'Chris', 'label': '13'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '10'}, {'name': 'Hannah', 'label': '-1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '10'}, {'name': 'Michelle', 'label': '12'}, {'name': 'Will', 'label': '11'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'Adam', 'label': '-4'}, {'name': 'David', 'label': '-1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '6'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Chris', 'label': '7'}, {'name': 'David', 'label': '7'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Ken', 'label': '4'}, {'name': 'Taylor', 'label': '-3'}, {'name': 'Bret', 'label': '2'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '10'}, {'name': 'Michelle', 'label': '7'}, {'name': 'Will', 'label': '5'}, {'name': 'Hannah', 'label': '2'}, {'name': 'David', 'label': '-1'}, {'name': 'Adam', 'label': '-6'}, {'name': 'Ken', 'label': '-2'}, {'name': 'Jessica', 'label': '0'}, {'name': 'Bret', 'label': '-2'}, {'name': 'Zeke', 'label': '-3'}, {'name': 'Chris', 'label': '-1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '7'}, {'name': 'Jay', 'label': '12'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Will', 'label': '6'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'David', 'label': '-2'}, {'name': 'Chris', 'label': '0'}, {'name': 'Adam', 'label': '-4'}, {'name': 'Bret', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}, {'name': 'Ken', 'label': '-2'}, {'name': 'Jessica', 'label': '-2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '6'}, {'name': 'Bret', 'label': '13'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Zeke', 'label': '7'}, {'name': 'Michelle', 'label': '0'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '2'}]},
]



# *** Relationship Strengths Undirected ***
# First 9 Episodes Relationship Strengths (Undirected):

episode9_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '7'}, {'name': 'Hannah', 'label': '-1'}, {'name': 'Taylor', 'label': '-15'}, {'name': 'Ken', 'label': '7'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Will', 'label': '-5'}, {'name': 'Jay', 'label': '-7'}, {'name': 'David', 'label': '3'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '4'}, {'name': 'Sunday', 'label': '4'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '9'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Ken', 'label': '8'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Bret', 'label': '0'}, {'name': 'Adam', 'label': '4'}, {'name': 'Taylor', 'label': '0'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '-3'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '14'}, {'name': 'Chris', 'label': '9'}, {'name': 'Jessica', 'label': '8'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '7'}, {'name': 'Taylor', 'label': '-4'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '6'}, {'name': 'Jessica', 'label': '9'}, {'name': 'Ken', 'label': '14'}, {'name': 'Taylor', 'label': '-5'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Zeke', 'label': '9'}, {'name': 'Jay', 'label': '0'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '3'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '2'}, {'name': 'Will', 'label': '6'}, {'name': 'Jay', 'label': '2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Jessica', 'label': '5'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '7'}, {'name': 'Jay', 'label': '11'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Adam', 'label': '-5'}, {'name': 'Jessica', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '4'}, {'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '12'}, {'name': 'Chris', 'label': '11'}, {'name': 'David', 'label': '6'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '8'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '4'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Taylor', 'label': '-2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '6'}, {'name': 'Chris', 'label': '16'}, {'name': 'Jessica', 'label': '0'}, {'name': 'Sunday', 'label': '12'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Will', 'label': '3'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '11'}, {'name': 'Will', 'label': '11'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '-1'}, {'name': 'Sunday', 'label': '8'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Adam', 'label': '-7'}, {'name': 'David', 'label': '0'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '7'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Chris', 'label': '9'}, {'name': 'David', 'label': '9'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Ken', 'label': '6'}, {'name': 'Taylor', 'label': '-5'}, {'name': 'Bret', 'label': '2'}, {'name': 'Sunday', 'label': '4'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '11'}, {'name': 'Will', 'label': '7'}, {'name': 'Hannah', 'label': '2'}, {'name': 'David', 'label': '-5'}, {'name': 'Adam', 'label': '-15'}, {'name': 'Ken', 'label': '-4'}, {'name': 'Jessica', 'label': '0'}, {'name': 'Bret', 'label': '-2'}, {'name': 'Zeke', 'label': '-5'}, {'name': 'Chris', 'label': '-2'}, {'name': 'Sunday', 'label': '-2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '6'}, {'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '16'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '11'}, {'name': 'Zeke', 'label': '9'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '4'}, {'name': 'Jay', 'label': '2'}]},
]



# *** Relationship Strengths Undirected ***
# First 10 Episodes Relationship Strengths (Undirected):

episode10_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '9'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Ken', 'label': '10'}, {'name': 'Jessica', 'label': '7'}, {'name': 'Will', 'label': '-3'}, {'name': 'Jay', 'label': '-8'}, {'name': 'David', 'label': '6'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'Sunday', 'label': '4'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '13'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '10'}, {'name': 'Chris', 'label': '-7'}, {'name': 'Bret', 'label': '-3'}, {'name': 'Adam', 'label': '7'}, {'name': 'Zeke', 'label': '5'}, {'name': 'Hannah', 'label': '7'}, {'name': 'Jay', 'label': '-5'}, {'name': 'Will', 'label': '4'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '19'}, {'name': 'Chris', 'label': '7'}, {'name': 'Jessica', 'label': '10'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '10'}, {'name': 'Zeke', 'label': '8'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '4'}, {'name': 'Jessica', 'label': '13'}, {'name': 'Ken', 'label': '19'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Zeke', 'label': '13'}, {'name': 'Jay', 'label': '0'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '6'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '9'}, {'name': 'Jay', 'label': '2'}, {'name': 'Zeke', 'label': '8'}, {'name': 'Adam', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '5'}, {'name': 'Chris', 'label': '0'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Ken', 'label': '5'}, {'name': 'Jessica', 'label': '7'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '10'}, {'name': 'Hannah', 'label': '9'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Adam', 'label': '-3'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Chris', 'label': '-2'}, {'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '1'}, {'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '15'}, {'name': 'Chris', 'label': '14'}, {'name': 'David', 'label': '5'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '10'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '4'}, {'name': 'Zeke', 'label': '4'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '6'}, {'name': 'Chris', 'label': '21'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Sunday', 'label': '15'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '3'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '4'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '10'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '10'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Adam', 'label': '-8'}, {'name': 'David', 'label': '0'}, {'name': 'Jessica', 'label': '-5'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '4'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '9'}, {'name': 'Hannah', 'label': '8'}, {'name': 'Chris', 'label': '9'}, {'name': 'David', 'label': '13'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Jessica', 'label': '5'}, {'name': 'Ken', 'label': '8'}, {'name': 'Bret', 'label': '4'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Will', 'label': '4'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '4'}, {'name': 'Ken', 'label': '7'}, {'name': 'Bret', 'label': '21'}, {'name': 'Jessica', 'label': '-7'}, {'name': 'Sunday', 'label': '14'}, {'name': 'Zeke', 'label': '9'}, {'name': 'Hannah', 'label': '0'}, {'name': 'Adam', 'label': '2'}, {'name': 'Jay', 'label': '4'}, {'name': 'Will', 'label': '-2'}]},
]



# *** Relationship Strengths Undirected ***
# First 11 Episodes Relationship Strengths (Undirected):

episode10_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '14'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Ken', 'label': '14'}, {'name': 'Jessica', 'label': '11'}, {'name': 'Will', 'label': '-3'}, {'name': 'Jay', 'label': '-8'}, {'name': 'David', 'label': '10'}, {'name': 'Bret', 'label': '2'}, {'name': 'Sunday', 'label': '4'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '19'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '17'}, {'name': 'Bret', 'label': '-3'}, {'name': 'Adam', 'label': '11'}, {'name': 'Zeke', 'label': '9'}, {'name': 'Hannah', 'label': '9'}, {'name': 'Jay', 'label': '-6'}, {'name': 'Will', 'label': '4'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '27'}, {'name': 'Jessica', 'label': '17'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '14'}, {'name': 'Zeke', 'label': '12'}, {'name': 'Hannah', 'label': '7'}, {'name': 'Jay', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-2'}, {'name': 'Jessica', 'label': '19'}, {'name': 'Ken', 'label': '27'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Zeke', 'label': '13'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Hannah', 'label': '10'}, {'name': 'Adam', 'label': '10'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '12'}, {'name': 'Jay', 'label': '5'}, {'name': 'Zeke', 'label': '11'}, {'name': 'Adam', 'label': '3'}, {'name': 'Bret', 'label': '5'}, {'name': 'David', 'label': '10'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Ken', 'label': '7'}, {'name': 'Jessica', 'label': '9'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '14'}, {'name': 'Hannah', 'label': '12'}, {'name': 'Bret', 'label': '7'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Adam', 'label': '-3'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Zeke', 'label': '7'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '1'}, {'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '19'}, {'name': 'David', 'label': '5'}, {'name': 'Will', 'label': '6'}, {'name': 'Jay', 'label': '14'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Adam', 'label': '4'}, {'name': 'Zeke', 'label': '9'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '4'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Sunday', 'label': '19'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '5'}, {'name': 'Will', 'label': '7'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '12'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '14'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '14'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Adam', 'label': '-8'}, {'name': 'David', 'label': '-1'}, {'name': 'Jessica', 'label': '-6'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '14'}, {'name': 'Hannah', 'label': '11'}, {'name': 'David', 'label': '13'}, {'name': 'Jay', 'label': '2'}, {'name': 'Jessica', 'label': '9'}, {'name': 'Ken', 'label': '12'}, {'name': 'Bret', 'label': '12'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Will', 'label': '7'}]},
]



# *** Relationship Strengths Undirected ***
# First 12 Episodes Relationship Strengths (Undirected):

episode11_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '12'}, {'name': 'Hannah', 'label': '11'}, {'name': 'Ken', 'label': '17'}, {'name': 'Will', 'label': '-1'}, {'name': 'Jay', 'label': '-6'}, {'name': 'David', 'label': '14'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '4'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '30'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '17'}, {'name': 'Zeke', 'label': '10'}, {'name': 'Hannah', 'label': '11'}, {'name': 'Jay', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-2'}, {'name': 'Ken', 'label': '30'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Zeke', 'label': '10'}, {'name': 'Jay', 'label': '-3'}, {'name': 'Hannah', 'label': '14'}, {'name': 'Adam', 'label': '14'}, {'name': 'Will', 'label': '3'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '14'}, {'name': 'Jay', 'label': '3'}, {'name': 'Zeke', 'label': '7'}, {'name': 'Adam', 'label': '11'}, {'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '14'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Ken', 'label': '11'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '15'}, {'name': 'Hannah', 'label': '14'}, {'name': 'Bret', 'label': '7'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Zeke', 'label': '5'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '23'}, {'name': 'David', 'label': '5'}, {'name': 'Will', 'label': '4'}, {'name': 'Jay', 'label': '18'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Adam', 'label': '4'}, {'name': 'Zeke', 'label': '13'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '4'}, {'name': 'Sunday', 'label': '23'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Jay', 'label': '9'}, {'name': 'Will', 'label': '7'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '16'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '15'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '9'}, {'name': 'Sunday', 'label': '18'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Adam', 'label': '-6'}, {'name': 'David', 'label': '-3'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '12'}, {'name': 'Hannah', 'label': '7'}, {'name': 'David', 'label': '10'}, {'name': 'Jay', 'label': '6'}, {'name': 'Ken', 'label': '10'}, {'name': 'Bret', 'label': '16'}, {'name': 'Sunday', 'label': '13'}, {'name': 'Will', 'label': '5'}]},
]



# *** Relationship Strengths Undirected ***
# First 13 Episodes Relationship Strengths (Undirected):

episode12_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '15'}, {'name': 'Ken', 'label': '19'}, {'name': 'Will', 'label': '-4'}, {'name': 'Jay', 'label': '-7'}, {'name': 'David', 'label': '15'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '8'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '32'}, {'name': 'Sunday', 'label': '11'}, {'name': 'Adam', 'label': '19'}, {'name': 'Hannah', 'label': '13'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '0'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-1'}, {'name': 'Ken', 'label': '32'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Jay', 'label': '-6'}, {'name': 'Hannah', 'label': '17'}, {'name': 'Adam', 'label': '15'}, {'name': 'Will', 'label': '-2'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '12'}, {'name': 'Jay', 'label': '3'}, {'name': 'Adam', 'label': '15'}, {'name': 'Bret', 'label': '5'}, {'name': 'David', 'label': '17'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Ken', 'label': '13'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '18'}, {'name': 'Hannah', 'label': '12'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-4'}, {'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '0'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '11'}, {'name': 'Bret', 'label': '28'}, {'name': 'David', 'label': '6'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '17'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Adam', 'label': '8'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '6'}, {'name': 'Sunday', 'label': '28'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '8'}, {'name': 'Will', 'label': '3'}, {'name': 'Adam', 'label': '5'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '18'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '8'}, {'name': 'Sunday', 'label': '17'}, {'name': 'Adam', 'label': '-7'}, {'name': 'David', 'label': '-6'}, {'name': 'Ken', 'label': '1'}]},
]



# *** Relationship Strengths Undirected ***
# First 14 Episodes Relationship Strengths (Undirected):

episode12_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '17'}, {'name': 'Ken', 'label': '21'}, {'name': 'Jay', 'label': '-6'}, {'name': 'David', 'label': '16'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '6'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '34'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '21'}, {'name': 'Hannah', 'label': '15'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-3'}, {'name': 'Ken', 'label': '34'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Jay', 'label': '-9'}, {'name': 'Hannah', 'label': '19'}, {'name': 'Adam', 'label': '16'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Adam', 'label': '17'}, {'name': 'Bret', 'label': '5'}, {'name': 'David', 'label': '19'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Ken', 'label': '15'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '9'}, {'name': 'Bret', 'label': '28'}, {'name': 'David', 'label': '4'}, {'name': 'Jay', 'label': '15'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Adam', 'label': '6'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-3'}, {'name': 'Ken', 'label': '6'}, {'name': 'Sunday', 'label': '28'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '10'}, {'name': 'Adam', 'label': '5'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '10'}, {'name': 'Sunday', 'label': '15'}, {'name': 'Adam', 'label': '-6'}, {'name': 'David', 'label': '-9'}, {'name': 'Ken', 'label': '1'}]},
]



# *** Relationship Strengths Undirected ***
# First 15 Episodes Relationship Strengths (Undirected):

episode13_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '19'}, {'name': 'Ken', 'label': '23'}, {'name': 'Jay', 'label': '-4'}, {'name': 'David', 'label': '20'}, {'name': 'Bret', 'label': '8'}]},  
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '8'}, {'name': 'David', 'label': '36'}, {'name': 'Adam', 'label': '23'}, {'name': 'Hannah', 'label': '17'}, {'name': 'Jay', 'label': '-3'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-4'}, {'name': 'Ken', 'label': '36'}, {'name': 'Jay', 'label': '-8'}, {'name': 'Hannah', 'label': '21'}, {'name': 'Adam', 'label': '20'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '2'}, {'name': 'Adam', 'label': '19'}, {'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '21'}, {'name': 'Ken', 'label': '17'}]},   
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-4'}, {'name': 'Ken', 'label': '8'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Jay', 'label': '6'}, {'name': 'Adam', 'label': '8'}]},  
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '6'}, {'name': 'Adam', 'label': '-4'}, {'name': 'David', 'label': '-8'}, {'name': 'Ken', 'label': '-3'}]},   
]



# *** Relationship Strengths Undirected ***
# First 16 Episodes Relationship Strengths (Undirected):

episode13_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '19'}, {'name': 'Ken', 'label': '23'}, {'name': 'David', 'label': '16'}, {'name': 'Bret', 'label': '13'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '6'}, {'name': 'David', 'label': '39'}, {'name': 'Adam', 'label': '23'}, {'name': 'Hannah', 'label': '19'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-10'}, {'name': 'Ken', 'label': '39'}, {'name': 'Hannah', 'label': '24'}, {'name': 'Adam', 'label': '16'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '19'}, {'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '24'}, {'name': 'Ken', 'label': '19'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-10'}, {'name': 'Ken', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Adam', 'label': '13'}]},
]



# *** Relationship Strengths Undirected ***
# First 17 Episodes Relationship Strengths (Undirected):

episode13_3_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '22'}, {'name': 'Ken', 'label': '23'}, {'name': 'David', 'label': '12'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '39'}, {'name': 'Adam', 'label': '23'}, {'name': 'Hannah', 'label': '20'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '39'}, {'name': 'Hannah', 'label': '21'}, {'name': 'Adam', 'label': '12'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '22'}, {'name': 'David', 'label': '21'}, {'name': 'Ken', 'label': '20'}]},
]



## Creating Graphs Section ##

# create_graph(episode1_takali, "Episode 1: Takali Tribe Relationship Strengths (Undirected)", "episode1_takali-U")
# create_graph(episode1_vanua, "Episode 1: Vanua Tribe Relationship Strengths (Undirected)", "episode1_vanua-U")
# create_graph(episode2_takali, "Episode 2: Takali Tribe Relationship Strengths (Undirected)", "episode2_takali-U")
# create_graph(episode2_vanua, "Episode 2: Vanua Tribe Relationship Strengths (Undirected)", "episode2_vanua-U")
# create_graph(episode3_takali, "Episode 3: Takali Tribe Relationship Strengths (Undirected)", "episode3_takali-U")
# create_graph(episode3_vanua, "Episode 3: Vanua Tribe Relationship Strengths (Undirected)", "episode3_vanua-U")
# create_graph(episode4_takali, "Episode 4: Takali Tribe Relationship Strengths (Undirected)", "episode4_takali-U")
# create_graph(episode4_vanua, "Episode 4: Vanua Tribe Relationship Strengths (Undirected)", "episode4_vanua-U")
# create_graph(episode5_takali, "Episode 5: Takali Tribe Relationship Strengths (Undirected)", "episode5_takali-U")
# create_graph(episode5_vanua, "Episode 5: Vanua Tribe Relationship Strengths (Undirected)", "episode5_vanua-U")
# create_graph(episode5_Ikabula, "Episode 5: Ikabula Tribe Relationship Strengths (Undirected)", "episode5_Ikabula-U")
# create_graph(episode6_takali, "Episode 6: Takali Tribe Relationship Strengths (Undirected)", "episode6_takali-U")
# create_graph(episode6_vanua, "Episode 6: Vanua Tribe Relationship Strengths (Undirected)", "episode6_vanua-U")
# create_graph(episode6_Ikabula, "Episode 6: Ikabula Tribe Relationship Strengths (Undirected)", "episode6_Ikabula-U")
# create_graph(episode7_takali, "Episode 7: Takali Tribe Relationship Strengths (Undirected)", "episode7_takali-U")
# create_graph(episode7_vanua, "Episode 7: Vanua Tribe Relationship Strengths (Undirected)", "episode7_vanua-U")
# create_graph(episode7_Ikabula, "Episode 7: Ikabula Tribe Relationship Strengths (Undirected)", "episode7_Ikabula-U")
# create_graph(episode8_vinaka, "Episode 8: Vinaka Tribe Relationship Strengths (Undirected)", "episode8_vinaka-U")
# create_graph(episode9_vinaka, "Episode 9: Vinaka Tribe Relationship Strengths (Undirected)", "episode9_vinaka-U")
# create_graph(episode10_1_vinaka, "Episode 10 - Part 1: Vinaka Tribe Relationship Strengths (Undirected)", "episode10_1_vinaka-U")
# create_graph(episode10_2_vinaka, "Episode 10 - Part 2: Vinaka Tribe Relationship Strengths (Undirected)", "episode10_2_vinaka-U")
# create_graph(episode11_vinaka, "Episode 11 Vinaka Tribe Relationship Strengths (Undirected)", "episode11_vinaka-U")
# create_graph(episode12_1_vinaka, "Episode 12 - Part 1:  Vinaka Tribe Relationship Strengths (Undirected)", "episode12_1_vinaka-U")
# create_graph(episode12_2_vinaka, "Episode 12 - Part 2: Vinaka Tribe Relationship Strengths (Undirected)", "episode12_2_vinaka-U")
# create_graph(episode13_1_vinaka, "Episode 13 - Part 1: Vinaka Tribe Relationship Strengths (Undirected)", "episode13_1_vinaka-U")
# create_graph(episode13_2_vinaka, "Episode 13 - Part 2: Vinaka Tribe Relationship Strengths (Undirected)", "episode13_2_vinaka-U")
# create_graph(episode13_3_vinaka, "Episode 13 - Part 3: Vinaka Tribe Relationship Strengths (Undirected)", "episode13_3_vinaka-U")



# *** Relationship Positive vs. Negative Undirected ***
# First 1 Episodes Positive vs. Negative (Undirected):

episode1_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Rachel', 'label': '-'}]},  
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},   
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-'}, {'name': 'Chris', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Paul', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
]

episode1_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 2 Episodes Positive vs. Negative (Undirected):

episode2_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},   
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},        
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Paul', 'label': '-'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},   
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},       
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '-'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '-'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
]

episode2_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Mari', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},        
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Mari', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Will', 'label': '+'}]},        
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Mari', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 3 Episodes Positive vs. Negative (Undirected):

episode3_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Paul', 'label': '-'}, {'name': 'David', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '-'}, {'name': 'Paul', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Paul', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Lucy', 'label': '+'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '-'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '-'}, {'name': 'Lucy', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-'}, {'name': 'Paul', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
]

episode3_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},        
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 4 Episodes Positive vs. Negative (Undirected):

episode4_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Lucy', 'label': '+'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Lucy', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'CeCe', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Lucy', 'label': '+'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '-'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '-'}]},
]

episode4_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},        
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 5 Episodes Positive vs. Negative (Undirected):

episode5_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
]

episode5_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},   
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
]

episode5_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},      
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 6 Episodes Positive vs. Negative (Undirected):

episode6_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Figgy', 'label': '-'}, {'name': 'Adam', 'label': '+'}]},     
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Figgy', 'label': '-'}, {'name': 'Taylor', 'label': '-'}]},
]

episode6_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': []},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}]},
]

episode6_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},      
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 7 Episodes Positive vs. Negative (Undirected):

episode7_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},       
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Taylor', 'label': '-'}]},    
]

episode7_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Zeke', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}]},
]

episode7_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'Sunday', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},        
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Michaela', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 8 Episodes Positive vs. Negative (Undirected):

episode8_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'Michelle', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},        
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Chris', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Sunday', 'label': '-'}, {'name': 'Ken', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 9 Episodes Positive vs. Negative (Undirected):

episode9_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Chris', 'label': '-'}, {'name': 'Sunday', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 10 Episodes Positive vs. Negative (Undirected):

episode10_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Will', 'label': '+'}]},       
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 11 Episodes Positive vs. Negative (Undirected):

episode10_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 12 Episodes Positive vs. Negative (Undirected):

episode11_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 13 Episodes Positive vs. Negative (Undirected):

episode12_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Will', 'label': '-'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 14 Episodes Positive vs. Negative (Undirected):

episode12_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 15 Episodes Positive vs. Negative (Undirected):

episode13_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 16 Episodes Positive vs. Negative (Undirected):

episode13_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Undirected ***
# First 17 Episodes Positive vs. Negative (Undirected):

episode13_3_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
]


# create_graph(episode1_takali_pn, 'Episode 1: Takali Positive vs. Negative Relationships (Undirected)', 'episode1_takali_pn')
# create_graph(episode1_vanua_pn, 'Episode 1: Vanua Positive vs. Negative Relationships (Undirected)', 'episode1_vanua_pn')
# create_graph(episode2_takali_pn, 'Episode 2: Takali Positive vs. Negative Relationships (Undirected)', 'episode2_takali_pn')
# create_graph(episode2_vanua_pn, 'Episode 2: Vanua Positive vs. Negative Relationships (Undirected)', 'episode2_vanua_pn')
# create_graph(episode3_takali_pn, 'Episode 3: Takali Positive vs. Negative Relationships (Undirected)', 'episode3_takali_pn')
# create_graph(episode3_vanua_pn, 'Episode 3: Vanua Positive vs. Negative Relationships (Undirected)', 'episode3_vanua_pn')
# create_graph(episode4_takali_pn, 'Episode 4: Takali Positive vs. Negative Relationships (Undirected)', 'episode4_takali_pn')
# create_graph(episode4_vanua_pn, 'Episode 4: Vanua Positive vs. Negative Relationships (Undirected)', 'episode4_vanua_pn')
# create_graph(episode5_takali_pn, 'Episode 5: Takali Positive vs. Negative Relationships (Undirected)', 'episode5_takali_pn')
# create_graph(episode5_vanua_pn, 'Episode 5: Vanua Positive vs. Negative Relationships (Undirected)', 'episode5_vanua_pn')
# create_graph(episode5_Ikabula_pn, 'Episode 5: Ikabula Positive vs. Negative Relationships (Undirected)', 'episode5_Ikabula_pn')
# create_graph(episode6_takali_pn, 'Episode 6: Takali Positive vs. Negative Relationships (Undirected)', 'episode6_takali_pn')
# create_graph(episode6_vanua_pn, 'Episode 6: Vanua Positive vs. Negative Relationships (Undirected)', 'episode6_vanua_pn')
# create_graph(episode6_Ikabula_pn, 'Episode 6: Ikabula Positive vs. Negative Relationships (Undirected)', 'episode6_Ikabula_pn')
# create_graph(episode7_takali_pn, 'Episode 7: Takali Positive vs. Negative Relationships (Undirected)', 'episode7_takali_pn')
# create_graph(episode7_vanua_pn, 'Episode 7: Vanua Positive vs. Negative Relationships (Undirected)', 'episode7_vanua_pn')
# create_graph(episode7_Ikabula_pn, 'Episode 7: Ikabula Positive vs. Negative Relationships (Undirected)', 'episode7_Ikabula_pn')
# create_graph(episode8_vinaka_pn, 'Episode 8: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode8_vinaka_pn')
# create_graph(episode9_vinaka_pn, 'Episode 9: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode9_vinaka_pn')
# create_graph(episode10_1_vinaka_pn, 'Episode 10 - Part 1: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode10_1_vinaka_pn')
# create_graph(episode10_2_vinaka_pn, 'Episode 10 - Part 2: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode10_2_vinaka_pn')
# create_graph(episode11_vinaka_pn, 'Episode 11: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode11_vinaka_pn')
# create_graph(episode12_1_vinaka_pn, 'Episode 12 - Part 1: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode12_1_vinaka_pn')
# create_graph(episode12_2_vinaka_pn, 'Episode 12 - Part 2: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode12_2_vinaka_pn')
# create_graph(episode13_1_vinaka_pn, 'Episode 13 - Part 1: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode13_1_vinaka_pn')
# create_graph(episode13_2_vinaka_pn, 'Episode 13 - Part 2: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode13_2_vinaka_pn')
# create_graph(episode13_3_vinaka_pn, 'Episode 13 - Part 3: Vinaka Positive vs. Negative Relationships (Undirected)', 'episode13_3_vinaka_pn')



# *** Relationship Strong vs. Weak Undirected ***
# First 1 Episodes Strong vs. Weak (Undirected):

episode1_takali_sw = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Jessica', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': []},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},        
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},        
        {'name': 'Rachel', 'tribe': 'purple', 'relationships': []},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
]

episode1_vanua_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 'w'}, {'name': 'Mari', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 's'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 2 Episodes Strong vs. Weak (Undirected):

episode2_takali_sw = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': []},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': []},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
]

episode2_vanua_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': []},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}, {'name': 'Figgy', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},     
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 's'}]},     
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},     
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 3 Episodes Strong vs. Weak (Undirected):

episode3_takali_sw = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Jessica', 'label': 's'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Chris', 'label': 's'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': 'w'}, {'name': 'Bret', 'label': 's'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Sunday', 'label': 's'}]},
]

episode3_vanua_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': 'w'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}, {'name': 'Figgy', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},     
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 's'}, {'name': 'Michelle', 'label': 's'}]},     
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 's'}, {'name': 'Michelle', 'label': 'w'}]},     
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 4 Episodes Strong vs. Weak (Undirected):

episode4_takali_sw = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Lucy', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': 's'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}]},
]

episode4_vanua_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Figgy', 'label': 's'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Figgy', 'label': 'w'}, {'name': 'Michelle', 'label': 'w'}]},     
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}, {'name': 'Jay', 'label': 'w'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 5 Episodes Strong vs. Weak (Undirected):

episode5_takali_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': 's'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
]

episode5_vanua_sw = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': []},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': []},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]

episode5_Ikabula_sw = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': []},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 6 Episodes Strong vs. Weak (Undirected):

episode6_takali_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 's'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': 's'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
]

episode6_vanua_sw = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': []},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]

episode6_Ikabula_sw = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': []},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 7 Episodes Strong vs. Weak (Undirected):

episode7_takali_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
]

episode7_vanua_sw = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': []},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]

episode7_Ikabula_sw = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 's'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 8 Episodes Strong vs. Weak (Undirected):

episode8_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},   
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Ken', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},     
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': 's'}, {'name': 'Sunday', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Michelle', 'label': 's'}, {'name': 'Will', 'label': 's'}]},      
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}, {'name': 'Michelle', 'label': 'w'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 's'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 9 Episodes Strong vs. Weak (Undirected):

episode9_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Chris', 'label': 'w'}, {'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}, {'name': 'Adam', 'label': 'w'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Ken', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},     
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 's'}, {'name': 'Chris', 'label': 'w'}, {'name': 'Jay', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': 's'}, {'name': 'Sunday', 'label': 's'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': 'w'}, {'name': 'Will', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},        
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}, {'name': 'Will', 'label': 'w'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 's'}, {'name': 'Sunday', 'label': 'w'}, {'name': 'Zeke', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 10 Episodes Strong vs. Weak (Undirected):

episode10_1_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Jessica', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}, {'name': 'Adam', 'label': 'w'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 'w'}, {'name': 'Ken', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},     
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 's'}, {'name': 'Chris', 'label': 's'}, {'name': 'Jay', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': 's'}, {'name': 'Sunday', 'label': 's'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}, {'name': 'Chris', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}, {'name': 'Sunday', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},     
]



# *** Relationship Strong vs. Weak Undirected ***
# First 11 Episodes Strong vs. Weak (Undirected):

episode10_2_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'Jessica', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'Adam', 'label': 'w'}]},     
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Jessica', 'label': 's'}, {'name': 'Adam', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}, {'name': 'Adam', 'label': 'w'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}, {'name': 'Zeke', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},        
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}, {'name': 'Jay', 'label': 's'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 's'}, {'name': 'Sunday', 'label': 's'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}, {'name': 'David', 'label': 'w'}, {'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 12 Episodes Strong vs. Weak (Undirected):

episode11_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': 'w'}, {'name': 'Ken', 'label': 's'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Adam', 'label': 's'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}, {'name': 'Adam', 'label': 'w'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 'w'}, {'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}, {'name': 'Jay', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},       
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 's'}, {'name': 'Zeke', 'label': 'w'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}, {'name': 'Sunday', 'label': 's'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}, {'name': 'Sunday', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 13 Episodes Strong vs. Weak (Undirected):

episode12_1_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 'w'}, {'name': 'Ken', 'label': 's'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Sunday', 'label': 'w'}, {'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 's'}, {'name': 'Adam', 'label': 'w'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 'w'}, {'name': 'Adam', 'label': 'w'}, {'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 'w'}, {'name': 'Bret', 'label': 's'}, {'name': 'Jay', 'label': 's'}]},        
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 's'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': 's'}, {'name': 'Sunday', 'label': 's'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 14 Episodes Strong vs. Weak (Undirected):

episode12_2_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'David', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 's'}, {'name': 'Adam', 'label': 'w'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 's'}, {'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': 's'}, {'name': 'Jay', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': 's'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Sunday', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 15 Episodes Strong vs. Weak (Undirected):

episode13_1_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'David', 'label': 's'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 'w'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 's'}, {'name': 'Adam', 'label': 's'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 's'}, {'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 'w'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 16 Episodes Strong vs. Weak (Undirected):

episode13_2_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 's'}, {'name': 'Ken', 'label': 's'}, {'name': 'David', 'label': 'w'}, {'name': 'Bret', 'label': 'w'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 's'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 's'}, {'name': 'Adam', 'label': 'w'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 's'}, {'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 's'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Adam', 'label': 'w'}]},
]



# *** Relationship Strong vs. Weak Undirected ***
# First 17 Episodes Strong vs. Weak (Undirected):

episode13_3_vinaka_sw = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': 's'}, {'name': 'Ken', 'label': 's'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': 's'}, {'name': 'Adam', 'label': 's'}, {'name': 'Hannah', 'label': 's'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': 's'}, {'name': 'Hannah', 'label': 's'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': 's'}, {'name': 'David', 'label': 's'}, {'name': 'Ken', 'label': 's'}]},
]



# create graphs

# create_graph(episode1_takali_sw, 'Episode 1: Takali Strong vs. Weak Relationships (Undirected)', 'episode1_takali_sw')
# create_graph(episode1_vanua_sw, 'Episode 1: Vanua Strong vs. Weak Relationships (Undirected)', 'episode1_vanua_sw')
# create_graph(episode2_takali_sw, 'Episode 2: Takali Strong vs. Weak Relationships (Undirected)', 'episode2_takali_sw')
# create_graph(episode2_vanua_sw, 'Episode 2: Vanua Strong vs. Weak Relationships (Undirected)', 'episode2_vanua_sw')
# create_graph(episode3_takali_sw, 'Episode 3: Takali Strong vs. Weak Relationships (Undirected)', 'episode3_takali_sw')
# create_graph(episode3_vanua_sw, 'Episode 3: Vanua Strong vs. Weak Relationships (Undirected)', 'episode3_vanua_sw')
# create_graph(episode4_takali_sw, 'Episode 4: Takali Strong vs. Weak Relationships (Undirected)', 'episode4_takali_sw')
# create_graph(episode4_vanua_sw, 'Episode 4: Vanua Strong vs. Weak Relationships (Undirected)', 'episode4_vanua_sw')
# create_graph(episode5_takali_sw, 'Episode 5: Takali Strong vs. Weak Relationships (Undirected)', 'episode5_takali_sw')
# create_graph(episode5_vanua_sw, 'Episode 5: Vanua Strong vs. Weak Relationships (Undirected)', 'episode5_vanua_sw')
# create_graph(episode5_Ikabula_sw, 'Episode 5: Ikabula Strong vs. Weak Relationships (Undirected)', 'episode5_Ikabula_sw')
# create_graph(episode6_takali_sw, 'Episode 6: Takali Strong vs. Weak Relationships (Undirected)', 'episode6_takali_sw')
# create_graph(episode6_vanua_sw, 'Episode 6: Vanua Strong vs. Weak Relationships (Undirected)', 'episode6_vanua_sw')
# create_graph(episode6_Ikabula_sw, 'Episode 6: Ikabula Strong vs. Weak Relationships (Undirected)', 'episode6_Ikabula_sw')
# create_graph(episode7_takali_sw, 'Episode 7: Takali Strong vs. Weak Relationships (Undirected)', 'episode7_takali_sw')
# create_graph(episode7_vanua_sw, 'Episode 7: Vanua Strong vs. Weak Relationships (Undirected)', 'episode7_vanua_sw')
# create_graph(episode7_Ikabula_sw, 'Episode 7: Ikabula Strong vs. Weak Relationships (Undirected)', 'episode7_Ikabula_sw')
# create_graph(episode8_vinaka_sw, 'Episode 8: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode8_vinaka_sw')
# create_graph(episode9_vinaka_sw, 'Episode 9: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode9_vinaka_sw')
# create_graph(episode10_1_vinaka_sw, 'Episode 10 - Part 1: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode10_1_vinaka_sw')
# create_graph(episode10_2_vinaka_sw, 'Episode 10 - Part 2: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode10_2_vinaka_sw')
# create_graph(episode11_vinaka_sw, 'Episode 11: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode11_vinaka_sw')
# create_graph(episode12_1_vinaka_sw, 'Episode 12 - Part 1: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode12_1_vinaka_sw')
# create_graph(episode12_2_vinaka_sw, 'Episode 12 - Part 2: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode12_2_vinaka_sw')
# create_graph(episode13_1_vinaka_sw, 'Episode 13 - Part 1: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode13_1_vinaka_sw')
# create_graph(episode13_2_vinaka_sw, 'Episode 13 - Part 2: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode13_2_vinaka_sw')
create_graph(episode13_3_vinaka_sw, 'Episode 13 - Part 3: Vinaka Strong vs. Weak Relationships (Undirected)', 'episode13_3_vinaka_sw')


