from test import Test
from machine import Machine
from resource import Resource
from simulation import Simulation
from time import time
from collections import deque

instances=["ts"+str(i)+".txt" for i in range(1,11)]
with file(instances[0],"r") as f:
    lines=[x.strip() for x in f.readlines()]

n_tests=int(lines[1].split(": ")[1])
n_machines=int(lines[2].split(": ")[1])
n_resources=int(lines[3].split(": ")[1])
tests,machines,resources=[],[],[]
i=5
for i in range(i,i+n_tests):
    split=lines[i].split("( ")[1][:-2].split(", ")
    test=Test(eval(split[0]),eval(split[1]),eval(split[2]),eval(split[3]))
    tests.append(test)

i+=2
for i in range(i,i+n_machines):
    name=lines[i].split("( ")[1][:-2]
    machine=Machine(eval(name))
    machines.append(machine)
i+=2
for i in range(i,i+n_resources):
    split=lines[i].split("( ")[1][:-2].split(", ")
    resource=Resource(eval(split[0]),eval(split[1]))
    resources.append(resource)

start=time()
sim=Simulation(machines,resources)
a=sim.run_simulation(deque(tests))
print a,time()-start




