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
        score = ""

        if self.playerAScore == self.playerBScore:
            if self.playerAScore > 3:
                score = "Deuce"
            else:
                score = self.score_strings[self.playerAScore] + "-All"

            return score

        if self.playerAScore >= 4 or self.playerBScore >= 4:
            difference = self.playerAScore - self. playerBScore

            if difference > 0:
                playerName = self.playerAName
            else:
                playerName = self.playerBName
                
            if abs(difference) == 1:
                score = "Advantage " + playerName
            else:
                score = "Win for " + playerName

            return score

        score = self.score_strings[self.playerAScore] + "-" + self.score_strings[self.playerBScore]

        return score
