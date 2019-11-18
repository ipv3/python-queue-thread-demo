#!/usr/bin/python3.6

# fifo-queue.py
# Version 1.0
# Illustrate Python FIFO queue
# by D.J. Davis
# Created 11/5/2019
# Python version at creation 3.6.8
# Copyright (C) 2019 D.J. Davis  All Rights Reserved
# License: Non-commercial use only. All other uses are prohibited

import queue

q = queue.Queue()

for i in range(1, 5):
    contents = str (i) + " " + "x" * 20
    print ("Writing to queue:  " + contents, end="")
    q.put(contents, timeout=2)
    print ("   (Done)" + str(i))

while not q.empty():
    q_content = q.get()  # Yes, could have used   print ( q.get() )  but need variable later
    print (q_content)

exit ()


# Extras for presentation examples
# , timeout=n
#####    print (len(q_content))
#####    print (q.get())


#class Task(object):
#    def __init__(self, priority, name):
#        self.priority = priority
#        self.name = name
#        
#    def __cmp__(self, other):
#        return cmp(self.priority, other.priority)

