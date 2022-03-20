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

        def get_score(self, otherPlayer):
            score_strings = ["Love", "Fifteen", "Thirty", "Forty"]
        
            if self.score == otherPlayer.score:
                if self.score > 3:
                    return "Deuce"
                else:
                    return score_strings[self.score] + "-All"
                
            if self.score >= 4 or otherPlayer.score >= 4:
                difference = self.score - otherPlayer.score
                    
                if difference > 0:
                    playerName = self.name
                else:
                    playerName = otherPlayer.name
                        
                if abs(difference) == 1:
                    return "Advantage " + playerName
                else:
                    return "Win for " + playerName

            return score_strings[self.score] + "-" + score_strings[otherPlayer.score]

    def __init__(self, nameA, nameB):
        self.playerA = self.Player(nameA)
        self.playerB = self.Player(nameB)       

    def won_point(self, player_name):
        if player_name == self.playerA.name:
            self.playerA.addPoint()
        else:
            self.playerB.addPoint()

    def get_score(self):
        return self.playerA.get_score(self.playerB)


