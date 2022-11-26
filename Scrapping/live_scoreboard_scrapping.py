from nba_api.live.nba.endpoints import scoreboard


def scrap_live_scoreboard_data_to_dict():
    scoreboard_data = scoreboard.ScoreBoard().get_dict()
    print(scoreboard_data)
