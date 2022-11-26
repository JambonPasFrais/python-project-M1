from nba_api.stats.endpoints import teamyearbyyearstats


def save_teams_stats_to_csv(team_stats, team_name):
    team_stats.to_csv('teams_stats/{}.csv'.format(team_name), index=False)
    print('Team: ', team_name, ' saved')


def scrap_teams_data_and_save_to_csv(teams):
    teams = teams.get_teams()  # 30 teams in total
    '''
    for team in teams:
        team_id = team['id']
        team_name = team['full_name']

        try:
            team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
            team_stats = team_stats.get_data_frames()[0]
            save_teams_stats_to_csv(team_stats, team_name)
            # team_stats = teams_stats[teams_stats['YEAR'] == '2022-23']
        except:
            print('Error with team: ', team_name)
            continue

        print('Team: ', team_name)
    '''

    for i in range(0, 5):
        team_id = teams[i]['id']
        team_name = teams[i]['full_name']

        try:
            team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
            team_stats = team_stats.get_data_frames()[0]
            save_teams_stats_to_csv(team_stats, team_name)
        except:
            print('Error with team: ', team_name)
            continue

    print('Scraping and saving of teams finished')
