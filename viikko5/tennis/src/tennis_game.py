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

        def getScore(self, otherPlayer):
            scoreWords = ["Love", "Fifteen", "Thirty", "Forty"]
        
            if self.score == otherPlayer.score:
                if self.score > 3:
                    return "Deuce"
                else:
                    return scoreWords[self.score] + "-All"
                
            if self.score < 4 and otherPlayer.score < 4:
                return scoreWords[self.score] + "-" + scoreWords[otherPlayer.score]

            difference = self.score - otherPlayer.score
            playerName = self.name if difference > 0 else otherPlayer.name

            if abs(difference) == 1:
                return "Advantage " + playerName

            return "Win for " + playerName

            

    def __init__(self, nameA, nameB):
        self.players = {
            nameA: self.Player(nameA),
            nameB: self.Player(nameB)            
        }

    def won_point(self, playerName):
        self.players[playerName].addPoint()

    def get_score(self):
        playerA, playerB = self.players.values()
        return playerA.getScore(playerB)


