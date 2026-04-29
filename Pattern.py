class Pattern(object):
    def __init__(self, pattern: list[int]):
        self.pattern = pattern
    def __eq__(self, value):
        return self.pattern == value.pattern
    def __hash__(self):
        return str(self.pattern).__hash__()
    def __repr__(self):
        return str(self.pattern)