import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import csv

# Extraction of data in the csv fill to a list
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
        rank_list.append(int(rows_list[i][9]))

    # Plot evolution plot
    plt.figure()
    plt.plot(season_list, rank_list, "-", color="blue", marker='o')
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.title(team + "'s evolution rank")
    plt.savefig("team_plot_images/" + team + " evolution rank.png") # Save the image in png

# Create a spider plot
def plot_histogram(team) :
    rows_list = extract_csv_data(team)
    fg2_list = []
    fg3_list = []
    season_list = []

    # Get number of 2 & 3 points lend per year for last 10 years
    for i in range(len(rows_list)-10, len(rows_list)):
        fg2_list.append(int(rows_list[i][18]))
        fg3_list.append(int(rows_list[i][21]))
        season_list.append(rows_list[i][3])

    # Plot bar plot
    plt.figure()
    plt.barh(season_list, fg2_list)
    plt.grid(True)
    plt.title("Number of 2 points of " + team)
    plt.savefig("team_plot_images/" + team + " number of 2 points lends.png") # Save image in png

    plt.figure()
    plt.barh(season_list, fg3_list)
    plt.grid(True)
    plt.title("Number of 3 points of " + team)
    plt.savefig("team_plot_images/" + team + " number of 3 points lends.png")

# Create a correlation plot
def plot_correlation(team):
    df = pd.read_csv("../Scrapping/teams_stats/" + team + ".csv") # From csv to DataFrame

    # Remove useless columns
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

    # Plot the heat map
    sns.heatmap(df.corr())
    plt.savefig("team_plot_images/" + team + " correlation plot.png") # Save image in png

# Create a spider plot
def plot_spider(team):
    rows_list = extract_csv_data(team)
    data_list = []

    # Get defensives data for last 3 years
    for i in range(len(rows_list)-3, len(rows_list)):
        tmp_list = []
        tmp_list.append(int(rows_list[i][24]))
        tmp_list.append(int(rows_list[i][25]))
        tmp_list.append(int(rows_list[i][29]))
        tmp_list.append(int(rows_list[i][30]))
        tmp_list.append(int(rows_list[i][31]))
        data_list.append(tmp_list)
    D1 = data_list[0]
    D2 = data_list[1]
    D3 = data_list[2]

    # Plot spider plot
    categories = ['OREB', 'DREB', 'TOV', 'STL', 'BLK']
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar( # year - 2
        r = D1,
        theta = categories,
        name='Second to last years'
    ))
    fig.add_trace(go.Scatterpolar( # year - 1
        r = D2,
        theta = categories,
        name = 'Last year'
    ))
    fig.add_trace(go.Scatterpolar( # Current year
        r = D3,
        theta = categories,
        name = 'Current year'
    ))

    fig.update_layout( # Get the plot easier to read
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 3000]
            )),
        showlegend = True
    )
    fig.update_traces(fill = "toself")

    fig.write_image("team_plot_images/" + team + " defensive spider plot.png") # Savce image in png

# Test
test = 1
if test == 1 :
    team1 = "Cleveland Cavaliers"
    team2 = "Chicago Bulls"
    plot_evolution(team1)
    plot_evolution(team2)
    '''plot_histogram(team1)
    plot_histogram(team2)
    plot_correlation(team1)
    plot_correlation(team2)
    plot_spider(team1)
    plot_spider(team2)'''
