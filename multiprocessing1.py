#!/usr/bin/python3

# multiprocessing1.py  (do not rename this to multiprocessing.py bcuz a namespace collision will break the interpreter)
# Version 1.0
# Illustrate Python multiprocessing that forks new processes
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

