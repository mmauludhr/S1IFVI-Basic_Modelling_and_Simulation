from random import choice
import numpy
import collections
import csv
import os
from itertools import izip_longest

(nservers, nemergency, eenterqsize, etranstime, eexitqsize) = (1,0,0,0,0)

def runday():
    arrivals= [0]*10 + [1]*15 + [2]*10 + [3]*35 + [4]*25 + [5]*05
    services= [1]*25 + [2]*20 + [3]*40 + [4]*15
    customerdata= [(0,choice(services))] + [(choice(arrivals), choice(services)) for i in range(149)]
    arrivaltimes= [0] + numpy.cumsum([c[0] for c in customerdata])
    customers = collections.deque([(c[0],c[1],arrivaltimes[i]) for i, c in enumerate(customerdata)])
    waiting=collections.deque()

    servers=[(False,0,False)]*nservers
    emergency=nemergency
    emergencyTransitionTime=etranstime
    emergencyEnterQueueSize=eenterqsize
    emergencyExitQueueSize=eexitqsize

    time=0

    dataWaits = []
    dataQueueLen = []
    dataTimeEmergency = []
    dataEmergencyAdded = []
    dataServerIdle = []
    while True:
        while len(customers) > 0 and customers[0][2] <= time:
            waiting.append(customers.popleft())
        servers = [(active, lasts - 1, isE) for active, lasts, isE in servers]
        servers = [(active, s, isE) if s != 0 else (False, 0, isE) for active, s, isE in servers]

        curDataTimeEmercency = 0
        curDataServerIdle = 0
        curDataEmergencyAdded = 0

        toRemove = []
        for i, zz in enumerate(servers):
            (active, s, isEmergency) = zz
            if isEmergency:
                curDataTimeEmercency += 1
            if not active:
                if isEmergency and len(waiting) <= emergencyExitQueueSize:
                    toRemove += [i]
                    continue
                if len(waiting) > 0:
                    (a, nexts, entrytime) = waiting.popleft()
                    dataWaits += [time - entrytime]
                    servers[i] = (True, nexts, isEmergency)
                else:
                    curDataServerIdle += 1
        for i in reversed(toRemove):
            emergency += 1
            del servers[i]
        if emergency > 0 and len(waiting) >= emergencyEnterQueueSize:
            emergency -= 1
            curDataEmergencyAdded += 1
            servers.append((True, emergencyTransitionTime, True))

        dataQueueLen+= [len(waiting)]
        dataTimeEmergency+= [curDataTimeEmercency]
        dataEmergencyAdded+=[curDataEmergencyAdded]
        dataServerIdle+= [curDataServerIdle]

        print([len(customers),len(waiting),servers])
        if len(waiting)==0 and len(customers)==0 and all([not active for active,t,isE in servers]):
            break
        time += 1
    return ((dataWaits), numpy.mean(dataQueueLen), sum(dataServerIdle), sum(dataEmergencyAdded), sum(dataTimeEmergency), time)
datas=[];
for n in range(10):
    # print(n)
    if numpy.mod(n, 10) == 0:
        # print(n/10)
        text_file = open("Output.txt", "w")
        text_file.write(str(n/10))
        text_file.close()
    datas+=[runday()]
