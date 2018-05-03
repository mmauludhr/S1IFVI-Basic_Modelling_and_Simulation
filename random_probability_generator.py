from random import choice
import numpy
import collections
import csv
import os
from itertools import izip_longest

numberofserver = 1;

def simulation():
    '''
    // Probabilitas dari waktu kedatangan (arrival) & waktu servis (service).
    '''
    arrivals = [0]*10 + [1]*15 + [2]*10 + [3]*35 + [4]*25 + [5]*05
    services = [1]*25 + [2]*20 + [3]*40 + [4]*15

    '''
    // Menghasilkan data waktu pelanggan berdasarkan probabilitas yang dimiliki
    // Pelanggan ke-1 selalu memiliki waktu kedatangan 0. (Berdasarkan asumsi)
    '''
    customerdata = [(0,choice(services))] + [(choice(arrivals), choice(services)) for i in range(10)]

    '''
    // Menghitung waktu kedatangan secara iteratif.
    '''
    arrivaltimes = [0] + numpy.cumsum([c[0] for c in customerdata])
    customers = collections.deque([(c[0],c[1],arrivaltimes[i]) for i, c in enumerate(customerdata)])

    '''
    //
    '''
    waiting = collections.deque()

    '''
    //
    '''
    server = [(False, 0, False)] * numberofserver;

    '''
    // Penentuan waktu awal
    '''
    time = 0;
    return (customers)



    arrival_time_file = open("arrival_time_file.txt", "w")
    service_time_file = open("service_time_file.txt", "w")
    # for cust in customers:
    #     print cust






    #     arrival_time_file.write("%s\n" % cust[0])
    #     service_time_file.write("%s\n" % cust[1])
    # arrival_time_file.close()
    # service_time_file.close()

    # print customerdata, "\n"
    # print customers

    # mean_arrival = 0
    # for i in customers:
    #     mean_arrival += i[0]
        # print i[0]

    # for x in customers:
    #     print x
    #
    # print "Mean Arrival: ", mean_arrival/float(len(customers))
    # print "Length customers: ", float(len(customers))

########################
##### MAIN PROGRAM #####
########################
a = simulation();
print a;

# for i in range(0, 10):
#     simulation()
