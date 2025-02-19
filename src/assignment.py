def create_player_tag(player_name, player_number):
    """
    Create a player tag by combining the player's name and number.
    
    Args:
        player_name (str): The player's name
        player_number (int): The player's number
    
    Returns:
        str: A string combining the name and number with '#' between them
        
    Example:
        create_player_tag("Mario", 123) should return "Mario#123"
    """
    # Your code here
    player_number_string = str(player_number)
    tag = player_name + '#' + player_number_string
    return tag


    pass

def calculate_points_needed(current_score, target_score):
    """
    Calculate how many more points are needed to reach the target score.
    
    Args:
        current_score (int): The current score
        target_score (int): The target score to reach
    
    Returns:
        int: The difference between target and current score
        
    Example:
        calculate_points_needed(100, 150) should return 50
    """
    # Your code here
    points_needed = (target_score - current_score)
    current_score = 100
    target_score = 150


    return points_needed


    pass

def create_team_roster(team_size, player_symbol):
    """
    Create a roster string that repeats the player symbol based on team size.
    
    Args:
        team_size (int): Number of players on the team
        player_symbol (str): Symbol to represent each player
    
    Returns:
        str: A string with the player symbol repeated team_size times
        
    Example:
        create_team_roster(3, "🏃") should return "🏃🏃🏃"
    """
    # Your code here
    meh = (team_size * player_symbol)
    team_size = 3
    player_symbol = '🏃'
                        
    


    return meh



def distribute_powerups(total_powerups, players_count):
    """
    Calculate how many powerups will be left over after distributing them equally.
    
    Args:
        total_powerups (int): Total number of powerups available
        players_count (int): Number of players to distribute to
    
    Returns:
        int: Number of powerups that will be left over
        
    Example:
        distribute_powerups(10, 3) should return 1 (3 players get 3 each, 1 left over)
    """
    # Your code here
    leftover = (total_powerups % players_count)



    
    return leftover