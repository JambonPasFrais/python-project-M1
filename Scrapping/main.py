from nba_api.stats.static import players
from nba_api.stats.static import teams
import player_scrapping
import team_scrapping

if __name__ == '__main__':

    # players scrapping part
    player_scrapping.scrap_players_data_and_save_to_csv(players)

    # team scrapping part
    team_scrapping.scrap_teams_data_and_save_to_csv(teams)

    # live game scrapping part
