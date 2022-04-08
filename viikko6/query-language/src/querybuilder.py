from matchers import All, Or, HasAtLeast, PlaysIn, HasFewerThan


class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self._matcher, team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self._matcher, value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(self._matcher, value, attr))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(self._matcher, matchers))
