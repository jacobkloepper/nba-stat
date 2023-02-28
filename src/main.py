# Generates a <date>.csv containing all team wins/losses today.

from nba_api.live.nba.endpoints import scoreboard
import sys

games = scoreboard.ScoreBoard()
g = games.get_dict()

org_stdout = sys.stdout

# Scoreboard
m = g.get('meta')
sb = g.get('scoreboard').get('games')


# Pathing things
dat_path = "dat/"
filename = g.get('scoreboard').get('gameDate')
filename = dat_path + filename + '.csv'


with open(filename, 'w') as f:
    sys.stdout = f

    for game in sb:
        # Extract some other info to tell if the game is over, escape
        game_state = game.get('gameStatus')
        if (game_state != 3):
            continue

        home_info = game.get('homeTeam')
        home_tricode = home_info.get('teamTricode')
        home_score = home_info.get('score')

        away_info = game.get('awayTeam')
        away_tricode = away_info.get('teamTricode')
        away_score = away_info.get('score')

        winstr = ""
        othstr = ""
        if (home_score > away_score):
            winstr = "W"
            othstr = "L"
        else:
            winstr = "L"
            othstr = "W"
        
        print(f"{away_tricode},{othstr},{home_tricode},{winstr}")

    sys.stdout = org_stdout
