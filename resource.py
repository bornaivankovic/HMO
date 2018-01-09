class Resource():
    def reset(self):
        self.current=0

    def __init__(self,name,n):
        self.name=name
        self.n=n
        self.reset()

    def __hash__(self):
        return hash(self.name)

    def __cmp__(self,other):
        if isinstance(other,Resource):
            return cmp(self.name,other.name)
        else:
            return cmp(self.name,other)

    def __repr__(self):
        return self.name