class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    #zastąpienie nieopisanej zmiennej n znaną juz zmienną player_name
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1
    Callouts = ["Love", "Fifteen", "Thirty", "Forty"]
    #ujednolicenie nazwenictwa, brak jednoliterowych nazw
    def score(self):
        if (self.p1points < 4 and self.p2points < 4) and (self.p1points + self.p2points < 6):
            result = self.Callouts[self.p1points]
            return result + "-All" if (self.p1points == self.p2points) else result + "-" + self.Callouts[self.p2points]
        if self.p1points == self.p2points:
                return "Deuce"
        return self.advantage()

    def advantage(self):
            #zastosowanie logiki przewagi
            diff = self.p1points - self.p2points
            if diff > 0:
                leader = self.player1_name
            else:
                leader = self.player2_name
            if abs(diff) == 1:
                return f"Advantage {leader}"
            else:
                return f"Win for {leader}"
