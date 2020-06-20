import json
from rich.console import Console
from rich.table import Column, Table
from player import Player
from team import Team

def ImportPlayersFromFile(file_name): #Function to import player attributes from a json file. Still having some problems with this
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data['players']:
            player_reference = p['player_id']
            player_reference = Player(p['player_id'],p['team_id'],p['player_name'],p['player_height'],
            p['player_strength'],p['player_speed'],p['player_jumping'],p['player_endurance'],p['player_2pt'],p['player_3pt'])
            PlayersList.append(player_reference)
            #print("Player {} has been added to the Global Player list with reference {}".format(p['player_name'],player_reference))
    
def AssignPlayerVars():    
    for i in range(len(PlayersList)): #TODO:Automatically assign player variable for list
        Player0 = PlayersList[0]
        Player1 = PlayersList[1]
        Player2 = PlayersList[2]
        Player3 = PlayersList[3]
        Player4 = PlayersList[4]

def ImportTeamsFromFile(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data ['teams']:
            team_reference = p['team_id']
            team_reference = Team(p['team_id'],p['team_name'])
            TeamsList.append(team_reference)
            #print("Team {} has been added to the Global Teams List with reference {}".format(p['team_name'],team_reference))

def CreateRoster(): #TODO: Function to create roster comparing the team_id values
    for i in PlayersList:
        if i.team_id == "0":
            roster = TeamsList[0].roster
            roster.append(i)
            #print("{} has been added to the roster of {}".format(i.player_name,TeamsList[0].team_name))

if __name__ == "__main__":
    PlayersList = []
    TeamsList = []
    ImportPlayersFromFile('players.json')  
    ImportTeamsFromFile('teams.json')
    CreateRoster()
    Team0 = TeamsList[0]
    Team0.PrintRoster(0)
    pass
