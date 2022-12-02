from nba_api.stats.endpoints import playercareerstats
import matplotlib.pyplot as plt
import pandas as pd
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
    plt.title(team + "'s rank evolution")
    plt.show()

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
    plt.savefig("team_plot_images/fg2.png")
    plt.show()
    plt.figure()
    plt.bar(list(fg3_dict.values()), list(fg3_dict.keys()))
    plt.grid(True)
    plt.title("Number of 3 points of " + team)
    plt.savefig("team_plot_images/fg3.png")
    plt.show()





# Test
team = "Atlanta Hawks"
plot_histogram(team)
