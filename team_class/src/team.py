class Team:

    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0
    
    def add_player(self, new_player_name):
        self.players.append(new_player_name)
    
    # def has_player(self, player_name):
    #     for player in self.players:
    #         if player[self.name] == player:
    #             return True
    #         else:
    #             return False

    def play_game(self, boolean):
        if True:
            self.points += 3
        else:
            self.points += 0
