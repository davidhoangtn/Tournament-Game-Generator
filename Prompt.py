import time
"""
Instructions:
    Create a program that can schedule games that teams will play

Variables:
    Team names: str
        _ All team names contain at most 2 words and at 
        least 2 characters
    Number of teams: int (even)
        _At least 2 teams 
    Names of teams: str
    Number of games (played by each team): int
        _store in some way: lst, dct, tup ...
        _assume each team plays same number of games
        _Each team play every other team at least once    
    Number of wins (each team had): int 
        _during season
        _Each team had minimum of 0 wins, 
            and <= number of games they played

Input:
    _Make sure all input is valid
    _Ask user to try again if invalid
    _Assume user input will always be the correct type (or not)

Output: (Tournament Game Generator)
    _Most wins vs least wins
    _Second most wins vs second least wins ...
    _etc
    _Same wins --> can choose any appropriate team
"""

# Input number of teams in tournament (>2)
TEAM_NUM = int(input("Enter the number of teams in the tournament: "))
while TEAM_NUM < 2:
    print('The minimum number of teams is 2, try again')
    TEAM_NUM = int(input("Enter the number of teams in the tournament: "))

# Input team names (most 2 words, least 2 characters)
TEAM_NAMES = []
for num in range(1, TEAM_NUM + 1):
    team_name = input(f'Enter the name for team #{str(num)}: ')
    while len(team_name) <= 1:
        print('Team names must have at least 2 characters, try again.')
        team_name = input(f'Enter the name for team #{str(num)}: ')
    while len(team_name.split(' ')) > 2:
        print('Team names must have at most 2 words, try again.')
        team_name = input(f'Enter the name for team #{str(num)}: ')
    TEAM_NAMES.append(team_name)
    #print(TEAM_NAMES)
# Input number of team games:    
NUM_GAMES = int(input("Enter the number of games played by each team: "))
while NUM_GAMES < (TEAM_NUM - 1):
    print("""Invalid number of games. Each team plays each other at \nleast once in the regular season, try again.""" )
    NUM_GAMES = int(input("Enter the number of games played by each team: "))

# Input number of wins by each team in regular season
NUM_WINS = []
for team_name in TEAM_NAMES:
    num_wins = int(input(f"Enter the number of wins Team {team_name} had: "))
    
    while num_wins > NUM_GAMES:
        print(f"The maximum number of wins is {str(NUM_GAMES)}, try again ")
        num_wins = int(input(f"Enter the number of wins Team {team_name} had: "))
    
    while num_wins < 0:
        print("The minimum number of wins is 0, try again.")
        num_wins = int(input(f"Enter the number of wins Team {team_name} had: "))
    NUM_WINS.append(num_wins)
    #print(NUM_WINS)
print('Generating the games to be played in the first round of the tournament...')
time.sleep(2)

# use while loop to destructively loop over list and return 
    # teams playing
while len(TEAM_NAMES) > 0:
    first_team =  TEAM_NAMES.pop(NUM_WINS.index(max(NUM_WINS)))
    NUM_WINS.remove(max(NUM_WINS))
    second_team = TEAM_NAMES.pop(NUM_WINS.index(min(NUM_WINS)))
    NUM_WINS.remove(min(NUM_WINS))
    print(f'Home: {first_team} VS AWAY: {second_team}')    
    
print('Finished code!')