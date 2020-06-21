import json
from rich.console import Console
from rich.table import Column, Table
from player import Player

class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.roster = []
        self.starting_lineup = []
        self.bench = []
        self.team_wins = 0
        self.team_losses = 0
        self.team_record = str(self.team_wins),str(self.team_losses)
    
    def print_team_overview(self):
        console = Console()
        table = Table(show_header=False)
        table.add_column(header="Heading")
        table.add_column(header="Info")
        table.add_row("Name",self.team_name)
        table.add_row("Record","TO ADD") #TODO - Add team records
        console.print(table)
    
    def construct_lineup(self):
        #TODO:Create a starting lineup based on the players with the highest overall
        pass
    def print_roster(self, argument): #TODO: This function
        console = Console()
        table = Table(show_header="False")
        table.add_column("Player")
        table.add_column("Position")
        if argument == 0: #Print Full Roster:
            for i in self.roster:
                table.add_row(i.player_name,i.player_position)
        if argument == 1: #Print Starting Lineup:
            for i in range(1,5):
                table.add_row(self.roster[i].player_name,self.roster[i].player_position)
        if argument == 2: #Print Bench
            for i in range(6,len(self.roster)):
                table.add_row(self.roster[i].player_name,self.roster[i].player_position)
        console.print(table)

