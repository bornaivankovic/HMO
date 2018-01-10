from test import Test
from machine import Machine
from resource import Resource
from simulation import Simulation
from random import randint

# array of instance file names
instances=["ts"+str(i)+".txt" for i in range(1,11)]

# array of instance file lines
with file(instances[1],"r") as f:
    lines=[x.strip() for x in f.readlines()]

# number of tests, machines, resources
n_tests=int(lines[1].split(": ")[1])
n_machines=int(lines[2].split(": ")[1])
n_resources=int(lines[3].split(": ")[1])


tests,machines,resources={},{},{}

# tests objects from file
i=5
for i in range(i,i+n_tests):
    split=lines[i].split("( ")[1][:-2].split(", ")
    test=Test(eval(split[0]),eval(split[1]),eval(split[2]),eval(split[3]))
    tests[test.name]=test

# machine objects from file
i+=2
for i in range(i,i+n_machines):
    name=lines[i].split("( ")[1][:-2]
    machine=Machine(eval(name))
    machines[machine.name]=machine

#resource objects from file
i+=2
for i in range(i,i+n_resources):
    split=lines[i].split("( ")[1][:-2].split(", ")
    resource=Resource(eval(split[0]),eval(split[1]))
    resources[resource.name]=resource

simulation=Simulation(machines, resources)
simulation.start(tests)
