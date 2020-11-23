class Team:

    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0
    
    def add_player(new_player_name):
        self.players.append(new_player_name)
    
    def has_player(player_name):
        for name in self.players:
            if name == player_name:
                return True
            else:
                return False


