class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        players = list(filter(
            lambda p: p.nationality == nationality,
            self._players
        ))

        players.sort(
            key=lambda p: p.assists + p.goals,
            reverse=True
        )

        return players
        
