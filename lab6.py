import time
import random
from led8x8 import led
import multiprocessing

def bug(dataPin, latchPin, clockPin): 
  row = random.randint(1, 8)
  col = random.randint(0, 7)

  leddisp = led(dataPin, latchPin, clockPin) 

  while True:
    Rrow = random.randint(-1, 1) 
    Rcol = random.randint(-1, 1)  

    leddisp.display(row, col)
    time.sleep(0.1) 

    if (row + Rrow < 1 or row + Rrow > 7): 
      row = row 
    else:
      row += Rrow 

    if (col + Rcol < 0 or col + Rcol > 7): 
      col = col 
    else:
      col += Rcol 

dataPin, latchPin, clockPin = 21, 19, 26 

p = multiprocessing.Process(target=bug, args=(dataPin, latchPin, clockPin)) 
p.start() 
