import numpy as np


# Split the player interactions by episode
# Takes a 2D numpy array of player interactions and returns a list of 2D numpy arrays of player interactions, each array representing an episode
def split_rows_by_episode(player_interactions):
    episodes = []
    current_episode = []
    current_episode_number = player_interactions[0][0]
    for row in player_interactions:
        if row[0] == current_episode_number:
            current_episode.append(row)
        else:
            episodes.append(current_episode)
            current_episode = []
            current_episode_number = row[0]
            current_episode.append(row)
    episodes.append(np.array(current_episode))
    return episodes


# Calculate the relationship strengths between players in the given episodes
# Takes a list of 2D numpy arrays of player interactions and returns a dictionary of dictionaries, where the keys are the names of the players and the values are dictionaries of the players they interacted with and the strength of the relationship
def calculate_relationship_strengths_directed(numpy_episodes):
    relationship_strengths = {}
    for episode in numpy_episodes:
        for row in episode:
            player_1 = row[1]
            player_2 = row[2]
            interaction_type = row[3]
            if player_1 in relationship_strengths:
                if player_2 in relationship_strengths[player_1]:
                    relationship_strengths[player_1][player_2] += int(interaction_type)
                else:
                    relationship_strengths[player_1][player_2] = int(interaction_type)
            else:
                relationship_strengths[player_1] = {player_2: int(interaction_type)}
    return relationship_strengths


# Calculate the relationship strengths between players in the given episodes
# Takes a list of 2D numpy arrays of player interactions and returns a dictionary of dictionaries, where the keys are the names of the players and the values are dictionaries of the players they interacted with and the strength of the relationship
def calculate_relationship_strengths_undirected(numpy_episodes):
    relationship_strengths = {}
    for episode in numpy_episodes:
        for row in episode:
            player_1 = row[1]
            player_2 = row[2]
            interaction_type = row[3]
            if player_1 in relationship_strengths:
                if player_2 in relationship_strengths[player_1]:
                    relationship_strengths[player_1][player_2] += int(interaction_type)
                else:
                    relationship_strengths[player_1][player_2] = int(interaction_type)
            else:
                relationship_strengths[player_1] = {player_2: int(interaction_type)}
            if player_2 in relationship_strengths:
                if player_1 in relationship_strengths[player_2]:
                    relationship_strengths[player_2][player_1] += int(interaction_type)
                else:
                    relationship_strengths[player_2][player_1] = int(interaction_type)
            else:
                relationship_strengths[player_2] = {player_1: int(interaction_type)}
    return relationship_strengths


# Calculate the relationship strengths between players in a given episode
# Takes a 2D numpy array of player interactions and returns a dictionary of dictionaries, where the keys are the names of the players and the values are dictionaries of the players they interacted with and the strength of the relationship
def calculate_relationship_strengths_episode_directed(numpy_episode):
    relationship_strengths = {}
    for row in numpy_episode:
            player_1 = row[1]
            player_2 = row[2]
            interaction_type = row[3]
            if player_1 in relationship_strengths:
                if player_2 in relationship_strengths[player_1]:
                    relationship_strengths[player_1][player_2] += int(interaction_type)
                else:
                    relationship_strengths[player_1][player_2] = int(interaction_type)
            else:
                relationship_strengths[player_1] = {player_2: int(interaction_type)}
    return relationship_strengths


# Calculate the relationship strengths between players in a given episode
# Takes a 2D numpy array of player interactions and returns a dictionary of dictionaries, where the keys are the names of the players and the values are dictionaries of the players they interacted with and the strength of the relationship
def calculate_relationship_strengths_episode_undirected(numpy_episode):
    relationship_strengths = {}
    for row in numpy_episode:
            player_1 = row[1]
            player_2 = row[2]
            interaction_type = row[3]
            if player_1 in relationship_strengths:
                if player_2 in relationship_strengths[player_1]:
                    relationship_strengths[player_1][player_2] += int(interaction_type)
                else:
                    relationship_strengths[player_1][player_2] = int(interaction_type)
            else:
                relationship_strengths[player_1] = {player_2: int(interaction_type)}
            if player_2 in relationship_strengths:
                if player_1 in relationship_strengths[player_2]:
                    relationship_strengths[player_2][player_1] += int(interaction_type)
                else:
                    relationship_strengths[player_2][player_1] = int(interaction_type)
            else:
                relationship_strengths[player_2] = {player_1: int(interaction_type)}
    return relationship_strengths


# Convert the relationship strengths dictionary to a string
# Takes a dictionary of dictionaries of relationship strengths and returns a string representation of the dictionary
def toString(relationship_strengths):
    string = ''
    for player in relationship_strengths:
        string += player + ': {'
        for other_player in relationship_strengths[player]:
            string += other_player + ': ' + str(relationship_strengths[player][other_player]) + ', '
        string = string[:-2] + '}\n'
    return string


# Convert the relationship strengths dictionary to a string for the graph template
# Example:     {'name': 'Paul', 'tribe': 'purple', 'relationships': []},
def toStringForGraphTemplate(relationship_strengths):
    string = ''
    for player in relationship_strengths:
        string += '{\'name\': \'' + player + '\', \'tribe\': \'purple\', \'relationships\': ['
        for other_player in relationship_strengths[player]:
            string += '{\'name\': \'' + other_player + '\', \'label\': \'' + str(relationship_strengths[player][other_player]) + '\'}, '
        string = string[:-2] + ']},\n'
    return string


# Main function
def main():

    # Load the player interactions data from the csv file
    episodes_1_2_player_interactions_fullpath = r'C:\Users\Ethan\Documents\Educational\School Terms\Winter 2024\COMP 4602 A\Project\Millenials-vs-GenX_Project\excel_data\Survivor_Player_Interactions_E12.csv'

    player_interactions = np.loadtxt(episodes_1_2_player_interactions_fullpath, delimiter=',', dtype=str, skiprows=1)

    episodes = split_rows_by_episode(player_interactions)
    
    relationship_strengths_ep1_dir = calculate_relationship_strengths_episode_directed(episodes[0])
    relationship_strengths_dir = calculate_relationship_strengths_directed(episodes)

    print("*** Directed Relationship Strengths ***")
    print('Episode 1 Relationship Strengths (Directed):')
    print(toStringForGraphTemplate(relationship_strengths_ep1_dir))
    print()
    print('First 2 Episodes Relationship Strengths (Directed):')
    print(toStringForGraphTemplate(relationship_strengths_dir))
    print()
    print()

    relationship_strengths_ep1_un = calculate_relationship_strengths_episode_undirected(episodes[0])
    relationship_strengths_un = calculate_relationship_strengths_undirected(episodes)

    print("*** Undirected Relationship Strengths ***")
    print('Episode 1 Relationship Strengths (Undirected):')
    print(toStringForGraphTemplate(relationship_strengths_ep1_un))
    print()
    print('First 2 Episodes Relationship Strengths (Undirected):')
    print(toStringForGraphTemplate(relationship_strengths_un))
    print()
    print()


if __name__ == '__main__':
    main()