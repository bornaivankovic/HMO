from test import Test
from machine import Machine
from resource import Resource
from greedy import Greedy
from random import randint
import time
from numpy import inf

instances = ["ts" + str(i) + ".txt" for i in range(1, 11)]
for inst in instances:
    with file(inst, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    n_tests = int(lines[1].split(": ")[1])
    n_machines = int(lines[2].split(": ")[1])
    n_resources = int(lines[3].split(": ")[1])
    tests = []
    machines, resources = {}, {}


    i = 5
    for i in range(i, i+n_tests):
        split=lines[i].split("( ")[1][:-2].split(", ")
        required_resources = [int(resource.split("r")[1]) for resource in eval(split[3])]
        test = Test(eval(split[0]), eval(split[1]), eval(split[2]), eval(split[3]))
        tests.append(test)

    i+=2
    for i in range(i,i+n_machines):
        name=lines[i].split("( ")[1][:-2]
        machine=Machine(eval(name))
        machines[machine.name] = machine

    i+=2
    for i in range(i,i+n_resources):
        split=lines[i].split("( ")[1][:-2].split(", ")
        resource=Resource(eval(split[0]))
        resources[resource.name] = resource


    def generate_test_queue(tests):
        tests_n = [randint(1, len(tests)-1) for i in range(2)]
        test_queue = tests
        tmp_test = tests[tests_n[0]]
        test_queue[tests_n[0]] = tests[tests_n[1]]
        tests[tests_n[1]] = tmp_test
        return test_queue

    start = time.time()

    PERIOD_OF_TIME = 10

    makespan = inf

    out_file = open("simulation"+inst.split(".")[0].split("ts")[1]+".txt ", "w")

    print 'Starting simulation!'
    while True:
        test_queue = generate_test_queue(tests)
        simulation = Greedy(machines, resources, test_queue)
        result = simulation.start()
        if result['makespan'] < makespan:
            makespan = result['makespan']
            out_file.write(result['buffer'])
        if time.time() > start + PERIOD_OF_TIME : break
    out_file.close()
    print "MINSPAN: ", makespan

