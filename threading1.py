#!/usr/bin/python3

# threading1.py  (do not rename this to threading.py bcuz a namespace collision will break the interpreter)
# Version 1.0
# Illustrate Python FIFO queue
# by D.J. Davis
# Created 11/5/2019
# Python version at creation 3.6.8
# Copyright (C) 2019 D.J. Davis  All Rights Reserved
# License: Non-commercial use only. All other uses are prohibited

import threading
import time

## Define supprocess/thread 1
def print_hello():
  for i in range(10):
    time.sleep(0.5)
    print("Hello")

## Define supprocess/thread 2
def print_hi(): 
    for i in range(4): 
      time.sleep(0.7)
      print("Hi") 

## Bind supproccesses to objects
t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  

## Start/run subpresses
t1.start()
time.sleep (2)
t2.start()

for i in range (6):
    print ("Main thread - continue execution after calling forking subprocesses...")

exit ()
## Even after exit is raised in main thread, the subthreads continue to execute until completion


