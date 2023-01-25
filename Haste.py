# This dictionary contains data about each players castle health (as an integer) and castle soldiers (as a tuple => (soldier's resistence, soldier's distance from castle)
game_dict = {"first castle health": 10, "first castle soldiers": [], "second castle health": 10, "second castle soldiers": []}

# This dictionary contains data about each players coins
coins = {"first": 0, "second": 0}

# This dictionary takes track of the functions added by graphic programmers
functions = {}

def get_status():
    '''
    this functions returns a dictionary about game status
    '''
    return game_dict

def teach(team_id, soldier_id):
    '''
    this function inputs two strings and trains a *soldier_id* soldier for the inputted
    player
    '''
    if (team_id in ["first", "second"]) and (soldier_id in ["3", "10"]):
        game_dict[team_id + " castle soldiers"].append((int(soldier_id) - 1, 0))
        coins[team_id] -= int(soldier_id)
        return True
    else:
        return False

def add_event(callback, event_id):
    '''
    this function adds the inputted function (event) to the functions dictionary
    '''
    functions[event_id] = callback

while True:
    # This is your game loop
    
    # The two following lines add coins to each player
    coins["first"] += 1
    coins["second"] += 1


    time.sleep(1)
