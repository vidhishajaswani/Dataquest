## 2. Defining Custom Classes ##

print(header)

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It is automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = data_row[2]
        self.team = data_row[3]

# Initialize a player using the first row of our data set
first_player = Player(nba[0])

# Implement the Team class

class Team():
    def __init__(self,name):
        self.team_name=name
        
spurs=Team("San Antonio Spurs")

## 3. More Interesting Instance Properties ##

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It is automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

# Initialize a player using the first row of our data set
first_player = Player(nba[0])

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        # Team roster initially empty
        self.roster = []
        # Find the players for the roster in the data set
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
        
        
spurs=Team("San Antonio Spurs")


## 4. Instance Methods ##

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class 
    # It's automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        # Team roster initially empty
        self.roster = []
        # Find the players for the roster in the data set
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    # Implement the average_age() instance method
    def average_age(self):
        sum=0
        for player in self.roster:
            sum=sum+player.age
        return sum/self.num_players()
    
    
spurs = Team("San Antonio Spurs")
spurs_num_players = spurs.num_players()
spurs_avg_age=spurs.average_age()

## 5. Class Methods ##

import math

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It's automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
   
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    
    @classmethod
    def older_team(self, team1, team2):
       one=team1.average_age()
       two=team2.average_age()
       if one>two:
            return team1
       else:
            return team2
        
old_team=Team.older_team(Team("New York Knicks"),Team("Miami Heat"))

## 7. Overloading Inherited Behavior ##

class Player(object):
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It is automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]
    def __lt__(self, other):
        return self.age < other.age
    # Implement the rest of the comparison operators here
    def __gt__(self,other):
        return self.age>other.age
    def __le__(self,other):
        return self.age<=other.age
    def __ge__(self,other):
        return self.age>=other.age
    def __eq__(self,other):
        return self.age==other.age
    def __ne__(self,other):
        return self.age!=other.age
    

carmelo = Player(nba[17])
kobe = Player(nba[68])
result=(carmelo!=kobe)

## 8. Comparing Average Ages ##

import math

class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    # Define operators here
    def __lt__(self, other):
        return self.average_age() < other.average_age()
    def __gt__(self, other):
        return self.average_age() > other.average_age()
    def __le__(self, other):
        return self.average_age() <= other.average_age()
    def __ge__(self, other):
        return self.average_age() >= other.average_age()
    def __eq__(self, other):
        return self.average_age() == other.average_age()
    def __ne__(self, other):
        return self.average_age() != other.average_age()

jazz = Team("Utah Jazz")
pistons = Team("Detroit Pistons")
older_team = max([jazz, pistons])

## 9. Oldest NBA Team ##

import math

class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    def __lt__(self, other):
        return self.average_age() < other.average_age()
    def __gt__(self, other):
        return self.average_age() > other.average_age()
    def __le__(self, other):
        return self.average_age() <= other.average_age()
    def __ge__(self, other):
        return self.average_age() >= other.average_age()
    def __eq__(self, other):
        return self.average_age() == other.average_age()
    def __ne__(self, other):
        return self.average_age() != other.average_age()

team_names = ["Boston Celtics", "Brooklyn Nets", "New York Knicks", "Philadelphia 76ers", "Toronto Raptors", 
         "Chicago Bulls", "Cleveland Cavaliers", "Detroit Pistons", "Indiana Pacers", "Milwaukee Bucks",
         "Atlanta Hawks", "Charlotte Hornets", "Miami Heat", "Orlando Magic", "Washington Wizards",
         "Dallas Mavericks", "Houston Rockets", "Memphis Grizzlies", "New Orleans Pelicans", "San Antonio Spurs",
         "Denver Nuggets", "Minnesota Timberwolves", "Oklahoma City Thunder", "Portland Trail Blazers", "Utah Jazz",
         "Golden State Warriors", "Los Angeles Clippers", "Los Angeles Lakers", "Phoenix Suns", "Sacramento Kings"]

# Alter this list comprehension
teams = list([Team(name) for name in team_names])
oldest_team=max(teams)
youngest_team = min(teams)
sorted_teams = sorted(teams)