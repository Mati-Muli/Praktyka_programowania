class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1
    #dodanie słownika w celu nie powtarzania tych samych nazw
    Callouts=["Love", "Fifteen", "Thirty", "Forty"]
    def score(self):
        #sama logika porównywania wyników z odniesieniami do odpowiednich funkcji
        if self.p1points == self.p2points:
            return self.tie()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.advantage()
        return f"{self.Callouts[self.p1points]}-{self.Callouts[self.p2points]}"

    def tie(self):
        #sprawdzanie czy jest remis, jeśli tak, dodanie -all
        if self.p1points>2:
            return "Deuce"
        return f"{self.Callouts[self.p1points]}-All"


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
