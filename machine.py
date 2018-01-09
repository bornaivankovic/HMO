class Machine():
    def reset(self):
        self.running_test=None

    def __init__(self,name):
        self.name=name
        self.reset()

    def __hash__(self):
        return hash(self.name)

    def __cmp__(self,other):
        if isinstance(other,Machine):
            return cmp(self.name,other.name)
        else:
            return cmp(self.name,other)

    def __repr__(self):
        return self.name