import time
import random
from led8x8 import Led8x8
import multiprocessing

def bug(dataPin, latchPin, clockPin): 
  row = random.randint(1, 8)
  col = random.randint(0, 7)

  theLEDdisplay= Led8x8(dataPin, latchPin, clockPin) 

  while True:
    dx = random.randint(-1, 1) 
    dy = random.randint(-1, 1)  

    theLEDdisplay.display(row, col)
    time.sleep(0.1) 

    if (row + dx < 1 or row + dx > 7): 
      row = row 
    else:
      row += dx 

    if (col + dy < 0 or col + dy > 7): 
      col = col 
    else:
      col += dy 

dataPin, latchPin, clockPin = 21, 19, 26 

p = multiprocessing.Process(target=bug, args=(dataPin, latchPin, clockPin)) 
p.start() 
