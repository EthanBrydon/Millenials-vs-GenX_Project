import numpy as np
from episode_tribes import get_episode_players_list

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


def tribe_color(name):
    if name in ['Sunday', 'Bret', 'Chris', 'David', 'Lucy', 'Ken', 'Paul', 'Rachel', 'CeCe', 'Jessica']:
        return 'purple'
    else:
        return 'red'

# Create a string for the episode name
def episode_string(episode_number, tribe):
    return 'episode' + str(episode_number) + '_' + tribe


# Create a string for the episode name with postive/negative relationships
def episode_string_pn(episode_number, tribe):
    return 'episode' + str(episode_number) + '_' + tribe + '_pn'

def episode_string_sw(episode_number, tribe):
    return 'episode' + str(episode_number) + '_' + tribe + '_sw'

# Create a string for the episode number
def episode_number_string(episode_number):
    if episode_number < 10:
        return str(episode_number)
    elif episode_number == 10:
        return '10_1'
    elif episode_number == 11:
        return '10_2'
    elif episode_number == 12:
        return '11'
    elif episode_number == 13:
        return '12_1'
    elif episode_number == 14:
        return '12_2'
    elif episode_number == 15:
        return '13_1'
    elif episode_number == 16:
        return '13_2'
    else:
        return '13_3'


# Convert the relationship strengths dictionary to a string for the graph template
def positive_negative_conversion(relationship_strengths):
    # save neutral relationships to pop after converting to positive/negative
    neutral_relationships = []

    for player in relationship_strengths:
        for other_player in relationship_strengths[player]:
            if relationship_strengths[player][other_player] < 0:
                relationship_strengths[player][other_player] = "-"
            elif relationship_strengths[player][other_player] > 1:
                relationship_strengths[player][other_player] = "+"
            else:
                # remove the relationship if it is not within threshold
                neutral_relationships.append((player, other_player))
    
    for player, other_player in neutral_relationships:
        relationship_strengths[player].pop(other_player)
    return relationship_strengths

# Convert the relationship strengths dictionary to a strong vs weak relationship dictionary
# Top 25% of relationships are strong, top 25-50% are weak
# Calculate based on the number of relationships, not the strength of the relationships
# Calculate based on episode, not the entire season
# take only the top 25% and 25-50% of positive relationships
def strong_weak_conversion(relationship_strengths):
    # save neutral relationships to pop after converting to positive/negative
    neutral_relationships = []

    episode_relationships = []
    for player in relationship_strengths:
        relationship_list = list(relationship_strengths[player].values())
        relationship_list.sort(reverse=True)
        episode_relationships += relationship_list

    episode_relationships.sort(reverse=True)
    # remove duplicates
    episode_relationships = list(dict.fromkeys(episode_relationships))

    print("Episode relationships: ")
    print(episode_relationships)
    episode_relationships = [x for x in episode_relationships if x > 0]
    print("Positive relationships: ")
    print(episode_relationships)
    weak_threshold = episode_relationships[int(len(episode_relationships) * 0.5)]
    strong_threshold = episode_relationships[int(len(episode_relationships) * 0.25)]
    print("Weak threshold: " + str(weak_threshold))
    print("Strong threshold: " + str(strong_threshold))

    for player in relationship_strengths:
        for other_player in relationship_strengths[player]:
            if relationship_strengths[player][other_player] >= strong_threshold:
                relationship_strengths[player][other_player] = "s"
            elif relationship_strengths[player][other_player] >= weak_threshold:
                relationship_strengths[player][other_player] = "w"
            else:
                # remove the relationship if it is not within threshold
                neutral_relationships.append((player, other_player))
    
    for player, other_player in neutral_relationships:
        relationship_strengths[player].pop(other_player)
    return relationship_strengths


# Convert the relationship strengths dictionary to a string for the graph template
# Example:     {'name': 'Paul', 'tribe': 'purple', 'relationships': []},
def toStringForGraphTemplate(relationship_strengths, episode_number, episode_tribes):
    string = ''
    
    for tribe in episode_tribes: # create dictionary for each tribe
        tribe_name = list(tribe.keys())[0]
        string += episode_string_sw(episode_number, tribe_name) + ' = [\n'

        for player in list(tribe.values())[0]:
            string += '\t{\'name\': \'' + player + '\', \'tribe\': \''+ tribe_color(player) +'\', \'relationships\': ['

            if player in relationship_strengths:
                check = 0
                for other_player in relationship_strengths[player]:
                    if other_player in list(tribe.values())[0]:
                        string += '{\'name\': \'' + other_player + '\', \'label\': \'' + str(relationship_strengths[player][other_player]) + '\'}, '
                        check += 1
                if check != 0:
                    string = string[:-2] + ']},\n'
                else:
                    string += ']},\n'
            
            else:
                string += ']},\n'
        
        string += ']\n\n'

    return string


# Print the directed relationship strengths for all episodes in formatted string for the graph template
def print_all_episode_graphs_dir(episodes):

    for i in range(len(episodes)):
        relationship_strengths_dir = calculate_relationship_strengths_directed(episodes[:i+1])
        relationship_strengths_dir_pn = positive_negative_conversion(relationship_strengths_dir)

        print("# *** Relationship Positive vs. Negative Directed ***")
        print('# First ' + str(i+1) + ' Episodes Positive vs. Negative (Directed):\n')
        # print(toStringForGraphTemplate(relationship_strengths_dir, episode_number_string(i+1), get_episode_players_list()[i]))
        print(toStringForGraphTemplate(relationship_strengths_dir_pn, episode_number_string(i+1), get_episode_players_list()[i]))
        print()


# Print the undirected relationship strengths for all episodes in formatted string for the graph template
def print_all_episode_graphs_undir(episodes):
    
    for i in range(len(episodes)):
        relationship_strengths_undir = calculate_relationship_strengths_undirected(episodes[:i+1])
        # relationship_strengths_undir_pn = positive_negative_conversion(relationship_strengths_undir)
        relationship_strengths_undir_sw = strong_weak_conversion(relationship_strengths_undir)
    
        print("# *** Relationship Strong vs. Weak Undirected ***")
        print('# First ' + str(i+1) + ' Episodes Strong vs. Weak (Undirected):\n')
        # print(toStringForGraphTemplate(relationship_strengths_undir, episode_number_string(i+1), get_episode_players_list()[i]))
        # print(toStringForGraphTemplate(relationship_strengths_undir_pn, episode_number_string(i+1), get_episode_players_list()[i]))
        print(toStringForGraphTemplate(relationship_strengths_undir_sw, episode_number_string(i+1), get_episode_players_list()[i]))
        print()


# Print the relationship strengths for all episodes
def print_all_episode_strengths(episodes):
    for i in range(len(episodes)):
        relationship_strengths_dir = calculate_relationship_strengths_directed(episodes[:i+1])
        relationship_strengths_undir = calculate_relationship_strengths_undirected(episodes[:i+1])

        print("# *** Relationship Strengths Directed ***")
        print('# First ' + str(i+1) + ' Episodes Strengths (Directed):\n')
        print(toString(relationship_strengths_dir))
        print()

        print("# *** Relationship Strengths Undirected ***")
        print('# First ' + str(i+1) + ' Episodes Strengths (Undirected):\n')
        print(toString(relationship_strengths_undir))
        print()


# Main function
def main():

    # Load the player interactions data from the csv file
    episodes_player_interactions_fullpath = r'C:\Users\Ethan\Documents\Educational\School Terms\Winter 2024\COMP 4602 A\Project\Millenials-vs-GenX_Project\excel_data\Survivor_Player_Interactions.csv'

    player_interactions = np.loadtxt(episodes_player_interactions_fullpath, delimiter=',', dtype=str, skiprows=1)

    episodes = split_rows_by_episode(player_interactions)

    sorted_episodes = sorted(episodes, key=lambda x: float(x[0][0]))

    # print_all_episode_graphs_undir(sorted_episodes)
    
    # print to a file
    f = open("relationship_strengths.txt", "w")
    f.write("##### RELATIONSHIP STRENGTHS #####\n")
    for i in range(len(sorted_episodes)):
        relationship_strengths_dir = calculate_relationship_strengths_directed(sorted_episodes[:i+1])
        relationship_strengths_undir = calculate_relationship_strengths_undirected(sorted_episodes[:i+1])

        f.write("# *** Relationship Strengths Directed ***\n")
        f.write('# First ' + str(i+1) + ' Episodes Strengths (Directed):\n')
        f.write(toString(relationship_strengths_dir) + '\n\n')

        f.write("# *** Relationship Strengths Undirected ***\n")
        f.write('# First ' + str(i+1) + ' Episodes Strengths (Undirected):\n')
        f.write(toString(relationship_strengths_undir) + '\n\n')
    
    f.close()

    print_all_episode_strengths(sorted_episodes)


if __name__ == '__main__':
    main()