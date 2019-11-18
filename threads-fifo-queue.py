#!/usr/bin/python3.6
# threads-fifo-queue.py
# version 1.0
# Send messages between 2 sub-threads via Python queue
# by D.J. Davis
# Python version at creation 3.6.8
# Copyright (C) 2019 D.J. Davis  All Rights Reserved
# License: Non-commercial use only. All other uses are prohibited

import threading
import queue
import time

for i in range (100000000):
    pass


def thread_1 ():
#Define Sub-thread 1
    i = 0
    x = 0

    while 1:

        #Read sub-thread's own queue and print entries
        print ("Thread 1 - Read Queue 1")
        while not q1.empty():
            print ("    Thread 1 queue: ", q1.get())

        # Stop after a certain amount & time. Comment for indefinite run
        if i > 100: 
            print ("Thread 1 - End")
            quit ()

        # Create messages for other thread Subthread 2
        print ("Thread 1 - Gen msgs for Thread 2")
        for x in range (1, 21):
            i = i + 1
            if (i / 11) == (i // 11):
                string1 = str(i) + " is divisible by 11"
                q2.put (string1)
            if (i / 13) == (i // 13):
                string1 = str(i) + " is divisible by 13"
                q2.put (string1)
            if (i / 17) == (i // 17):
                string1 = str(i) + " is divisible by 17"
                q2.put (string1)

        time.sleep(1)
#End Definition of Sub-thread 1


def thread_2 ():
#Define Subthread 2
    j = 0
    y = 0

    while 1:

        #Read sub-thread's own queue and print entries
        print ("Thread 2 - Read Queue 2")
        while not q2.empty():
            print ("    Thread 2 queue: ", q2.get())

        # Stop after a certain amount & time. Comment for indefinite run 
        if j > 100: 
            print ("Thread 2 - End")
            quit ()

        # Create messages for other thread Subthread 1
        print ("Thread 2 - Gen msgs for Thread 1")
        for y in range (1, 21):
           j = j + 1 
           if (j / 11) == (j // 11):
                string2 = str(j) + " is divisible by 11"
                q1.put (string2)
           if (j / 13) == (j // 13):
                string2 = str(j) + " is divisible by 13"
                q1.put (string2)
           if (j / 17) == (j // 17):
                string2 = str(j) + " is divisible by 17"
                q1.put (string2)

        time.sleep(1)
#End Definition of Sub-thread 2


print ("MAIN THREAD - Execution Begins")

q1 = queue.Queue()  ##define FIFO queue. Thread 2 writes, Thread 1 reads
q2 = queue.Queue () ##define FIFO queue. Thread 1 writes. Thread 2 reads

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)  
t1.start()
print ("MAIN THREAD - Thread 1 has been started")
time.sleep (1)
t2.start()
print ("MAIN THREAD - Thread 2 has been started")

print ("MAIN THREAD - Execution Ends")  # Worker threads continue to execute
quit ()

