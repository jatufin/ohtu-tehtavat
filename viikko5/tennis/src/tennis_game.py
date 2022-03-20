class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_strings = ["Love", "Fifteen", "Thirty", "Forty"]
        
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            if self.m_score1 > 3:
                score = "Deuce"
            else:
                score = self.score_strings[self.m_score1] + "-All"

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = self.score_strings[self.m_score1] + "-" + self.score_strings[self.m_score2]

        return score
