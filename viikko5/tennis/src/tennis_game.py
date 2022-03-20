class TennisGame:
    class Player:
        def __init__(self, name):
            self._name = name
            self._score = 0

        def addPoint(self):
            self._score += 1

        @property
        def name(self):
            return self._name

        @property
        def score(self):
            return self._score
        
    def __init__(self, nameA, nameB):
        self.playerA = self.Player(nameA)
        self.playerB = self.Player(nameB)        

        self.score_strings = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.playerA.name:
            self.playerA.addPoint()
        else:
            self.playerB.addPoint()

    def get_score(self):
        if self.playerA.score == self.playerB.score:
            if self.playerA.score > 3:
                return "Deuce"
            else:
                return self.score_strings[self.playerA.score] + "-All"

        if self.playerA.score >= 4 or self.playerB.score >= 4:
            difference = self.playerA.score - self. playerB.score

            if difference > 0:
                playerName = self.playerA.name
            else:
                playerName = self.playerB.name
                
            if abs(difference) == 1:
                return "Advantage " + playerName
            else:
                return "Win for " + playerName

        return self.score_strings[self.playerA.score] + "-" + self.score_strings[self.playerB.score]

