import json
import itertools
from rich.console import Console
from rich.table import Column, Table
from player import Player
from team import Team
   
# def assign_player_variables():    
#     for i in range(len(players_list)): #TODO:Is this really necessary?
#         Player0 = players_list[0]
#         Player1 = players_list[1]
#         Player2 = players_list[2]
#         Player3 = players_list[3]
#         Player4 = players_list[4]

# def assign_team_variables(): #TODO:Is this really necessary?
#     for n, team in enumerate(teams_list):
#         globals()["team%d"%n] = team  
#     pass

def import_players_from_json(file_name): #Function to import player attributes from a json file.
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data['players']:
            player_reference = p['player_id']
            player_reference = Player(p['player_id'],p['team_id'],p['player_name'],p['player_position'],p['player_height'],
            p['player_strength'],p['player_speed'],p['player_jumping'],p['player_endurance'],p['player_2pt'],p['player_3pt'])
            players_list.append(player_reference)
            #print("Player {} has been added to the Global Player list with reference {}".format(p['player_name'],player_reference))

def import_teams_from_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data ['teams']:
            team_reference = p['team_id']
            team_reference = Team(p['team_id'],p['team_name'])
            teams_list.append(team_reference)
            #print("Team {} has been added to the Global Teams List with reference {}".format(p['team_name'],team_reference))

def generate_roster(): 
    for x, y in [(x,y) for x in players_list for y in teams_list]:
        player_to_compare = x.team_id
        team_to_compare = y.team_id
        if player_to_compare == team_to_compare:
            roster_to_add = y.roster
            roster_to_add.append(x)
            #print("Debugging: {} has been added to the roster of {}".format(x.player_name, y.team_name)) 

def simulate_match(hometeam, awayteam):
    print("""
    Welcome!
    Our game tonight sees the {} matched up against the {}.
    Let's review the starting lineups for our two teams.
    """.format(hometeam.team_name,awayteam.team_name))
    print('#'*80)
    print("The Starting Lineup for the {}:".format(hometeam.team_name))
    hometeam.printlineup()
    print("The Starting Lineup for the {}:".format(awayteam.team_name))
    awayteam.printlineup()
    
if __name__ == "__main__":
    players_list = []
    teams_list = []
    import_players_from_json('players.json')  
    import_teams_from_json('teams.json')
    generate_roster()
    teams_list[0].print_roster(2)    
    pass
