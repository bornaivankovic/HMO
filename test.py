class Test():
    def __init__(self,name,duration,machines,resources):
        self.name=name
        self.duration=duration
        self.machines=machines
        self.resources=resources
        self.run_time=0
    
    def can_run(self,target_machine):
        if not self.machines:
            return True
        if target_machine in self.machines:
            return True
        else: return False
    
    
    """
    slower but supports multiple resources of the same type
    """
    def resources_available(self,resources):
        if not self.resources:
            return True
        cnt=0
        for i in set(self.resources):
            cur_res=resources[resources.index(i)]
            if cur_res.current+len(filter(lambda x: x==cur_res.name,self.resources))<=cur_res.n:
                cnt+=1
        if cnt==len(set(self.resources)):
            return True
        else: return False

    """
    faster but assumes only one resource of each type is available
    """
    def resources_available2(self,resources):
        if not self.resources:
            return True
        cnt=0
        for i in self.resources:
            for j in resources:
                if i==j.name and j.current<j.n:
                    cnt+=1
        if cnt==len(self.resources):
            return True
        else: return False

    def unlock_resources(self,resources):
        if self.resources:
            for i in self.resources:
                resources[resources.index(i)].current-=1

    def __repr__(self):
        return self.name
