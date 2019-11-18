#!/usr/bin/python3.6

# multiprocessing.py
# Version 1.0
# Illustrate Python FIFO queue
# by D.J. Davis
# Created 11/5/2019
# Python version at creation 3.6.8
# Copyright (C) 2019 D.J. Davis  All Rights Reserved
# License: Non-commercial use only. All other uses are prohibited

import multiprocessing

def spawn (num):
    print (num)

if __name__ == '__main__' :
    for i in range (25):
        p = multiprocessing.Process (target=spawn, args=(i,))
        p.start ()
        p.join ()

exit ()

