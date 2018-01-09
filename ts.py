from test import Test
from machine import Machine
from resource import Resource
from simulation import Simulation
from time import time
from collections import deque
from helpers import generate_neighbourhood,is_tabu

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

sim=Simulation(machines,resources)

best_candidate=range(len(tests))
best_fitness=sim.run_simulation(deque([tests[x] for x in best_candidate]))
tabu_list=deque()
max_tabu_size=5
start=time()
neighbourhood_size=20

time_limit=60
while time()-start<time_limit:
    neighbourhood=generate_neighbourhood(best_candidate,neighbourhood_size)
    remove=[]
    for i in neighbourhood:
        if is_tabu(tabu_list,i,5):
            remove.append(i)
    for i in remove:
        neighbourhood.remove(i)
    fitness_list=[]
    for i in neighbourhood:
        fitness_list.append(sim.run_simulation(deque([tests[x] for x in i])))
    if best_fitness>min(fitness_list):
        best_fitness=min(fitness_list)
        best_candidate=neighbourhood[fitness_list.index(best_fitness)]
    tabu_list.append(best_candidate)
    if len(tabu_list)>max_tabu_size:
        tabu_list.popleft()
    print best_candidate,best_fitness


