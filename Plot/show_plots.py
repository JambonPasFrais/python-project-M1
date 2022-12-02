import os
import os.path as path
import player_plot
import matplotlib.pyplot as plt
import team_plot as tp

#get the list of all the files in the players_stats directory
players_list = os.listdir("../Scrapping/players_stats")
players_list.sort()
#Remove .csv extension and print the name of the player
for i in range(len(players_list)):
    players_list[i] = players_list[i].replace('.csv','')

#get all the wanted players for a specific season
required_players_list = []
team_dict = {
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers"
}
season = '2022-23'
for player in players_list:
    result = player_plot.check_players_team(player,team_dict, season)
    if result != None:
        required_players_list.append(result)

print("Generation of all the plots in progress... (it can take a while)")
for player_info in required_players_list:
    path_to_team_dir = "player_plot_images/"+player_info['team']
    path_to_player_dir = path_to_team_dir + "/"+player_info['name']
    if not path.exists(path_to_team_dir):
        os.mkdir(path_to_team_dir)
    if not path.exists(path_to_player_dir):
        os.mkdir(path_to_player_dir)
    player_plot.plot_all_data(player_info, season)
print("Generation done !")


# Get team plot's images
team1 = "Cleveland Cavaliers"
team2 = "Chicago Bulls"
tp.plot_evolution(team1)
tp.plot_evolution(team2)
tp.plot_histogram(team1)
tp.plot_histogram(team2)
tp.plot_correlation(team1)
tp.plot_correlation(team2)
