from numpy import inf

class Simulation():
    def __init__(self,machines,resources):
        self.machines=machines
        self.resources=resources
        self.T = 500
        self.T_min = 0.01
        self.alpha = 0.9

        for machine in machines:
            print machines[machine].name


    def get_available_machine(self, machines, time):
        for machine in machines:
            print

    def resources_available_at(self, test):
        resources=[]





    def start(self, tests):
        T_tmp = self.T
        self.resources_available_at(tests)






