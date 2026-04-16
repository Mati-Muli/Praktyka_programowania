class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        # przeniesienie logiki zliczania punktów do funkcji
        if player_name == self.player1_name:
            self.p1points +=1
        else:
            self.p2points +=1
    # ponowne zastosowanie słownika
    Callouts = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    def score(self):
        if self.p1points == self.p2points:
           if self.p1points > 2:
               return "Deuce"
           else:
               return f"{self.Callouts[self.p1points]}-All"

        if self.p1points >= 4 or self.p2points >= 4:
            #ponowne zastosowanie tej samej logiki co w tennis1
            return self.advantage()
        return f"{self.Callouts[self.p1points]}-{self.Callouts[self.p2points]}"
    def advantage(self):
        # odseparowanie logiki wyliczania przewagi i zwyciętwa, używając modułu różnicy wyniku
        diff = self.p1points-self.p2points
        if diff > 0:
            leader = self.player1_name
        else:
            leader = self.player2_name
        if abs(diff) == 1:
            return f"Advantage {leader}"
        else:
            return f"Win for {leader}"

