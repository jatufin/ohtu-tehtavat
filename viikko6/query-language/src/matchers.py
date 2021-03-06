class All:
    def matches(self, player):
        return True


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False

        return True


class Or:
    def __init__(self, matcher, matchers):
        self._matcher = matcher
        self._matchers = matchers

    def matches(self, player):
        if not self._matcher.matches(player):
            return False
        
        for matcher in self._matchers:
            if matcher.matches(player):
                return True

        return False


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def matches(self, player):
        return not self._matcher.matches(player)


class PlaysIn:
    def __init__(self, matcher, team):
        self._matcher = matcher
        self._team = team

    def matches(self, player):
        return player.team == self._team and self._matcher.matches(player)


class HasAtLeast:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value and self._matcher.matches(player)


class HasFewerThan:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value and self._matcher.matches(player)
