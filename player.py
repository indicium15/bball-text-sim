import json
from rich.console import Console
from rich.table import Column, Table

class Player:
    def __init__(self,player_id, team_id, player_name, player_position, player_height, player_strength, player_speed,
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
        self.player_position = player_position
        self.player_overall = 0
        
    #Using rich module to print out nice tables
    def calculate_overall(self): #Function to calculate the overall of a player based on their position
        pass
    
    def print_attributes(self): 
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
    

       