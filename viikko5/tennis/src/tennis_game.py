class TennisGame:
    _SCORE_WORDS = ["Love", "Fifteen", "Thirty", "Forty"]
    
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
            if self.score == otherPlayer.score:
                return self._scoreInTie(self.score)

            if self.score < 4 and otherPlayer.score < 4:
                return TennisGame._SCORE_WORDS[self.score] + "-" + TennisGame._SCORE_WORDS[otherPlayer.score]

            return self._scoreInEndGame(self, otherPlayer)

        def _scoreInTie(self, score):
            if score > 3:
                return "Deuce"
            return TennisGame._SCORE_WORDS[score] + "-All"

        def _scoreInEndGame(self, playerA, playerB):
            difference = playerA.score - playerB.score
            playerName = playerA.name if difference > 0 else playerB.name

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
