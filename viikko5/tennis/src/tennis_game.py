class TennisGame:
    def __init__(self, playerAName, playerBName):
        self.playerAName = playerAName
        self.playerBName = playerBName
        self.playerAScore = 0
        self.playerBScore = 0
        self.score_strings = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.playerAName:
            self.playerAScore = self.playerAScore + 1
        else:
            self.playerBScore = self.playerBScore + 1

    def get_score(self):
        if self.playerAScore == self.playerBScore:
            if self.playerAScore > 3:
                return "Deuce"
            else:
                return self.score_strings[self.playerAScore] + "-All"

        if self.playerAScore >= 4 or self.playerBScore >= 4:
            difference = self.playerAScore - self. playerBScore

            if difference > 0:
                playerName = self.playerAName
            else:
                playerName = self.playerBName
                
            if abs(difference) == 1:
                return "Advantage " + playerName
            else:
                return "Win for " + playerName

        return self.score_strings[self.playerAScore] + "-" + self.score_strings[self.playerBScore]

