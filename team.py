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
        self.team_record = str(self.team_wins) + ',' + str(self.team_losses)
    
    def print_team_overview(self):
        console = Console()
        table = Table(show_header=False)
        table.add_column(header="Heading")
        table.add_column(header="Info")
        table.add_row("Name",self.team_name)
        table.add_row("Record",self.team_record) #TODO - Add team records
        console.print(table)
    
    def construct_lineup(self):
        #TODO:Create a starting lineup based on the players with the highest overall
        for player in self.roster:
            pass
        pass
    def print_players(self, argument): #TODO: This function
        console = Console()
        table = Table(show_header="False")
        table.add_column("Player")
        table.add_column("Position")
        if argument == 0: #Print Full Roster:
            for i in self.roster:
                table.add_row(i.player_name,i.player_position)
        if argument == 1: #Print Starting Lineup:
            for i in self.starting_lineup:
                table.add_row(self.roster[i].player_name,self.roster[i].player_position)
        if argument == 2: #Print Bench
            for i in self.bench:
                table.add_row(self.roster[i].player_name,self.roster[i].player_position)
        console.print(table)

    def add_to_lineup(self, player):
        if player in self.team.roster() and len(self.team.starting_lineup) <= 4:
            self.team.starting_lineup.append(player)
            print(f"Lineup Debugging: {player.player_name} has been added to the starting lineup of {self.team_name} ")
            self.print_players(1) 
        
        elif len(self.starting_lineup) > 4:
            print("The starting lineup is full. Please remove a player first to continue")
            print("Current Starting Lineup:")
            self.print_players(1)   
    

