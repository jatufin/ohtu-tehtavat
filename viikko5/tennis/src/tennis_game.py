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

        elif self.playerAScore >= 4 or self.playerBScore >= 4:
            minus_result = self.playerAScore - self. playerBScore

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = self.score_strings[self.playerAScore] + "-" + self.score_strings[self.playerBScore]

        return score
