#!/usr/bin/python3

# priority-queue.py
# Version 1.0
# Illustrate Python LIFO queue
# by D.J. Davis
# Created 11/5/2019
# Python version at creation 3.6.8
# Copyright (C) 2019 D.J. Davis  All Rights Reserved
# License: Non-commercial use only. All other uses are prohibited

import threading
import queue

q2 = queue.PriorityQueue ()

q2.put((100, 'a not important task') )
q2.put((5, 'a highly important task') )
q2.put((10, 'an important task') )
q2.put((5, 'a highly important task') )

codeblock = """
q2.put((100, 'a not important task') )
q2.put((5, 'a highly important task') )
q2.put((10, 'an important task') )
q2.put((5, 'a highly important task') )
"""

print ("Code to Stack the Queue: ", codeblock, "\n")

while not q2.empty():
#    print (q2.get())
    upup = q2.get()
    print ( upup [0], upup[1], " and all together: ", upup )

exit ()

