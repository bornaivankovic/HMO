class Simulation():
    def __init__(self,machines,resources):
        self.machines=machines
        self.resources=resources

    def nr_machines_working(self):
        cnt=0
        for i in self.machines:
            if i.running_test!=None:
                cnt+=1
        return cnt

    def run_simulation(self,tests):
        ticks=0
        while True:
            if not tests and self.nr_machines_working()==0:
                break
            ticks+=1
            for i in self.machines:
                try:
                    cur_test=tests.popleft()
                except:
                    cur_test=None
                if cur_test==None and i.running_test==None:
                    continue
                if i.running_test==None and cur_test!=None and cur_test.can_run(i) and cur_test.resources_available2(self.resources):
                    i.running_test=cur_test
                    for j in cur_test.resources:
                        self.resources[self.resources.index(j)].current+=1
                    continue
                elif i.running_test!=None:
                    i.running_test.run_time+=1
                    if i.running_test.duration==i.running_test.run_time:
                        i.running_test.run_time=0
                        i.running_test.unlock_resources(self.resources)
                        i.running_test=None
                if cur_test!=None:
                    tests.append(cur_test)

        for i in self.machines:
            i.reset()
        for i in self.resources:
            i.reset()
        return ticks