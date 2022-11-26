from nba_api.stats.endpoints import playercareerstats


def save_players_stats_to_csv(player_stats, player_name):
    player_stats.to_csv('players_stats/{}.csv'.format(player_name), index=False)


def scrap_all_players_data_to_csv(players):
    players = players.get_active_players()  # 582 players in total

    '''for player in players:
        player_id = player['id']
        player_name = player['full_name']

        try:
            player_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
            player_stats = player_stats.get_data_frames()[0]
        except:
            print('Error with player: ', player_name)
            continue

        print('Player: ', player_name)
        players_stats[player_name] = player_stats'''

    for i in range(0, 5):
        player_id = players[i]['id']
        player_name = players[i]['full_name']

        try:
            player_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
            player_stats = player_stats.get_data_frames()[0]

            player_stats['PLAYER_NAME'] = player_name

            # remove the column where the SEASON_ID is different from 2022-23
            # player_stats = player_stats[player_stats['SEASON_ID'] == '2022-23']

            save_players_stats_to_csv(player_stats, player_name)
        except:
            print('Error with player: ', player_name)
            continue

    print('Scraping and saving of players finished')
