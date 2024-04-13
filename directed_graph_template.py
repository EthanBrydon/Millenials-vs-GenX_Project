import networkx as nx
import matplotlib.pyplot as plt

def create_graph(players, graph_title, graph_filename):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges
    for player in players:
        G.add_node(player['name'], color='lightcoral' if player['tribe'] == 'red' else 'thistle')
        for relationship in player['relationships']:
            G.add_edge(player['name'], relationship['name'], label=relationship['label'])
            G.add_edge(player['name'], relationship['name'], label=relationship['label'])

    # Define positions for nodes
    red_nodes = [player['name'] for player in players if player['tribe'] == 'red']
    purple_nodes = [player['name'] for player in players if player['tribe'] == 'purple']
    pos = nx.circular_layout(G)
#     pos = nx.spring_layout(G)
#     pos = nx.random_layout(G)
#     pos = nx.shell_layout(G, nlist=[red_nodes, purple_nodes])
    
    # Draw the graph
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1000, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=6)
    edge_labels = nx.get_edge_attributes(G, 'label')
    edge_colors = ['k'] * len(edge_labels)
    # edge_colors = ['red' if int(label) < 0 else 'blue' if int(label) > 0 else 'black' for label in edge_labels.values()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True, node_size=900, width=0.5, alpha=0.5, edgelist=G.edges())
    
    # color the labels based on vlaue
#     for edge, label in edge_labels.items():
#         if int(label) < 0:
#             color = 'red'
#         elif int(label) > 0:
#             color = 'blue'
#         else:
#             color = 'black'
    
    # color the labels based on + or - value
    for edge, label in edge_labels.items():
        if str(label) == '-':
            color = 'red'
        else:
            color = 'blue'                        
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): label}, font_size=8, label_pos=0.33, rotate=True, font_color=color)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5, label_pos=0.33, rotate=True)

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
    plt.savefig(graph_filename)

    plt.show()


# *** Relationship Strengths Directed ***
# First 1 Episodes Relationship Strengths (Directed):

episode1_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-4'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-3'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Bret', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Rachel', 'label': '-2'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-2'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Rachel', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
]

episode1_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '1'}, {'name': 'Mari', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '2'}, {'name': 'Figgy', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '2'}, {'name': 'Taylor', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Strengths Directed ***
# First 2 Episodes Relationship Strengths (Directed):

episode2_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '1'}, {'name': 'Bret', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '-2'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '3'}, {'name': 'Paul', 'label': '-1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '0'}, {'name': 'Chris', 'label': '1'}, {'name': 'CeCe', 'label': '-1'}]},  
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Paul', 'label': '-1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
]

episode2_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-2'}, {'name': 'Mari', 'label': '1'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '1'}, {'name': 'Figgy', 'label': '-4'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-1'}, {'name': 'Figgy', 'label': '-4'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Figgy', 'label': '4'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Mari', 'label': '-1'}, {'name': 'Figgy', 'label': '0'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '3'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Michelle', 'label': '3'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '4'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Mari', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '1'}, {'name': 'Mari', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 3 Episodes Relationship Strengths (Directed):

episode3_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '2'}, {'name': 'Jessica', 'label': '3'}, {'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Paul', 'label': '-2'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '2'}, {'name': 'Chris', 'label': '3'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '1'}, {'name': 'Paul', 'label': '2'}, {'name': 'Bret', 'label': '3'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Ken', 'label': '2'}, {'name': 'Paul', 'label': '-5'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'CeCe', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-1'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Paul', 'label': '-3'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '3'}, {'name': 'Paul', 'label': '-5'}, {'name': 'Chris', 'label': '1'}, {'name': 'CeCe', 'label': '0'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Lucy', 'label': '1'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '1'}, {'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '-1'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '-4'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Paul', 'label': '-4'}, {'name': 'Ken', 'label': '2'}, {'name': 'Lucy', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'CeCe', 'label': '-1'}, {'name': 'Lucy', 'label': '3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Chris', 'label': '1'}, {'name': 'Paul', 'label': '-2'}, {'name': 'Bret', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
]

episode3_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Hannah', 'label': '-1'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-1'}, {'name': 'Figgy', 'label': '-5'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Zeke', 'label': '-1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '4'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Figgy', 'label': '0'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '3'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Michelle', 'label': '3'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '5'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Hannah', 'label': '-1'}]},
]



# *** Relationship Strengths Directed ***
# First 4 Episodes Relationship Strengths (Directed):

episode4_takali = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-2'}, {'name': 'Lucy', 'label': '3'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '2'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '2'}, {'name': 'Chris', 'label': '4'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Lucy', 'label': '0'}, {'name': 'Jessica', 'label': '-4'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Bret', 'label': '4'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Lucy', 'label': '0'}, {'name': 'Jessica', 'label': '-4'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Ken', 'label': '2'}, {'name': 'Lucy', 'label': '-2'}, {'name': 'Sunday', 'label': '1'}, {'name': 'CeCe', 'label': '3'}, {'name': 'Jessica', 'label': '4'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-1'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Sunday', 'label': '3'}, {'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '3'}, {'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '4'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '0'}, {'name': 'Jessica', 'label': '0'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Lucy', 'label': '0'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '2'}, {'name': 'Lucy', 'label': '-1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '1'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'Lucy', 'label': '3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Chris', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'Ken', 'label': '-1'}]},
]

episode4_vanua = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Hannah', 'label': '-1'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-1'}, {'name': 'Figgy', 'label': '-5'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Zeke', 'label': '-1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '4'}, {'name': 'Figgy', 'label': '6'}, {'name': 'Michelle', 'label': '2'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '2'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Figgy', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '2'}, {'name': 'Figgy', 'label': '0'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '3'}, {'name': 'Figgy', 'label': '3'}, {'name': 'Michelle', 'label': '3'}, {'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Taylor', 'label': '5'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Michelle', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Zeke', 'label': '-2'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-3'}, {'name': 'Michaela', 'label': '-1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Hannah', 'label': '-1'}]},
]



# *** Relationship Strengths Directed ***
# First 5 Episodes Relationship Strengths (Directed):

episode5_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-4'}, {'name': 'Taylor', 'label': '-1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '5'}, {'name': 'Adam', 'label': '-1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '7'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '0'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
]

episode5_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'CeCe', 'label': '-6'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Michelle', 'label': '-2'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'CeCe', 'label': '-2'}, {'name': 'Chris', 'label': '1'}, {'name': 'David', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '1'}, {'name': 'Michelle', 'label': '0'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '2'}, {'name': 'CeCe', 'label': '-3'}, {'name': 'David', 'label': '0'}]},
]

episode5_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 6 Episodes Relationship Strengths (Directed):

episode6_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-6'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '7'}, {'name': 'Adam', 'label': '0'}, {'name': 'Ken', 'label': '-2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '10'}, {'name': 'Ken', 'label': '-2'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '2'}, {'name': 'Figgy', 'label': '-2'}, {'name': 'Adam', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '2'}, {'name': 'Adam', 'label': '2'}, {'name': 'Figgy', 'label': '-2'}]},
]

episode6_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'Chris', 'label': '1'}, {'name': 'David', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '2'}, {'name': 'Michelle', 'label': '0'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '2'}, {'name': 'David', 'label': '0'}]},
]

episode6_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 7 Episodes Relationship Strengths (Directed):

episode7_takali = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-1'}, {'name': 'Jessica', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Ken', 'label': '-1'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '2'}, {'name': 'Adam', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '2'}, {'name': 'Adam', 'label': '2'}]},
]

episode7_vanua = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Michelle', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '0'}, {'name': 'Chris', 'label': '1'}, {'name': 'David', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '2'}, {'name': 'Michelle', 'label': '0'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Chris', 'label': '2'}, {'name': 'David', 'label': '1'}]},
]

episode7_Ikabula = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '-2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '-1'}, {'name': 'Will', 'label': '3'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '-1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '0'}, {'name': 'Jay', 'label': '3'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '0'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '3'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '2'}, {'name': 'Bret', 'label': '-3'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '4'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '3'}, {'name': 'Michaela', 'label': '-2'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 8 Episodes Relationship Strengths (Directed):

episode8_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '3'}, {'name': 'Hannah', 'label': '0'}, {'name': 'Taylor', 'label': '0'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Will', 'label': '-2'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'David', 'label': '1'}, {'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '3'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Chris', 'label': '2'}, {'name': 'Bret', 'label': '2'}, {'name': 'Ken', 'label': '4'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '7'}, {'name': 'Chris', 'label': '3'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Adam', 'label': '3'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '3'}, {'name': 'Ken', 'label': '5'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jessica', 'label': '6'}, {'name': 'Michelle', 'label': '-3'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '0'}, {'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Zeke', 'label': '0'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Bret', 'label': '-2'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '1'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '3'}, {'name': 'Taylor', 'label': '2'}, {'name': 'Jay', 'label': '5'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '0'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-3'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '2'}, {'name': 'Bret', 'label': '5'}, {'name': 'Chris', 'label': '3'}, {'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '3'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '3'}, {'name': 'Chris', 'label': '7'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '1'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '5'}, {'name': 'Michelle', 'label': '6'}, {'name': 'Will', 'label': '6'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '0'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Adam', 'label': '-4'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Michelle', 'label': '-2'}, {'name': 'Chris', 'label': '3'}, {'name': 'David', 'label': '3'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Taylor', 'label': '-3'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '1'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '5'}, {'name': 'Michelle', 'label': '3'}, {'name': 'Will', 'label': '3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Ken', 'label': '-1'}, {'name': 'Adam', 'label': '-6'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '2'}, {'name': 'Jay', 'label': '6'}, {'name': 'Taylor', 'label': '4'}, {'name': 'Will', 'label': '3'}, {'name': 'Zeke', 'label': '0'}, {'name': 'Chris', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Adam', 'label': '-2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '3'}, {'name': 'Bret', 'label': '6'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Michelle', 'label': '-1'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 9 Episodes Relationship Strengths (Directed):

episode9_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '4'}, {'name': 'Hannah', 'label': '0'}, {'name': 'Taylor', 'label': '-4'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Ken', 'label': '3'}, {'name': 'Will', 'label': '-2'}, {'name': 'David', 'label': '2'}, {'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '2'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jay', 'label': '0'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '3'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Chris', 'label': '2'}, {'name': 'Bret', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Taylor', 'label': '-1'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '8'}, {'name': 'Chris', 'label': '4'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Adam', 'label': '4'}, {'name': 'Zeke', 'label': '3'}, {'name': 'Taylor', 'label': '-3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Jay', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'Chris', 'label': '4'}, {'name': 'Ken', 'label': '6'}, {'name': 'Taylor', 'label': '-5'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Jessica', 'label': '6'}, {'name': 'Zeke', 'label': '5'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '1'}, {'name': 'Will', 'label': '3'}, {'name': 'Jay', 'label': '0'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '1'}, {'name': 'Jessica', 'label': '3'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '3'}, {'name': 'Jay', 'label': '4'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-3'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '0'}, {'name': 'Bret', 'label': '6'}, {'name': 'Chris', 'label': '5'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '4'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Taylor', 'label': '-2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '3'}, {'name': 'Chris', 'label': '8'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '1'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '4'}, {'name': 'Will', 'label': '7'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '0'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Adam', 'label': '-7'}, {'name': 'Zeke', 'label': '0'}, {'name': 'Jessica', 'label': '-1'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '3'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Chris', 'label': '4'}, {'name': 'David', 'label': '4'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Ken', 'label': '3'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Taylor', 'label': '-5'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '7'}, {'name': 'Will', 'label': '4'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Ken', 'label': '-1'}, {'name': 'Adam', 'label': '-11'}, {'name': 'Jessica', 'label': '1'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '5'}, {'name': 'Bret', 'label': '8'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Zeke', 'label': '5'}, {'name': 'Taylor', 'label': '-2'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Jay', 'label': '1'}]},
]



# *** Relationship Strengths Directed ***
# First 10 Episodes Relationship Strengths (Directed):

episode10_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '5'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Jessica', 'label': '4'}, {'name': 'Ken', 'label': '5'}, {'name': 'Will', 'label': '-1'}, {'name': 'David', 'label': '4'}, {'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '0'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jay', 'label': '-1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '4'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Bret', 'label': '2'}, {'name': 'Ken', 'label': '5'}, {'name': 'Adam', 'label': '3'}, {'name': 'Zeke', 'label': '3'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '10'}, {'name': 'Chris', 'label': '2'}, {'name': 'Jessica', 'label': '5'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Adam', 'label': '5'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Chris', 'label': '1'}, {'name': 'Ken', 'label': '9'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jessica', 'label': '9'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Adam', 'label': '2'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '4'}, {'name': 'Jay', 'label': '0'}, {'name': 'Zeke', 'label': '3'}, {'name': 'Adam', 'label': '0'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '2'}, {'name': 'Chris', 'label': '-1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '3'}, {'name': 'Jessica', 'label': '4'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '3'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Chris', 'label': '-2'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '-2'}, {'name': 'Bret', 'label': '7'}, {'name': 'Chris', 'label': '6'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '5'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '2'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '0'}, {'name': 'Ken', 'label': '3'}, {'name': 'Chris', 'label': '10'}, {'name': 'Sunday', 'label': '8'}, {'name': 'Jessica', 'label': '-5'}, {'name': 'Will', 'label': '2'}, {'name': 'Jay', 'label': '0'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '3'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '7'}, {'name': 'Hannah', 'label': '2'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Adam', 'label': '-7'}, {'name': 'Zeke', 'label': '0'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '1'}, {'name': 'Chris', 'label': '2'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '4'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Chris', 'label': '3'}, {'name': 'David', 'label': '7'}, {'name': 'Jay', 'label': '-1'}, {'name': 'Ken', 'label': '4'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '5'}, {'name': 'Bret', 'label': '11'}, {'name': 'Sunday', 'label': '8'}, {'name': 'Jessica', 'label': '-6'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Adam', 'label': '2'}, {'name': 'Jay', 'label': '2'}]},
]



# *** Relationship Strengths Directed ***
# First 11 Episodes Relationship Strengths (Directed):

episode10_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '9'}, {'name': 'Hannah', 'label': '1'}, {'name': 'Jessica', 'label': '6'}, {'name': 'Ken', 'label': '7'}, {'name': 'Will', 'label': '-1'}, {'name': 'David', 'label': '6'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jay', 'label': '-1'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '7'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Bret', 'label': '2'}, {'name': 'Ken', 'label': '10'}, {'name': 'Adam', 'label': '5'}, {'name': 'Zeke', 'label': '7'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Jay', 'label': '-3'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '13'}, {'name': 'Jessica', 'label': '7'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Adam', 'label': '7'}, {'name': 'Zeke', 'label': '8'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Ken', 'label': '14'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jessica', 'label': '12'}, {'name': 'Zeke', 'label': '8'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '4'}, {'name': 'Will', 'label': '0'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '4'}, {'name': 'Jay', 'label': '0'}, {'name': 'Zeke', 'label': '4'}, {'name': 'Adam', 'label': '2'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '5'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '4'}, {'name': 'Jessica', 'label': '5'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '5'}, {'name': 'Hannah', 'label': '8'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Adam', 'label': '-2'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Zeke', 'label': '3'}, {'name': 'David', 'label': '1'}, {'name': 'Ken', 'label': '1'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '-2'}, {'name': 'Bret', 'label': '9'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Will', 'label': '3'}, {'name': 'Jay', 'label': '7'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '4'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Sunday', 'label': '10'}, {'name': 'Jessica', 'label': '-5'}, {'name': 'Will', 'label': '4'}, {'name': 'Jay', 'label': '2'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Adam', 'label': '1'}, {'name': 'Zeke', 'label': '7'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '9'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '7'}, {'name': 'Adam', 'label': '-7'}, {'name': 'Zeke', 'label': '1'}, {'name': 'Jessica', 'label': '-3'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '5'}, {'name': 'Hannah', 'label': '7'}, {'name': 'David', 'label': '5'}, {'name': 'Jay', 'label': '1'}, {'name': 'Ken', 'label': '4'}, {'name': 'Jessica', 'label': '2'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Will', 'label': '4'}]},
]



# *** Relationship Strengths Directed ***
# First 12 Episodes Relationship Strengths (Directed):

episode11_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '7'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Ken', 'label': '8'}, {'name': 'Will', 'label': '0'}, {'name': 'David', 'label': '8'}, {'name': 'Bret', 'label': '1'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jay', 'label': '0'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '15'}, {'name': 'Sunday', 'label': '5'}, {'name': 'Adam', 'label': '9'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Jay', 'label': '1'}, {'name': 'Will', 'label': '2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '0'}, {'name': 'Ken', 'label': '15'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Zeke', 'label': '6'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Hannah', 'label': '7'}, {'name': 'Adam', 'label': '6'}, {'name': 'Will', 'label': '1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '5'}, {'name': 'Jay', 'label': '0'}, {'name': 'Zeke', 'label': '2'}, {'name': 'Adam', 'label': '5'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '7'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Ken', 'label': '6'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '4'}, {'name': 'Hannah', 'label': '9'}, {'name': 'Bret', 'label': '2'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-1'}, {'name': 'Zeke', 'label': '-1'}, {'name': 'David', 'label': '2'}, {'name': 'Ken', 'label': '0'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '11'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Will', 'label': '3'}, {'name': 'Jay', 'label': '9'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Adam', 'label': '2'}, {'name': 'Zeke', 'label': '6'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '2'}, {'name': 'Sunday', 'label': '12'}, {'name': 'Will', 'label': '5'}, {'name': 'Jay', 'label': '4'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Adam', 'label': '0'}, {'name': 'Zeke', 'label': '9'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '11'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '-6'}, {'name': 'Zeke', 'label': '3'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '-1'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '5'}, {'name': 'Hannah', 'label': '5'}, {'name': 'David', 'label': '4'}, {'name': 'Jay', 'label': '3'}, {'name': 'Ken', 'label': '4'}, {'name': 'Bret', 'label': '7'}, {'name': 'Sunday', 'label': '7'}, {'name': 'Will', 'label': '6'}]},
]



# *** Relationship Strengths Directed ***
# First 13 Episodes Relationship Strengths (Directed):

episode12_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '8'}, {'name': 'Ken', 'label': '9'}, {'name': 'Will', 'label': '-3'}, {'name': 'David', 'label': '8'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Jay', 'label': '-1'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '16'}, {'name': 'Sunday', 'label': '6'}, {'name': 'Adam', 'label': '10'}, {'name': 'Hannah', 'label': '6'}, {'name': 'Jay', 'label': '0'}, {'name': 'Will', 'label': '0'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Ken', 'label': '16'}, {'name': 'Sunday', 'label': '3'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Hannah', 'label': '8'}, {'name': 'Adam', 'label': '7'}, {'name': 'Will', 'label': '-1'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '3'}, {'name': 'Jay', 'label': '0'}, {'name': 'Adam', 'label': '7'}, {'name': 'Bret', 'label': '0'}, {'name': 'David', 'label': '9'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Ken', 'label': '7'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '9'}, {'name': 'Bret', 'label': '2'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Adam', 'label': '-1'}, {'name': 'David', 'label': '-1'}, {'name': 'Ken', 'label': '0'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '14'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '5'}, {'name': 'Will', 'label': '0'}, {'name': 'Jay', 'label': '8'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Adam', 'label': '4'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-2'}, {'name': 'Ken', 'label': '3'}, {'name': 'Sunday', 'label': '14'}, {'name': 'Will', 'label': '1'}, {'name': 'Jay', 'label': '3'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '12'}, {'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '5'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '-6'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '-4'}]},
]



# *** Relationship Strengths Directed ***
# First 14 Episodes Relationship Strengths (Directed):

episode12_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '9'}, {'name': 'Ken', 'label': '10'}, {'name': 'David', 'label': '8'}, {'name': 'Bret', 'label': '3'}, {'name': 'Sunday', 'label': '2'}, {'name': 'Jay', 'label': '-2'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '3'}, {'name': 'David', 'label': '17'}, {'name': 'Sunday', 'label': '4'}, {'name': 'Adam', 'label': '11'}, {'name': 'Hannah', 'label': '7'}, {'name': 'Jay', 'label': '0'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Ken', 'label': '17'}, {'name': 'Sunday', 'label': '1'}, {'name': 'Jay', 'label': '-2'}, {'name': 'Hannah', 'label': '9'}, {'name': 'Adam', 'label': '8'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '0'}, {'name': 'Adam', 'label': '8'}, {'name': 'Bret', 'label': '0'}, {'name': 'David', 'label': '10'}, {'name': 'Sunday', 'label': '-1'}, {'name': 'Ken', 'label': '8'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '14'}, {'name': 'David', 'label': '3'}, {'name': 'Ken', 'label': '5'}, {'name': 'Jay', 'label': '6'}, {'name': 'Hannah', 'label': '4'}, {'name': 'Adam', 'label': '4'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-4'}, {'name': 'Ken', 'label': '3'}, {'name': 'Sunday', 'label': '14'}, {'name': 'Jay', 'label': '4'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '2'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '6'}, {'name': 'Sunday', 'label': '9'}, {'name': 'Adam', 'label': '-4'}, {'name': 'Ken', 'label': '1'}, {'name': 'David', 'label': '-7'}]},
]



# *** Relationship Strengths Directed ***
# First 15 Episodes Relationship Strengths (Directed):

episode13_1_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '10'}, {'name': 'Ken', 'label': '11'}, {'name': 'David', 'label': '10'}, {'name': 'Bret', 'label': '4'}, {'name': 'Jay', 'label': '-2'}]},  
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '4'}, {'name': 'David', 'label': '18'}, {'name': 'Adam', 'label': '12'}, {'name': 'Hannah', 'label': '8'}, {'name': 'Jay', 'label': '-2'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '1'}, {'name': 'Ken', 'label': '18'}, {'name': 'Jay', 'label': '-3'}, {'name': 'Hannah', 'label': '10'}, {'name': 'Adam', 'label': '10'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '-1'}, {'name': 'Adam', 'label': '9'}, {'name': 'Bret', 'label': '1'}, {'name': 'David', 'label': '11'}, {'name': 'Ken', 'label': '9'}]},    
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-5'}, {'name': 'Ken', 'label': '4'}, {'name': 'Jay', 'label': '0'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '4'}]},  
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '3'}, {'name': 'Bret', 'label': '6'}, {'name': 'Adam', 'label': '-2'}, {'name': 'Ken', 'label': '-1'}, {'name': 'David', 'label': '-5'}]},   
]



# *** Relationship Strengths Directed ***
# First 16 Episodes Relationship Strengths (Directed):

episode13_2_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '10'}, {'name': 'Ken', 'label': '11'}, {'name': 'David', 'label': '7'}, {'name': 'Bret', 'label': '7'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '2'}, {'name': 'David', 'label': '19'}, {'name': 'Adam', 'label': '12'}, {'name': 'Hannah', 'label': '9'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-1'}, {'name': 'Ken', 'label': '20'}, {'name': 'Hannah', 'label': '12'}, {'name': 'Adam', 'label': '9'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '9'}, {'name': 'Bret', 'label': '-1'}, {'name': 'David', 'label': '12'}, {'name': 'Ken', 'label': '10'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-9'}, {'name': 'Ken', 'label': '4'}, {'name': 'Hannah', 'label': '5'}, {'name': 'Adam', 'label': '6'}]},
]



# *** Relationship Strengths Directed ***
# First 17 Episodes Relationship Strengths (Directed):

episode13_3_vinaka = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '11'}, {'name': 'Ken', 'label': '11'}, {'name': 'David', 'label': '5'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '18'}, {'name': 'Adam', 'label': '12'}, {'name': 'Hannah', 'label': '9'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '21'}, {'name': 'Hannah', 'label': '12'}, {'name': 'Adam', 'label': '7'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '11'}, {'name': 'David', 'label': '9'}, {'name': 'Ken', 'label': '11'}]},
]


# create all relationship strength directed graphs
# create_graph(episode1_takali, 'Episode 1: Takali Relationship Strengths (Directed)', 'episode1_takali.png')
# create_graph(episode1_vanua, 'Episode 1: Vanua Relationship Strengths (Directed)', 'episode1_vanua.png')
# create_graph(episode2_takali, 'Episode 2: Takali Relationship Strengths (Directed)', 'episode2_takali.png')
# create_graph(episode2_vanua, 'Episode 2: Vanua Relationship Strengths (Directed)', 'episode2_vanua.png')
# create_graph(episode3_takali, 'Episode 3: Takali Relationship Strengths (Directed)', 'episode3_takali.png')
# create_graph(episode3_vanua, 'Episode 3: Vanua Relationship Strengths (Directed)', 'episode3_vanua.png')
# create_graph(episode4_takali, 'Episode 4: Takali Relationship Strengths (Directed)', 'episode4_takali.png')
# create_graph(episode4_vanua, 'Episode 4: Vanua Relationship Strengths (Directed)', 'episode4_vanua.png')
# create_graph(episode5_takali, 'Episode 5: Takali Relationship Strengths (Directed)', 'episode5_takali.png')
# create_graph(episode5_vanua, 'Episode 5: Vanua Relationship Strengths (Directed)', 'episode5_vanua.png')
# create_graph(episode5_Ikabula, 'Episode 5: Ikabula Relationship Strengths (Directed)', 'episode5_Ikabula.png')
# create_graph(episode6_takali, 'Episode 6: Takali Relationship Strengths (Directed)', 'episode6_takali.png')
# create_graph(episode6_vanua, 'Episode 6: Vanua Relationship Strengths (Directed)', 'episode6_vanua.png')
# create_graph(episode6_Ikabula, 'Episode 6: Ikabula Relationship Strengths (Directed)', 'episode6_Ikabula.png')
# create_graph(episode7_takali, 'Episode 7: Takali Relationship Strengths (Directed)', 'episode7_takali.png')
# create_graph(episode7_vanua, 'Episode 7: Vanua Relationship Strengths (Directed)', 'episode7_vanua.png')
# create_graph(episode7_Ikabula, 'Episode 7: Ikabula Relationship Strengths (Directed)', 'episode7_Ikabula.png')
# create_graph(episode8_vinaka, 'Episode 8: Vinaka Relationship Strengths (Directed)', 'episode8_vinaka.png')
# create_graph(episode9_vinaka, 'Episode 9: Vinaka Relationship Strengths (Directed)', 'episode9_vinaka.png')
# create_graph(episode10_1_vinaka, 'Episode 10 - Part 1: Vinaka Relationship Strengths (Directed)', 'episode10_1_vinaka.png')
# create_graph(episode10_2_vinaka, 'Episode 10 - Part 2: Vinaka Relationship Strengths (Directed)', 'episode10_2_vinaka.png')
# create_graph(episode11_vinaka, 'Episode 11: Vinaka Relationship Strengths (Directed)', 'episode11_vinaka.png')
# create_graph(episode12_1_vinaka, 'Episode 12 - Part 1: Vinaka Relationship Strengths (Directed)', 'episode12_1_vinaka.png')
# create_graph(episode12_2_vinaka, 'Episode 12 - Part 2: Vinaka Relationship Strengths (Directed)', 'episode12_2_vinaka.png')
# create_graph(episode13_1_vinaka, 'Episode 13 - Part 1: Vinaka Relationship Strengths (Directed)', 'episode13_1_vinaka.png')
# create_graph(episode13_2_vinaka, 'Episode 13 - Part 2: Vinaka Relationship Strengths (Directed)', 'episode13_2_vinaka.png')
# create_graph(episode13_3_vinaka, 'Episode 13 - Part 3: Vinaka Relationship Strengths (Directed)', 'episode13_3_vinaka.png')



# *** Relationship Positive vs. Negative Directed ***
# First 1 Episodes Positive vs. Negative (Directed):

episode1_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Rachel', 'label': '-'}]},
        {'name': 'Rachel', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Rachel', 'label': '-'}, {'name': 'CeCe', 'label': '-'}]},  
]

episode1_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': []},
        {'name': 'Mari', 'tribe': 'red', 'relationships': []},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': []},
]



# *** Relationship Positive vs. Negative Directed ***
# First 2 Episodes Positive vs. Negative (Directed):

episode2_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Paul', 'label': '-'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'CeCe', 'label': '-'}]},
]

episode2_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}]},
        {'name': 'Mari', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}]},
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}, {'name': 'Figgy', 'label': '-'}, {'name': 'Mari', 'label': '-'}]},    
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Mari', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Mari', 'label': '-'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Mari', 'label': '-'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Mari', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 3 Episodes Positive vs. Negative (Directed):

episode3_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Paul', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Paul', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '-'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Paul', 'label': '-'}, {'name': 'Ken', 'label': '+'}]},        
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Paul', 'label': '-'}]},
]

episode3_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},        
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}, {'name': 'Figgy', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Zeke', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},     
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},     
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 4 Episodes Positive vs. Negative (Directed):

episode4_takali_pn = [
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Lucy', 'label': '-'}, {'name': 'CeCe', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Lucy', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Lucy', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'CeCe', 'label': '-'}, {'name': 'Lucy', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '-'}]},
]

episode4_vanua_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},        
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}, {'name': 'Figgy', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Zeke', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},     
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Figgy', 'label': '+'}, {'name': 'Michelle', 'label': '+'}]},     
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Michaela', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 5 Episodes Positive vs. Negative (Directed):

episode5_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': []},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': []},
]

episode5_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'CeCe', 'label': '-'}, {'name': 'Zeke', 'label': '+'}]},      
        {'name': 'CeCe', 'tribe': 'purple', 'relationships': [{'name': 'Michelle', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'CeCe', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}, {'name': 'CeCe', 'label': '-'}]},
]

episode5_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
]



# *** Relationship Positive vs. Negative Directed ***
# First 6 Episodes Positive vs. Negative (Directed):

episode6_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '-'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Figgy', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Ken', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Figgy', 'label': '+'}, {'name': 'Ken', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Figgy', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Figgy', 'label': '-'}]},     
]

episode6_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}]},
]

episode6_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': []},
        {'name': 'Jay', 'tribe': 'red', 'relationships': []},
        {'name': 'Will', 'tribe': 'red', 'relationships': []},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': []},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': []},
]



# *** Relationship Positive vs. Negative Directed ***
# First 7 Episodes Positive vs. Negative (Directed):

episode7_takali_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Ken', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
]

episode7_vanua_pn = [
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': []},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Chris', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Chris', 'label': '+'}]},
]

episode7_Ikabula_pn = [
        {'name': 'Michaela', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Michaela', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Michaela', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Sunday', 'label': '+'}, {'name': 'Michaela', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 8 Episodes Positive vs. Negative (Directed):

episode8_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '-'}, {'name': 'Bret', 'label': '-'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Michelle', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Michelle', 'label': '-'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Michelle', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Ken', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Michelle', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Michelle', 'label': '-'}, {'name': 'Taylor', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 9 Episodes Positive vs. Negative (Directed):

episode9_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}]},       
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},        
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Bret', 'label': '-'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Hannah', 'label': '+'}]},       
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Taylor', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Taylor', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Ken', 'label': '-'}, {'name': 'Adam', 'label': '-'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Taylor', 'label': '-'}, {'name': 'Adam', 'label': '+'}]},       
]



# *** Relationship Positive vs. Negative Directed ***
# First 10 Episodes Positive vs. Negative (Directed):

episode10_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},       
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Chris', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Chris', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Chris', 'label': '+'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Chris', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Chris', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Jay', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 11 Episodes Positive vs. Negative (Directed):

episode10_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Jessica', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Jessica', 'label': '-'}, {'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jessica', 'label': '-'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Jessica', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jessica', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 12 Episodes Positive vs. Negative (Directed):

episode11_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Zeke', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Zeke', 'label': '-'}, {'name': 'David', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Zeke', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Zeke', 'label': '+'}, {'name': 'David', 'label': '-'}]},
        {'name': 'Zeke', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Will', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 13 Episodes Positive vs. Negative (Directed):

episode12_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Will', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Will', 'label': '-'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Will', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Will', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 14 Episodes Positive vs. Negative (Directed):

episode12_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Sunday', 'label': '-'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Sunday', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Jay', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Sunday', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'David', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 15 Episodes Positive vs. Negative (Directed):

episode13_1_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Jay', 'label': '-'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Jay', 'label': '-'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Jay', 'label': '-'}, {'name': 'Adam', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Jay', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Bret', 'label': '+'}, {'name': 'Adam', 'label': '-'}, {'name': 'Ken', 'label': '-'}, {'name': 'David', 'label': '-'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 16 Episodes Positive vs. Negative (Directed):

episode13_2_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Bret', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Bret', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'Bret', 'label': '-'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
        {'name': 'Bret', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '-'}, {'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},
]



# *** Relationship Positive vs. Negative Directed ***
# First 17 Episodes Positive vs. Negative (Directed):

episode13_3_vinaka_pn = [
        {'name': 'Adam', 'tribe': 'red', 'relationships': [{'name': 'Hannah', 'label': '+'}, {'name': 'Ken', 'label': '+'}, {'name': 'David', 'label': '+'}]},
        {'name': 'Ken', 'tribe': 'purple', 'relationships': [{'name': 'David', 'label': '+'}, {'name': 'Adam', 'label': '+'}, {'name': 'Hannah', 'label': '+'}]},      
        {'name': 'David', 'tribe': 'purple', 'relationships': [{'name': 'Ken', 'label': '+'}, {'name': 'Hannah', 'label': '+'}, {'name': 'Adam', 'label': '+'}]},      
        {'name': 'Hannah', 'tribe': 'red', 'relationships': [{'name': 'Adam', 'label': '+'}, {'name': 'David', 'label': '+'}, {'name': 'Ken', 'label': '+'}]},
]


# create positive and negative relationship graphs
# create_graph(episode1_takali_pn, 'Episode 1: Takali Positive vs. Negative Relationships (Directed)', 'episode1_takali_pn.png')
# create_graph(episode1_vanua_pn, 'Episode 1: Vanua Positive vs. Negative Relationships (Directed)', 'episode1_vanua_pn.png')
# create_graph(episode2_takali_pn, 'Episode 2: Takali Positive vs. Negative Relationships (Directed)', 'episode2_takali_pn.png')
# create_graph(episode2_vanua_pn, 'Episode 2: Vanua Positive vs. Negative Relationships (Directed)', 'episode2_vanua_pn.png')
# create_graph(episode3_takali_pn, 'Episode 3: Takali Positive vs. Negative Relationships (Directed)', 'episode3_takali_pn.png')
# create_graph(episode3_vanua_pn, 'Episode 3: Vanua Positive vs. Negative Relationships (Directed)', 'episode3_vanua_pn.png')
# create_graph(episode4_takali_pn, 'Episode 4: Takali Positive vs. Negative Relationships (Directed)', 'episode4_takali_pn.png')
# create_graph(episode4_vanua_pn, 'Episode 4: Vanua Positive vs. Negative Relationships (Directed)', 'episode4_vanua_pn.png')
# create_graph(episode5_takali_pn, 'Episode 5: Takali Positive vs. Negative Relationships (Directed)', 'episode5_takali_pn.png')
# create_graph(episode5_vanua_pn, 'Episode 5: Vanua Positive vs. Negative Relationships (Directed)', 'episode5_vanua_pn.png')
# create_graph(episode5_Ikabula_pn, 'Episode 5: Ikabula Positive vs. Negative Relationships (Directed)', 'episode5_Ikabula_pn.png')
# create_graph(episode6_takali_pn, 'Episode 6: Takali Positive vs. Negative Relationships (Directed)', 'episode6_takali_pn.png')
# create_graph(episode6_vanua_pn, 'Episode 6: Vanua Positive vs. Negative Relationships (Directed)', 'episode6_vanua_pn.png')
# create_graph(episode6_Ikabula_pn, 'Episode 6: Ikabula Positive vs. Negative Relationships (Directed)', 'episode6_Ikabula_pn.png')
# create_graph(episode7_takali_pn, 'Episode 7: Takali Positive vs. Negative Relationships (Directed)', 'episode7_takali_pn.png')
# create_graph(episode7_vanua_pn, 'Episode 7: Vanua Positive vs. Negative Relationships (Directed)', 'episode7_vanua_pn.png')
# create_graph(episode7_Ikabula_pn, 'Episode 7: Ikabula Positive vs. Negative Relationships (Directed)', 'episode7_Ikabula_pn.png')
create_graph(episode8_vinaka_pn, 'Episode 8: Vinaka Positive vs. Negative Relationships (Directed)', 'episode8_vinaka_pn.png')
create_graph(episode9_vinaka_pn, 'Episode 9: Vinaka Positive vs. Negative Relationships (Directed)', 'episode9_vinaka_pn.png')
create_graph(episode10_1_vinaka_pn, 'Episode 10 - Part 1: Vinaka Positive vs. Negative Relationships (Directed)', 'episode10_1_vinaka_pn.png')
# create_graph(episode10_2_vinaka_pn, 'Episode 10 - Part 2: Vinaka Positive vs. Negative Relationships (Directed)', 'episode10_2_vinaka_pn.png')
# create_graph(episode11_vinaka_pn, 'Episode 11: Vinaka Positive vs. Negative Relationships (Directed)', 'episode11_vinaka_pn.png')
# create_graph(episode12_1_vinaka_pn, 'Episode 12 - Part 1: Vinaka Positive vs. Negative Relationships (Directed)', 'episode12_1_vinaka_pn.png')
# create_graph(episode12_2_vinaka_pn, 'Episode 12 - Part 2: Vinaka Positive vs. Negative Relationships (Directed)', 'episode12_2_vinaka_pn.png')
# create_graph(episode13_1_vinaka_pn, 'Episode 13 - Part 1: Vinaka Positive vs. Negative Relationships (Directed)', 'episode13_1_vinaka_pn.png')
# create_graph(episode13_2_vinaka_pn, 'Episode 13 - Part 2: Vinaka Positive vs. Negative Relationships (Directed)', 'episode13_2_vinaka_pn.png')
# create_graph(episode13_3_vinaka_pn, 'Episode 13 - Part 3: Vinaka Positive vs. Negative Relationships (Directed)', 'episode13_3_vinaka_pn.png')

