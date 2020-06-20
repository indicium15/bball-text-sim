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
    
    def PrintTeamOverview(self):
        console = Console()
        table = Table(show_header=False)
        table.add_column(header="Heading")
        table.add_column(header="Info")
        table.add_row("Name",self.team_name)
        table.add_row("Record","TO ADD") #TODO - Add team records
        console.print(table)
    
    def PrintRoster(self, argument): #TODO: This function
        if argument == 0: #Print Entire Roster
            for i in self.roster:
                print (i.player_name)
        elif argument == 1: #Print Starting Lineup
            pass
        elif argument == 2: #Print Bench
            pass

if __name__ == "__main__":
    pass
    