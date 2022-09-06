class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
    

    #return self.players.count(player_name) > 0
    def has_player(self, player_name):
        return self.players.count(player_name) > 0

    def play_game(self, game_won):
        if game_won:
            self.points += 3
