class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    # def has_player(self, player):
    #     if self.players.count(player) > 0:
    #         return True

    def has_player(self, player):
        if player in self.players:
            return True

    # def has_player(self, player_name):
    #     for player in self.players:
    #         if player[self.name] == player:
    #             return True
    #         else:
    #             return False

    def play_game(self, game_won):
        if game_won:
            self.points += 3
