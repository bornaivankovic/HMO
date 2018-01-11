
class Greedy():
    def __init__(self, machines, resources, tests):
        self.machines = machines
        self.resources = resources
        self.tests = tests

    def start(self, i):
        self.reset()

        for test in self.tests:
            machine_to_run = self.get_available_machine(test)
            latest_resource = self.get_available_resources(test)

            time_to_run = max(machine_to_run.available_at, latest_resource.available_at if latest_resource else 0)
            self.machines[machine_to_run.name].available_at = time_to_run + test.duration

            if latest_resource:
                for resource in test.resources:
                    self.resources[resource].available_at = time_to_run + test.duration

        print 'iteration: ', i, '', max(self.machines[machine].available_at for machine in self.machines)
        return max(self.machines[machine].available_at for machine in self.machines)


    def get_available_machine(self, test):
        test_machines = test.machines
        machines_to_iterate = self.machines

        if len(test_machines) > 0:
            machines_to_iterate = {}
            for machine in test_machines:
                machines_to_iterate[machine] = self.machines[machine]

        first_available = machines_to_iterate[list(machines_to_iterate.keys())[0]]

        for machine in machines_to_iterate:
            if machines_to_iterate[machine].available_at < first_available.available_at:
                first_available = machines_to_iterate[machine]

        return first_available




    def get_available_resources(self, test):
        test_resources = test.resources
        last_available = None

        if len(test_resources) > 0:

            last_available = self.resources[test_resources[0]]

            for resource in test_resources:
                if self.resources[resource].available_at > last_available.available_at:
                    last_available = self.resources[resource]

        return last_available

    def reset(self):
        for machine in self.machines:
            self.machines[machine].available_at = 0
        for resource in self.resources:
            self.resources[resource].available_at = 0
