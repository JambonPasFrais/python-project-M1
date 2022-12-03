import time
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerdashboardbyyearoveryear
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv

#Allows to check if the player is in the required team
def check_players_team(player, team_dict, season):
    if hasPlayed(player):
        player_data = extract_csv_data(player)
        for abrev in list(team_dict.keys()):
            for rows in player_data[1:]:
                if rows[4] == abrev and rows[1] == season:
                    return {'name': player, 'team': abrev}
    return None

#Extracts data from a csv file and return the content as list
def extract_csv_data(player):
    with open("../Scrapping/players_stats/" + player + ".csv", mode="r") as infile:
        reader = csv.reader(infile)
        rows_list = []
        for rows in reader:
            rows_list.append(rows)
        return rows_list

#Return if the player has played this season
def hasPlayed(player):
    data_list = extract_csv_data(player)
    return  (len(data_list) - 1)

#Plots general data for the player for a specific season
def plot_data(player, team,season):
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
    #season = wait_choice(rows_list[1:],rows_list[0].index("SEASON_ID"), "personal data")*
    for list in rows_list[1:]:
        temp_dict = {}
        if list[1] == season:
            for key in data_dict:
                temp_dict[key] = list[data_dict[key]]
            player_data_list.append(temp_dict)
    # Plot
    plt.figure()
    plt.savefig('test.png')
    total = 0
    for x in player_data_list[0].values():
        total += int(x)
    plt.pie(player_data_list[0].values(), labels=player_data_list[0].keys(),
            autopct=lambda x: '{:.0f}'.format(total * x / 100))

    plt.title(player + "'s personal stats for the " + season + " season")
    plt.savefig("player_plot_images/"+team+"/"+player+"/general_data.png")
    plt.close()

#Plots player's rank evolution through the seasons he played
def player_rank_evo(player, team):
    rows_list = extract_csv_data(player)
    #get player's ranks
    rank_stats = playercareerstats.PlayerCareerStats(player_id=rows_list[1][0]).get_data_frames()[10]
    stats_dict = rank_stats[['SEASON_ID','RANK_PTS']].to_dict()
    age_list = []
    previous_season = ''
    for row in rows_list[1:]:
        if previous_season != row[rows_list[0].index('SEASON_ID')]:
            age_list.append(int(float(row[rows_list[0].index('PLAYER_AGE')])))
            previous_season = row[rows_list[0].index('SEASON_ID')]
    #Plot
    plt.figure()
    plt.plot(age_list, list(stats_dict['RANK_PTS'].values()), "-", color='black')
    for i in range(len(age_list)):
        plt.plot(age_list[i],list(stats_dict['RANK_PTS'].values())[i], "o", label=list(stats_dict['SEASON_ID'].values())[i])
    plt.gca().invert_yaxis()
    plt.gca().set_xticks(age_list)
    plt.gca().set_yticks(list(stats_dict['RANK_PTS'].values()))
    plt.grid(True)
    plt.title(player+"'s rank evolution")
    plt.legend()
    plt.xlabel("Age")
    plt.ylabel("Rank")
    plt.savefig("player_plot_images/"+team+"/"+player+"/rank_evo.png")
    plt.close()

#Plots a player's plus/minus evolution
def plus_minus(player, team):
    rows_list = extract_csv_data(player)
    player_id = rows_list[1][0]
    stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id).get_data_frames()[1]
    plus_minus_stats = stats[['GROUP_VALUE','PLUS_MINUS']].to_dict()
    mean = 0
    #Plot
    plt.figure()
    plt.plot(list(plus_minus_stats['GROUP_VALUE'].values()), list(plus_minus_stats['PLUS_MINUS'].values()), "-", color='black')
    for i in range(len(list(plus_minus_stats['GROUP_VALUE'].values()))):
        plt.plot(list(plus_minus_stats['GROUP_VALUE'].values())[i],list(plus_minus_stats['PLUS_MINUS'].values())[i], "o")
        mean+=list(plus_minus_stats['PLUS_MINUS'].values())[i]
    mean/=len(list(plus_minus_stats['PLUS_MINUS'].values()))
    plt.gca().invert_xaxis()
    plt.gca().set_yticks(list(plus_minus_stats['PLUS_MINUS'].values()))
    plt.title(player + "'s +/- evolution\nmean="+str(mean))
    plt.grid()
    plt.xlabel("Season")
    plt.savefig("player_plot_images/"+team+"/"+player+"/plus_minus.png")
    plt.close()

#Shows the winrate of a player per season
def win_lose(player, team):
    rows_list = extract_csv_data(player)
    player_id = rows_list[1][0]
    stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id).get_data_frames()[1]
    #Wanted data are stored in a dict
    data = stats[['GROUP_VALUE','W','L']].to_dict()
    rows_count = len(data['GROUP_VALUE'])
    mean_list = []
    #Calculation of the win rate per season. Stores the results in a list
    for i in range(rows_count):
        temp_mean = 0
        temp_total = 0
        for key in data:
            if key != "GROUP_VALUE" and key == "W":
                temp_mean += data[key][i]
                temp_total += data[key][i]
            elif key != "GROUP_VALUE":
                temp_total += data[key][i]
        temp_mean = temp_mean / temp_total * 100
        mean_list.append(round(temp_mean, ndigits=2))
    #Plotting evolution
    plt.figure()
    plt.barh(list(data['GROUP_VALUE'].values()), mean_list)
    #Adding the text at the end of each bar
    for i,v in enumerate(mean_list):
        plt.text(v + .8, i - .1, str(v)+"%", color="black", fontweight="bold")
    plt.title(player+"'s win rate per season")
    plt.savefig("player_plot_images/"+team+"/"+player+"/win_lose.png")
    plt.close()

#Plots a spider chart which contains home games stats and roads games stats
def data_spider(player, team, season):
    rows_list = extract_csv_data(player)
    player_id = rows_list[1][0]
    home_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id, location_nullable='Home').get_data_frames()[1]
    away_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id, location_nullable='Road').get_data_frames()[1]
    #Sorting wanted data in dictionnaries
    home_stats = home_stats[['GROUP_VALUE', 'TEAM_ABBREVIATION', 'OREB', 'DREB', 'FTM', 'FTA', 'PF', 'FGM', 'FGA']].to_dict()
    away_stats = away_stats[['GROUP_VALUE', 'TEAM_ABBREVIATION', 'OREB', 'DREB', 'FTM', 'FTA', 'PF', 'FGM', 'FGA']].to_dict()
    for key in home_stats:
        home_stats[key] = list(home_stats[key].values())
    for key in away_stats:
        away_stats[key] = list(away_stats[key].values())
    home_wanted_stats = {}
    away_wanted_stats = {}
    #Getting home stats for a player, in a certain team and for a certain season
    for i in range(len(home_stats['TEAM_ABBREVIATION'])):
        if home_stats['TEAM_ABBREVIATION'][i] == team and home_stats['GROUP_VALUE'][i] == season:
            for key in home_stats:
                home_wanted_stats[key] = home_stats[key][i]
    #Getting away stats for a player, in a certain team and for a certain season
    for i in range(len(away_stats['TEAM_ABBREVIATION'])):
        if away_stats['TEAM_ABBREVIATION'][i] == team and away_stats['GROUP_VALUE'][i] == season:
            for key in away_stats:
                away_wanted_stats[key] = away_stats[key][i]
    #Getting the max value of the two stats list to make the range of the spider chart
    max = 0
    for val in list(home_wanted_stats.values())[2:]:
        if val > max:
            max = val
    for val in list(away_wanted_stats.values())[2:]:
        if val > max:
            max = val
    #Plot of the spider chart
    categories = list(home_wanted_stats.keys())[2:]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=list(home_wanted_stats.values())[2:], theta=categories,fill='toself',name='Home stats'))
    fig.add_trace(go.Scatterpolar(r=list(away_wanted_stats.values())[2:], theta=categories, fill='toself', name='Away stats'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, max+5])),showlegend=True,title_text=player+"'s home and away stats for the "+season+" season", title_x=0.5)
    fig.write_image('player_plot_images/'+team+'/'+player+'/home_away.png')

#Allows to plot all the data at one. Avoid calling to many differents functions in another file
def plot_all_data(player,season):
    #Waiting 0.3 second to start scrapping yo avoid a Timed Out error
    time.sleep(.3)
    try:
        plot_data(player['name'], player['team'], season)
        player_rank_evo(player['name'], player['team'])
        plus_minus(player['name'], player['team'])
        win_lose(player['name'], player['team'])
        data_spider(player['name'], player['team'], season)
        print("Genration done for "+player['name'])
    except Exception as e:
        print("An error as occured for "+player['name']+": " + str(e))
    #Making sure that all the plots generated are closed in order to free some space and improve performances
    plt.close('all')