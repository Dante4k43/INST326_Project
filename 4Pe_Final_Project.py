#INST 326
#Group: 4Pe
#Members:
#Dante Caraballo, Bryant Pham, Farhaan Lalit, Jonathan Ricci, Justin Long
#Clone Repository:
#HTTPS: https://github.com/Dante4k43/INST326_Project.git
#SSH: git@github.com:Dante4k43/INST326_Project.git
#GitHub CLI: gh repo clone Dante4k43/INST326_Project
#



class Analysis: #parent class
    """Produces analysis on NBA player statisitic 
    
        Attributes: 
            points (str): point by team/player
            assists (str): assists by team/player
            percentage (str): percnetage by team/player
            rebounds (str): rebounds by team/player
            steals (str): steals point by team/player
    """
    def __init__(self, filepath, name1):
        """Initializes file path for data (Possible using webscraping)
        
            Args::
            filepath(str): filepath containing NBA Statistics 
                            (teams and players) *most likely a cvs file 
        
        """
        
    def stats(self):#points, assists, and percentage (used for players and teams)
        """Displays statisitc regarding teams or players 
        
            Side effect: 
            self.points: attribute of self would change 
            self.assists: attribute of self would change
            self.percentage: attribute of self would change
            self.rebounds: attribute of self would change
            self.steals: attribute of self would change 
            
            
            Returns:
            total_stat(str): displays statistics from everyone,
                             (dictonary of tuples populated by str)
        """
        pass
    
    
    def comparison(self, name2):
        """Compares two items by stats

        Args:
            name2 (str): name of team or player someone want to compare first name to
            
        Return:
        compared_stat (str): show the statistics of two items compared
        best(str): shows whos better out of the two items #counter
        """
        pass
  
  
  
    
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