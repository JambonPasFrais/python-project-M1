from nba_api.stats.static import players
import player_scrapping

if __name__ == '__main__':

    # players scrapping part
    players_stats = player_scrapping.get_players_stats(players)
    player_scrapping.save_players_stats_to_csv(players_stats)

    # team scrapping part


    # live game scrapping part
