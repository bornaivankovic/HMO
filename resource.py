import numpy

class Resource():
    def __init__(self,name,n):
        self.name=name
        self.available_at=numpy.zeros(n, dtype=int)
        self.n=n

    def get_first_availabile(self):
        index=1
        time=numpy.inf

        for available_at in self.available_at:
            if(available_at<time):
                time=available_at
            ++index
        return {index,time}