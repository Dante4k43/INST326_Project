#INST 326
#Group: 4Pe
#Members:
#Dante Caraballo, Bryant Pham, Farhaan Lalit, Jonathan Ricci, Justin Long
#Clone Repository:
#HTTPS: https://github.com/Dante4k43/INST326_Project.git
#SSH: git@github.com:Dante4k43/INST326_Project.git
#GitHub CLI: gh repo clone Dante4k43/INST326_Project
#

from argparse import ArgumentParser
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
        """Initializes file path for data (Possible using webscraping)
        
            Args:
            filepath(str): filepath containing NBA Statistics 
                            (teams and players) *most likely a cvs file 
        
        """
        self.df = pd.read_csv(filepath, sep=",", comment="#")
            
        team_regex = r"""(?i)(team)""" 
        player_regex = r"""(?i)(player)"""
        team_sort_class = re.search(team_regex, filepath)    
        player_sort_class = re.search(player_regex, filepath)
        
        if team_sort_class is not None:
            return Team_stats(self)
        elif player_sort_class is not None:
            return Player_stats(self)
        else:
            raise ValueError('The file name is not named correctly, '
                             'please include the word team or player '
                             'for the correct analysis')
        
    def stats(self, name1 = False):
        """Displays statisitc regarding teams or players from file in init 
            method, option to view specific team or player available
            
            Args:
            name1(str): name of player or team's stats user wants to view 
        """
        self.df = pd.read_csv("player_stats.csv", sep=",", comment="#")
        [print(self.df.loc[self.df["NAME"] == name1]) if 
         name1 is not False else print(self.df)]
        
    def comparison(self, name1, name2):
        """Compares two items by stats from stats method (full stats)

        Args:
            name1 (str): name of the first team or player to be compared
            name2 (str): name of the second team or player to be compared
            
        Return:
            str: shows which of the two items is better
        """
        self.df = pd.read_csv("player_stats.csv", sep=",", comment="#")
        
        self.df = self.df.reset_index(drop=True)
        
        row_number1 = self.df[self.df["NAME"] == name1].index
        row_number2 = self.df[self.df["NAME"] == name2].index
        
        r1 = str(self.df.loc[row_number1]["RANK"])
        r2 = str(self.df.loc[row_number2]["RANK"])
                
        if r1 < r2:
            best = f"{name1} is ranked higher than {name2}"
        elif r1 > r2:
            best = f"{name2} is ranked higher than {name1}"
        else:
            best = "Both are equal."
        return best
  
    
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
        """Display the top 5 offensive teams and the best offensive team.
        
        Side Effects:
            Creates a new Dataframe called dfo that has top 5 offensive teams.
        """
        self.df = pd.read_csv("team_stats.csv", sep=",", comment="#")
        dfo = self.df.groupby("NAME")[['FG%','FT%','ORB','AST','RANK']].max().reset_index().sort_values(["FG%"], ascending = False)
        best_o = dfo.iloc[0]
        print (f"This is the highest rated offensive team based on the stats displayed! \n\n{best_o.to_string(index =True)}\n")
        print(f"These are the top 5 best offensive teams! \n\n{dfo.head().to_string(index = False)} \n\n")
    

        
    def best_defense(self):
        """Displays the top 5 defensive teams and the best defensive team.
        
        Side Effects:
            Creates a new Dataframe called dfd that has top 5 defensive teams.
        """
        self.df = pd.read_csv("team_stats.csv", sep=",", comment="#")
        dfd = self.df.groupby("NAME")[['DRB','STL','BLK','RANK']].max().reset_index().sort_values(["DRB"], ascending = False)
        best_d = dfd.iloc[0]
        print (f"This is the highest rated defensive team based on the stats displayed! \n\n{best_d.to_string(index =True)}\n")
        print(f"These are the top 5 best defensive teams! \n\n{dfd.head().to_string(index = False)} \n\n")
        
    def best_team(self): #by division 
        """Finds the top 5 teams
        
        Side Effect:
            new data frame created called best, contains the top 5 teams of the csv.
        """
        df = pd.read_csv("team_stats.csv")
        for col in df:
            if "PTS" not in df:
                print("Need a PTS Column to read; Need 'NAME' and 'PTS' columns")
                pass
            elif "NAME" not in df:
                print("Need a NAME Column to read; Need 'NAME' and 'PTS' columns")
                pass
            else:
                best = df.groupby('NAME')['PTS'].max().reset_index().sort_values(['PTS'], ascending=False)[:5]      
                print(f"Top 5 best teams are:\n{best}\n")  
                break   
   
    def worst_team(self):#by division
        """Finds the bottom 5 teams
        
        Side Effect:
            new data frame created called worst, contains the bottom 5 teams of the csv.
        """
        df = pd.read_csv("team_stats.csv")
        worst = df.groupby('NAME')['PTS'].max().reset_index().sort_values(['PTS'])[:5]
        point = 'PTS'
        print(f"Top 5 best worst are:\n{worst}\n") if point in df else print("Need PTS")
        
        
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
        t_player (list): best players 
        """

        self.df = pd.read_csv("player_stats.csv", sep = ",", comment = "#")
        
        df_best = self.df[["NAME", "PPG", "APG", "RPG"]]
        
        self.best_points = []
        
        for row in df_best.rows: 
            name = df_best.loc[row, "NAME"]
            ppg = df_best.loc[row, "PPG"]
            apg = df_best.loc[row, "APG"]
            rpg = df_best.loc[row, "RPG"]
            total_points = (ppg + apg + rpg) / 3 
            self.best_points.append((name, total_points)) 
            
        self.best_sorted = sorted(self.best_points, key = lambda x: x[1],\
                                    reverse = True)[:5]
        
        print(f"These are the best players in the league.\n")
    
    def bottom_players(self):
        """Determines bottom players based on attributes from analysis class
        
        Return:
        b_player (list): worst players 
        """
                
        self.df = pd.read_csv("player_stats.csv", sep = ",", comment  ="#")
        
        df_best = self.df[["NAME", "PPG", "APG", "RPG"]]
        
        self.best_points = []
        
        for row in df_best.rows: 
            name = df_best.loc[row, "NAME"]
            ppg = df_best.loc[row, "PPG"]
            apg = df_best.loc[row, "APG"]
            rpg = df_best.loc[row, "RPG"]
            total_points = (ppg + apg + rpg) / 3 
            self.best_points.append((name, total_points)) 
            
        self.best_sorted = sorted(self.best_points, key = lambda x: x[1],\
                                    reverse = False)[:5]
        
        print(f"These are the worst players in the league.\n")
        
    def __str__(self): 
        """prints out the top or bottom 5 names of players from best_points

        Returns:
        str: the names of top or bottom 5 players 
        """
        return f"{self.best_sorted}"
    print(__str__())
    
    def mvp_predict(self):
        """Determines MVP prediction based on each player's versatility index.
        
        Returns:
            str: the name of the player most likely to be named mvp.
        
        Side effects:
            Plots a barplot predicting the likelihood each player becoming an
            mvp based on their versatility.
            Prints out the name of the player most likely to be named mvp to
            stdout.
        """
        
        self.df = pd.read_csv("player_stats.csv", sep=",", comment="#")
        
        df_new = self.df[["NAME", "VI"]]
        df_new[df_new["VI"] > 12.5].plot.bar(x="NAME", y="VI")

        vi_max = df_new["VI"].max()
        mvp = str(df_new.loc[df_new["VI"] == vi_max]["NAME"])
        space1 = mvp.find(" ", 7)
        space2 = mvp.find("\n", space1)
        name = mvp[7: space2]
        
        return print(f"{name} is the most likely to be named most valuable "
                     "player.")
    
def parse_args(arglist):
    
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to stat csv file")
    parser.add_argument("name1", help="player names")
    parser.add_argument("name2", help="player names")

    return parser.parse_args(arglist)

def main(filepath, name1 = False, name2 = False):
    analyze = Analysis(filepath, name1, name2)
    print(analyze)


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.filepath, args.name1, args.name2)