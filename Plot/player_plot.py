from nba_api.stats.endpoints import playercareerstats
import matplotlib.pyplot as plt
import pandas as pd
import csv


def extract_csv_data(player):
    with open("../Scrapping/players_stats/" + player + ".csv", mode="r") as infile:
        reader = csv.reader(infile)
        rows_list = []
        for rows in reader:
            rows_list.append(rows)
        return rows_list

def wait_choice(choice_list,index,text):
    choice = 0
    print("Choose the season for the "+text)
    for i in range(len(choice_list)):
        print(str(i+1)+". "+choice_list[i][index])
    while choice < 1 or choice > len(choice_list):
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(choice_list):
                print("Invalid choice, try again")
                choice = 0
        except:
            print("Invalid input, try again")

    return choice_list[choice-1][index]

def plot_data(player):
    rows_list = extract_csv_data(player)
    data_dict = {
        "OREB": rows_list[0].index("OREB"),
        "DREB": rows_list[0].index("DREB"),
        "FTM": rows_list[0].index("FTM"),
        "FTA": rows_list[0].index("FTA"),
        "PF": rows_list[0].index("PF"),
        "FGM": rows_list[0].index("FGM"),
        "FGA": rows_list[0].index("FGA")
    }
    player_data_list = []
    season = wait_choice(rows_list[1:],rows_list[0].index("SEASON_ID"), "personal data")
    for list in rows_list[1:]:
        temp_dict = {}
        if list[1] == season:
            for key in data_dict:
                temp_dict[key] = list[data_dict[key]]
            player_data_list.append(temp_dict)
    # Plot
    plt.figure()
    total = 0
    for x in player_data_list[0].values():
        total += int(x)
    plt.pie(player_data_list[0].values(), labels=player_data_list[0].keys(),
            autopct=lambda x: '{:.0f}'.format(total * x / 100))

    plt.title(player + "'s personal stats for the " + season + " season")
    plt.show()

def player_rank_evo(player):
    rows_list = extract_csv_data(player)
    #get the age of the player for every seasons he played
    global_stats = playercareerstats.PlayerCareerStats(player_id=rows_list[1][0]).get_data_frames()[0]
    age_dict = global_stats[['PLAYER_AGE']].to_dict()
    #get player's ranks
    rank_stats = playercareerstats.PlayerCareerStats(player_id=rows_list[1][0]).get_data_frames()[10]
    stats_dict = rank_stats[['SEASON_ID','RANK_PTS','PLAYER_AGE']].to_dict()
    #Plot
    plt.figure()
    plt.plot(list(age_dict['PLAYER_AGE'].values()), list(stats_dict['RANK_PTS'].values()), "-", color='black')
    for i in range(len(list(age_dict['PLAYER_AGE'].values()))):
        plt.plot(list(age_dict['PLAYER_AGE'].values())[i],list(stats_dict['RANK_PTS'].values())[i], "o", label=list(stats_dict['SEASON_ID'].values())[i])
    plt.gca().invert_yaxis()
    plt.gca().set_xticks(list(age_dict['PLAYER_AGE'].values()))
    plt.gca().set_yticks(list(stats_dict['RANK_PTS'].values()))
    plt.grid(True)
    plt.title(player+"'s rank evolution")
    plt.legend()
    plt.show()