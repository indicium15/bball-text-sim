import json
from rich.console import Console
from rich.table import Column, Table
player_id = ""
PlayersList = []
class Player:
    def __init__(self,player_id, team_id, player_name, player_height, player_strength, player_speed,
    player_jumping,player_endurance, player_2pt, player_3pt): #Simple way to define a player
        self.player_name = player_name
        self.player_id = player_id
        self.team_id = team_id
        self.player_height = player_height
        self.player_strength = player_strength
        self.player_speed = player_speed
        self.player_jumping = player_jumping
        self.player_endurance = player_endurance
        self.player_2pt = player_2pt
        self.player_3pt = player_3pt
        
    #Using rich module to print out nice tables
    def PrintAttributes(self): 
        print("Player Overview for {}:".format(self.player_name))
        console = Console()
        
        table = Table(show_header=False)
        
        table.add_column("Attribute")
        table.add_column("Value")
        
        table.add_row("Height",str(self.player_height))
        table.add_row("Strength",str(self.player_strength))
        table.add_row("Speed",str(self.player_speed))
        table.add_row("Jumping",str(self.player_jumping))
        table.add_row("Endurace",str(self.player_endurance))
        table.add_row("Two-Point",str(self.player_2pt))
        table.add_row("Three-Point",str(self.player_3pt))
        
        console.print(table)
    
def ImportPlayersFromFile(file_name): #Function to import player attributes from a json file. Still having some problems with this
    global player_id
    with open(file_name) as json_file:
        data = json.load(json_file)
        for p in data['players']:
            player_reference = p['player_id']
            player_reference = Player(p['player_id'],p['team_id'],p['player_name'],p['player_height'],
            p['player_strength'],p['player_speed'],p['player_jumping'],p['player_endurance'],p['player_2pt'],p['player_3pt'])
            #print(type(player_reference))
            PlayersList.append(player_reference)
            print("Player {} has been added to the Global Player list with reference {}".format(p['player_name'],player_reference))
    
    for i in range(len(PlayersList)): #TODO:Automatically Assign Each Player in the list with a variable corresponding to their player id
        PlayersList[i] = "Player" + str(i)
        

if __name__ == "__main__":
    ImportPlayersFromFile('players.json')
    Player0.PrintAttributes()
    Player1.PrintAttributes()
    
   
    pass






       