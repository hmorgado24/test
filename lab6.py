import time
from shifter import Shifter    # extend by composition
import random
from led8x8 import Led8x8
import multiprocessing

def bug(dataPin, latchPin, clockPin): #lighting bug "random walking" function
    x = random.randint(1, 8)
    y = random.randint(0, 7)

    theLEDdisplay= Led8x8(dataPin, latchPin, clockPin) #create an LED display obj that extends 8x8 class

    while True:
        dx = random.randint(-1, 1) #change of x by one
        dy = random.randint(-1, 1) #change of y by one 

        theLEDdisplay.display(x, y) #display initial random position
        time.sleep(0.1) #requested time delay

        if (x + dx < 1 or x + dx > 7): #check to make sure the bug is staying in bounds
            x = x #if it would be "out of bounds" with the change keep it in the same place
        else:
            x += dx #if it won't be out of bounds then you can add the change and move by one place

        if (y + dy < 0 or y + dy > 7): #check to make sure the bug is staying in bounds
            y = y #if it would be "out of bounds" with the change keep it in the same place
        else:
            y += dy #if it won't be out of bounds then you can add the change and move by one place

dataPin, latchPin, clockPin = 21, 19, 26 #assign the appropriate pins for the shift registers

p = multiprocessing.Process(target=bug, args=(dataPin, latchPin, clockPin)) #use multiprocesssing to run the bug function continuously
p.start() #run multiprocessing 
