import pandas as pd
from statistics import mean
import random


def display_teamList(l_team):
    for play in l_team:
        print(play)
    print('')
    
def display_team(ddd):
    for play in ddd.items():
        print('   ', play)
    print('')

def fDict_addListToDictValues(d_players, l_random):
    d_players_Random = d_players.copy()
    l_players_level = list(d_players.values())
    l_players_name = list(d_players.keys())
    
    for i in range(len(d_players)):
        str_player = l_players_name[i]
        int_level = l_players_level[i]
        int_randomNum = l_random[i]
        int_levelRandom = round(int_level + int_randomNum, 1)
        # Change the value of Player by giving some randomness
        d_players_Random[str_player] = abs(int_levelRandom)
    return d_players_Random


def f_BuildTeams(d_players, bl_print = False):
    # PARAM
    l_teamWhite = []
    l_teamColor = []
    int_WhiteScore = 0
    int_ColorScore = 0
    
    # First Player in Color team
    l_teamColor.append('Randolf')
    int_ColorScore += d_players['Randolf']
    del d_players['Randolf']
    
    # # Second Player in White team
    # l_teamWhite.append('_Roland')
    # int_WhiteScore += d_players['_Roland']
    # del d_players['_Roland']
    
    
    # Fill the team in a loop
    for i_numPlayer in range(1, len(d_players) + 1):
        int_nbPlayer = len(d_players)
        l_randomlist = random.sample(range(0, int_nbPlayer), int_nbPlayer)
        
        if bl_print:    print('Player in teams: ', i_numPlayer, '   Remaining player: ', int_nbPlayer)
        
        # If White Team (odd number)
        if int_nbPlayer % 2 != 0:
            if bl_print:    print(' White team...')
            int_gapToFillForWhite = int_ColorScore - int_WhiteScore
            if bl_print:    print('   Gap to fill...', int_gapToFillForWhite)
            d_players_level = {play : abs(rate - int_gapToFillForWhite) for (play, rate) in d_players.items()}
            if bl_print:    display_team(d_players_level)
            d_players_level = {play : abs(rate - int_gapToFillForWhite) * i_numPlayer for (play, rate) in d_players.items()}
            if bl_print:    display_team(d_players_level)
            # str_player = min(d_players_level, key = d_players_level.get)
            # print('   ', str_player)
            
            ## Add some randomness
            d_playersLevel_Random = fDict_addListToDictValues(d_players_level, l_randomlist)
            if bl_print:    print('   ', l_randomlist)
            if bl_print:    display_team(d_playersLevel_Random)
            # Get the right player
            str_player = min(d_playersLevel_Random, key = d_playersLevel_Random.get)
            if bl_print:    print('   White Player chosen: ', str_player, '\n')
            # Add the player to white team
            l_teamWhite.append(str_player)
            int_WhiteScore += d_players[str_player]
            del d_players[str_player]
        
        # If color Team (even number)
        else:
            if bl_print:    print(' color team...')
            int_whiteAdvantage = int_WhiteScore - int_ColorScore
            if bl_print:    print('   White advantage...', int_whiteAdvantage)
            flt_avgLevelPlayers = round(max(d_players.values()), 1)
            if bl_print:    print('   Average level or remaining player...', flt_avgLevelPlayers)
            flt_levelWanted = round(flt_avgLevelPlayers + int_whiteAdvantage, 2)
            if bl_print:    print('   Level wanted for a new player...', flt_levelWanted)
            d_players_level = {play : round(abs(rate - flt_levelWanted), 1)  for (play, rate) in d_players.items()} 
            if bl_print:    display_team(d_players_level)
            d_players_level = {play : round(abs(rate - flt_levelWanted) * i_numPlayer, 1)  for (play, rate) in d_players.items()} 
            if bl_print:    display_team(d_players_level)
            # str_player = min(d_players_level, key = d_players_level.get)
            # print('   ', str_player)
            
            ## Add some randomness
            d_playersLevel_Random = fDict_addListToDictValues(d_players_level, l_randomlist)
            if bl_print:    print('   ', l_randomlist)
            if bl_print:    display_team(d_playersLevel_Random)
            # Get the right player
            str_player = min(d_playersLevel_Random, key = d_playersLevel_Random.get)
            if bl_print:    print('   Color Player chosen: ', str_player, '\n')
            # Add the player to white team
            l_teamColor.append(str_player)
            int_ColorScore += d_players[str_player]
            del d_players[str_player]

    return l_teamWhite, int_WhiteScore, l_teamColor, int_ColorScore


#=============================================================================

# Get the PLayers
df_players = pd.read_excel(r'..\..\0_CompanyCopy\IHSMarkit\SCAA Tuesdays Football.xlsx', 
                           sheet_name = 'Team', header = 0, index_col = None)
d_players = {}
for index, row in df_players.iterrows():
    d_players[row['Player']] = row['Rate']
display_team(d_players)


# Make the team
l_teamWhite, int_WhiteScore, l_teamColor, int_ColorScore = f_BuildTeams(d_players, bl_print = False)

print(' Color team: ')
display_teamList(l_teamColor)
print(' White team:')
display_teamList(l_teamWhite)
print('  * Color score:', int_ColorScore, '\n')
print('  * White score:', int_WhiteScore, '\n')








