from random import choice
import numpy
import collections
import os

numberofserver = 1

def simulation():
    arrivalprob = [0]*10 + [1]*15 + [2]*10 + [3]*35 + [4]*25 + [5]*05
    serviceprob = [1]*25 + [2]*20 + [3]*40 + [4]*15

    customerdata = [(0,choice(serviceprob))] + [(choice(arrivalprob), choice(serviceprob)) for i in range(149)]
    arrivaltimes = [0] + numpy.cumsum([c[0] for c in customerdata])
    customers = collections.deque([(c[0],c[1],arrivaltimes[i]) for i, c in enumerate(customerdata)])
    pelanggan = collections.deque([(c[0],c[1],arrivaltimes[i]) for i, c in enumerate(customerdata)])
    waiting = collections.deque()

    servers = [(False, 0)] * numberofserver

    time = 0

    dataWaits = []
    dataQueueLen = []
    dataServerIdle = []

    while True:
        while len(customers) > 0 and customers[0][2] <= time:
            waiting.append(customers.popleft())
        servers = [(active, lasts - 1) for active, lasts in servers]
        servers = [(active, s) if s != 0 else (False, 0) for active, s in servers]

        curDataServerIdle = 0

        toRemove = []
        for i, zz in enumerate(servers):
            (active, s) = zz
            if not active:
                if len(waiting) > 0:
                    (a, nexts, entrytime) = waiting.popleft()
                    dataWaits += [time - entrytime]
                    servers[i] = (True, nexts)
                else:
                    curDataServerIdle += 1
        for i in reversed(toRemove):
            del servers[i]

        dataQueueLen+= [len(waiting)]
        dataServerIdle+= [curDataServerIdle]

        if len(waiting)==0 and len(customers)==0 and all([not active for active,t in servers]):
            break
        time += 1
    return (numpy.mean(dataWaits), numpy.mean(dataQueueLen))


'''
// Main Program
'''
title = "Server-" + str(numberofserver) + ".txt"
outputfile = open(title, "w")
for i in range(10):
    (avgWaitTime, avgQueueLength) = simulation();
    # print "avgWaitTime: " + str(avgWaitTime) + " | avgQueueLength: " + str(avgQueueLength)
    outputfile.write(str(i+1) + " " + str(avgWaitTime) + " " + str(avgQueueLength) + "\n")
outputfile.close()
