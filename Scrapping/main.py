from nba_api.stats.static import players
from nba_api.stats.static import teams
import player_scrapping
import team_scrapping
import live_scoreboard_scrapping

if __name__ == '__main__':

    while True:
        print("What do you want to scrap?")
        print("1. Players")
        print("2. Teams")
        print("3. Live Scoreboard")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            player_scrapping.scrap_all_players_data_to_csv(players)
        elif choice == '2':
            team_scrapping.scrap_all_teams_data_to_csv(teams)
        elif choice == '3':
            live_scoreboard_scrapping.scrap_live_scoreboard_data_to_dict()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

    print("Thank you for using this program!")
