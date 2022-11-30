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
def plot_spider(team, year) :
    rows_list = extract_csv_data(team)




# Test
team = "Atlanta Hawks"
year = "2017-18"
