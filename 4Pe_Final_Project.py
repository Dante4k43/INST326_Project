#INST 326
#Group: 4Pe
#Members:
#Dante Caraballo, Bryant Pham, Farhaan Lalit, Jonathan Ricci, Justin Long
#Clone Repository:
#HTTPS: https://github.com/Dante4k43/INST326_Project.git
#SSH: git@github.com:Dante4k43/INST326_Project.git
#GitHub CLI: gh repo clone Dante4k43/INST326_Project
#

import re
import pandas as pd
import sys

class Analysis: #parent class
    """Produces analysis on NBA player statisitic 
    
        Attributes: 
            points (str): point by team/player
            assists (str): assists by team/player
            percentage (str): percnetage by team/player
            rebounds (str): rebounds by team/player
            steals (str): steals point by team/player
    """
    def __init__(self, filepath):
        """Initializes file path for data
        
            Args:
            filepath(str): filepath containing NBA Statistics 
                            (teams and players) a csv file 
        
        """ 
        self.df = pd.read_csv(filepath, sep=",", comment="#")
        team_regex = r"(?i)\b(team)\b" 
        player_regex = r"(?i)\b(player)\b"
        team_sort_class = re.search(team_regex, filepath)    
        player_sort_class = re.search(player_regex, filepath)
        
        if team_sort_class is not None:
            return Team_stats(self.df)
        elif player_sort_class is not None:
            return Player_stats(self.df)
        else:
            raise ValueError('The file name is not named correctly, '
                             'please include the word team or player '
                             'for the correct analysis')
    
    def stats(self, name1=False):
        """Displays statisitc regarding teams or players from file in init 
            method, option to view specific team or player available
            
            Args:
            name1(str): name of player or team's stats user wants to view 
        """
        print(self.df.loc[self.df["FULL NAME"] == name1]) if name1 is not False else print(self.df)
        
    def comparison(self, name1, name2):
        """Compares two items by stats from stats method (full stats)

        Args:
            name2 (str): name of team or player someone want to compare first name to
            
        Return:
        compared_stat (str): show the statistics of two items compared
        best(str): shows whos better out of the two items #counter
        """
        r1 = self.df.loc[self.df["FULL NAME"] == name1, "Rank"]
        r2 = self.df.loc[self.df["FULL NAME"] == name2, "Rank"]
        
        if r1 < r2:
            best = f"{name1} is ranked higher than {name2}"
        elif r1 > r2:
            best = f"{name2} is ranked higher than {name1}"
        else:
            best = "Both are equal."
        print(best)
  
  
  
    
class Team_stats(Analysis):
    """Compares team statisitics in the NBA
    
    Attributes: 
            points (str): point by team/player
            assists (str): assists by team/player
            percentage (str): percnetage by team/player
            rebounds (str): rebounds by team/player
            steals (str): steals point by team/player
    """
    
    
    def best_offense(self):
        """Finds the best offensive team
        
        returns
        best_o: returns result of best offensive  #
        """
        pass
        
    def best_defense(self):
        """Finds the best defensive team
        
        returns
        best_d: returns result of best defensive team
        """
        pass
        
    def best_team(self): #by division
        """Finds the best team overall
        
        returns
        best_overall: returns result of best team overall (both offense and defense)
        """
        pass
        
    def worst_team(self):#by division
        """Finds the worst team overall
        
        returns
        worst_overall: returns result of worst team overall (both offense and defense)
        """
        pass
        
        
     
    
class Player_stats(Analysis):
    """Compares player statisitics in the NBA

    Attributes: 
            points (str): point by team/player
            assists (str): assists by team/player
            percentage (str): percnetage by team/player
            rebounds (str): rebounds by team/player
            steals (str): steals point by team/player
    """
        
    def top_players(self):
        """Determines tops players based on attributes from analysis class
        
        Return:
        t_player: best players 
        """
        pass
    
    def bottom_players(self):
        """Determines bottom players based on attributes from analysis class
        
        Return:
        b_player: worst players 
        """
        pass
    
    def mvp_predict(self):
        """Determines MVP prediction based on top_player
        
        Return: 
        mvp_predict: mvp prediction #counter for better stats
        """
        pass
    
#def main() needed?

if __name__ == "__main__": 
    pass