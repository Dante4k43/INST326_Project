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

class Analysis: 
    """Produces analysis on NBA player statisitic. 
    
        Attributes: 
            df (str): dataframe from csv file.
            name1 (str): first name of team/player (optional).
            name2 (str): second name of team/player (optional).

    """
    def __init__(self, filepath, name1 = False, name2 = False):                     
        """Initializes file path for data.
        
            Args:
            filepath(str): filepath containing NBA Statistics 
                            (teams and players), must be a cvs file. 
            name1 (str): first name of team/player (optional but must be full).
            name2 (str): second name of team/player (optional but must be full).
        """
        with open(filepath, "r", encoding="utf-8") as file:
            df = pd.read_csv(file, sep=",")
            self.df = df
            self.name1= name1
            self.name2 = name2
            
        self.stats()
        self.comparison()
        
          
        
    def stats(self):
        """Displays statisitc regarding teams or players from file in init 
            method, option to view specific team or player available.
            
            Args:
            name1(str): name of player or team's stats user wants to view. 
        """
        if self.name1 is not False and self.name2 is False:
            print(self.df.loc[self.df.iloc[:,1] == self.name1]) 
        else:
            print(self.df)
        
    def comparison(self):
        """Compares two items by stats from stats method (full stats).

        Args:
            name1 (str): name of the first team or player to be compared.
            name2 (str): name of the second team or player to be compared.
            
        Return:
            str: shows which of the two items is better.
        """        
        compare = self.df
        
        #Boolean Indexing
       
        r1 = str(compare.loc[compare.iloc[:,1] == self.name1]) 
        r2 = str(compare.loc[compare.iloc[:,1] == self.name2])
        
        
        if self.name1 is not False and self.name2 is not False:        
            print(r1)
            print(r2) 
        else:
            pass
    
    
  
    
class Team_stats(Analysis):
    """Compares team statisitics in the NBA.
    
    Attributes: 
            df (str): dataframe from csv file.
    """
    
    
    def best_offense(self):
        """Display the top 5 offensive teams and the best offensive team.
        
        Side Effects:
            Creates a new Dataframe called dfo that has top 5 offensive teams.
        """
        dfo = (self.df.groupby("NAME")[['FG%','FT%','ORB','AST','RANK']]
               .max().reset_index().sort_values(["FG%"], ascending = False))
        best_o = dfo.iloc[0]
        print(f"This is the highest rated offensive team based on the stats "
              f"displayed! \n\n{best_o.to_string(index =True)}\n")
        #Keyword Argument (Line 116)
        print(f"These are the top 5 best offensive teams!"
              f"\n\n{dfo.head().to_string(index = False)} \n\n")
        
    

        
    def best_defense(self):
        """Displays the top 5 defensive teams and the best defensive team.
        
        Side Effects:
            Creates a new Dataframe called dfd that has top 5 defensive teams.
        """
        #Grouby Method (Line 129)
        dfd = (self.df.groupby("NAME")[['DRB','STL','BLK','RANK']] 
               .max().reset_index().sort_values(["DRB"], ascending = False))
        best_d = dfd.iloc[0]
        print(f"This is the highest rated defensive team based on the stats "
             f"displayed! \n\n{best_d.to_string(index =True)}\n")
        print(f"These are the top 5 best defensive teams!"
              f"\n\n{dfd.head().to_string(index = False)} \n\n")
        
    def best_team(self):  
        """Finds the top 5 teams.
        
        Side Effect:
            new data frame created called best, contains the top 5
            teams of the csv.
        """
        for col in self.df:
            if "PTS" not in self.df:
                print("Need a PTS Column to read; Need 'NAME'"
                      + "and 'PTS' columns")
            elif "NAME" not in self.df:
                print("Need a NAME Column to read; Need 'NAME'"
                      + "and 'PTS' columns")
            else:
                best = (self.df.groupby('NAME')['PTS'].max().reset_index()
                        .sort_values(['PTS'], ascending=False)[:5]) 
                #Fstring (Line 156)  
                print(f"Top 5 best teams are:\n{best}\n")  
                break   
   
    def worst_team(self):
        """Finds the bottom 5 teams.
        
        Side Effect:
            new data frame created called worst, contains the bottom 5 
            teams of the csv.
        """
        worst = (self.df.groupby('NAME')['PTS'].max().reset_index()
                 .sort_values(['PTS'])[:5])
        point = 'PTS'
        #Conditional Expression (Line 171-172)
        print((f"Top 5 best worst are:\n{worst}\n") if point in self.df
              else print("Need PTS"))
        
        
class Player_stats(Analysis):
    """Compares player statisitics in the NBA.

    Attributes: 
            df (str): dataframe from csv file.
    """
 
    def top_players(self):
        """Determines top players based on attributes from analysis class.
        
        Return:
        t_player (list): best players 
        """        
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
        """Determines bottom players based on attributes from analysis class.
        
        Return:
        b_player (list): worst players 
        """        
        df_best = self.df[["NAME", "PPG", "APG", "RPG"]]
        
        self.best_points = []
        
        for row in df_best.rows: 
            name = df_best.loc[row, "NAME"]
            ppg = df_best.loc[row, "PPG"]
            apg = df_best.loc[row, "APG"]
            rpg = df_best.loc[row, "RPG"]
            total_points = (ppg + apg + rpg) / 3 
            self.best_points.append((name, total_points)) 
        #Lambda Expression (Line 233)
        self.best_sorted = sorted(self.best_points, key = lambda x: x[1],\
                                    reverse = False)[:5]
        
        print(f"These are the worst players in the league.\n")
        
    def __str__(self): #Magic Method
        """Prints out the top or bottom 5 names of players from best_points.

        Returns:
        str: the names of top or bottom 5 players.
        """
        return f"{self.best_sorted}"
        
    
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
                
        df_new = self.df[["NAME", "VI"]]
        df_new[df_new["VI"] > 12.5].plot.bar(x="NAME", y="VI") #Pyplot

        vi_max = df_new["VI"].max()
        mvp = str(df_new.loc[df_new["VI"] == vi_max]["NAME"])
        space1 = mvp.find(" ", 7)
        space2 = mvp.find("\n", space1)
        name = mvp[7: space2]
        
        return print(f"{name} is the most likely to be named most valuable "
                     "player.")
    
def main(filepath, name1 = False, name2 = False):
    """Displays key statisitics of dataframe, player, or team.
    
        Args:
            filepath(str): filepath containing NBA Statistics 
                            (teams and players), must be a cvs file. 
            name1 (str): first name of team/player (optional).
            name2 (str): second name of team/player (optional).
    """
    team_regex = r"""(?i)team"""        #Regex section from here until line 182
    player_regex = r"""(?i)player"""
    team_sort_class = re.search(team_regex, filepath)                           
    player_sort_class = re.search(player_regex, filepath)       
    
    
    if team_sort_class is not None:
        return Team_stats(filepath, name1, name2)

    elif player_sort_class is not None:
        return Player_stats(filepath, name1, name2)
    else:                                                                           
        raise ValueError('The file name is not named correctly, '               
                             'please include the word team or player '
                             'for the correct analysis')
    
    
def parse_args(arglist): #Argument Parser Class
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments
        filepath (str): the filepath/file of a csv.
        
    This function also allows the following optional arguments:
        name1 (str): name of team/player to compare or look up stats.
        name2 (str): name of team/player compaing to name1.
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information).
    
    Raises:
        TypeError: encountered an invalid argument.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", type= str, help="path to stat csv file")        
    parser.add_argument("-name1",type= str, default= False, help="player names")
    parser.add_argument("-name2",type=str, default= False,help="player names")

    args = parser.parse_args(arglist)                                               
    return args


if __name__ == "__main__":                                                          
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.filepath, args.name1, args.name2)
