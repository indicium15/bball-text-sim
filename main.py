import json
import itertools
from rich.console import Console
from rich.table import Column, Table
from player import Player
from operator import itemgetter
from team import Team
from game import Game
   
# def assign_player_variables():    
#     for i in range(len(players_dict)): #TODO:Is this really necessary?
#         Player0 = players_dict[0]
#         Player1 = players_dict[1]
#         Player2 = players_dict[2]
#         Player3 = players_dict[3]
#         Player4 = players_dict[4]

# def assign_team_variables(): #TODO:Is this really necessary?
#     for n, team in enumerate(teams_dict):
#         globals()["team%d"%n] = team  
#     pass

def import_players_from_json(file_name): #Function to import player attributes from a json file.
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data['players']:
            #player_reference = p['player_id']
            player_id = p['player_id']
            player_reference = Player(p['player_id'],p['team_id'],p['player_name'],p['player_position'],int(p['player_height']),
            int(p['player_strength']),int(p['player_speed']),int(p['player_jumping']),int(p['player_endurance']),int(p['player_2pt']),int(p['player_3pt']))
            players_dict[player_id] = player_reference
            print("Player Import Debugging: {} has been added to the Global Player list with reference {}".format(p['player_name'],player_reference))
    print("#" * 80)        

def import_teams_from_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data ['teams']:
            team_id = p['team_id']
            team_reference = Team(p['team_id'],p['team_name'])
            teams_dict[team_id] = team_reference
            print("Team Import Debugging: {} has been added to the Global Teams List with reference {}".format(p['team_name'],team_reference))
    print("#" * 80)

def generate_roster(): #Probably a more efficient way of doing this
    for y in players_dict.values():
        player_to_compare = y.team_id
        #print(f"Debugging: Player ID:{player_to_compare}")
        for x in teams_dict:
            #print(f"Debugging: Team ID: {x}")
            if player_to_compare == x:
                team_to_add = teams_dict.get(x)
                team_to_add.roster.append(y)
                print(f"Roster Debugging: Player {y.player_name} has been added to the roster of {teams_dict.get(x).team_name}")

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
    players_dict = {}
    teams_dict = {}
    import_players_from_json('players.json')  
    import_teams_from_json('teams.json')
    generate_roster()
    teams_dict[0].print_players(0)
    teams_dict[1].print_players(0)
    team0 = teams_dict[0]
    team0.print_team_overview()
    
    pass
