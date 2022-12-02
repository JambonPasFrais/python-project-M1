from nba_api.stats.endpoints import playercareerstats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import csv

def extract_csv_data(team):
    with open("../Scrapping/teams_stats/" + team + ".csv", mode="r") as infile:
        reader = csv.reader(infile)
        rows_list = []
        for rows in reader:
            rows_list.append(rows)
        return rows_list

# Evolution of the rank of a team in the NBA league
def plot_evolution(team):
    rows_list = extract_csv_data(team)
    season_list = []
    rank_list = []
    # Get the rank of the 10 last years
    for i in range(len(season_list)-10, len(season_list)):
        season_list.append(rows_list[i][3])
        rank_list.append(rows_list[i][9])

    plt.figure()
    plt.plot(season_list, rank_list, "-", color="blue", marker='o')
    plt.grid(True)
    plt.title(team + "'s evolution rank")
    plt.savefig("team_plot_images/" + team + " evolution rank.png")

# Create a spider plot
def plot_histogram(team) :
    rows_list = extract_csv_data(team)
    fg2_list = []
    fg3_list = []
    season_list = []
    for i in range(len(rows_list)-10, len(rows_list)):
        fg2_list.append(rows_list[i][18])
        fg3_list.append(rows_list[i][21])
        season_list.append(rows_list[i][3])

    fg2_dict = {}
    fg3_dict = {}
    for i in range(len(season_list)):
        fg2_dict[season_list[i]] = fg2_list[i]
    fg2_dict = dict(sorted(fg2_dict.items(), key=lambda item: int(item[1])))
    for i in range(len(season_list)):
        fg3_dict[season_list[i]] = fg3_list[i]
    fg3_dict = dict(sorted(fg3_dict.items(), key=lambda item: int(item[1])))

    plt.figure()
    plt.bar(list(fg2_dict.values()), list(fg2_dict.keys()))
    plt.grid(True)
    plt.title("Number of 2 points of " + team)
    plt.savefig("team_plot_images/fg2 " + team + ".png")

    plt.figure()
    plt.bar(list(fg3_dict.values()), list(fg3_dict.keys()))
    plt.grid(True)
    plt.title("Number of 3 points of " + team)
    plt.savefig("team_plot_images/fg3 " + team + ".png")

# Create a correlation plot
def plot_correlation(team):
    df = pd.read_csv("../Scrapping/teams_stats/" + team + ".csv")
    df = df.drop('TEAM_ID', axis=1)
    df = df.drop('TEAM_NAME', axis=1)
    df = df.drop('TEAM_CITY', axis=1)
    df = df.drop('YEAR', axis=1)
    df = df.drop('GP', axis=1)
    df = df.drop('DIV_RANK', axis=1)
    df = df.drop('DIV_COUNT', axis=1)
    df = df.drop('PO_WINS', axis=1)
    df = df.drop('PO_LOSSES', axis=1)
    df = df.drop('PTS_RANK', axis=1)
    df = df.drop('NBA_FINALS_APPEARANCE', axis=1)
    df = df.drop('CONF_RANK', axis=1)
    df = df.drop('CONF_COUNT', axis=1)
    df = df.drop('WINS', axis=1)
    df = df.drop('LOSSES', axis=1)
    df = df.drop('WIN_PCT', axis=1)
    df = df.drop('OREB', axis=1)
    df = df.drop('DREB', axis=1)
    df = df.drop('REB', axis=1)
    df = df.drop('STL', axis=1)
    df = df.drop('TOV', axis=1)
    df = df.drop('BLK', axis=1)
    sns.heatmap(df.corr())
    plt.savefig("team_plot_images/correlation " + team + ".png")



# Test
team1 = "Cleveland Cavaliers"
team2 = "Chicago Bulls"
#plot_evolution(team1)
#plot_evolution(team2)
#plot_histogram(team1)
#plot_histogram(team2)
plot_correlation(team1)
plot_correlation(team2)
