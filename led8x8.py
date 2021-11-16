# LEDdisplay class
import time
from shifter import Shifter    # extend by composition
import random

class Led8x8():

  #'Class for controlling a 7-segment LED display'
  numbers = [  #sequence for different positions
    0b11111110, # 0 
    0b11111101, # 1
    0b11111011, # 2
    0b11110111, # 3
    0b11101111, # 4
    0b11011111, # 5
    0b10111111, # 6
    0b01111111] # 7

  def __init__(self, data, latch, clock): #make the definition off of the shifter class
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, x, y):
       # change this value to pick which row the pattern appears on
    self.shifter.shiftByte(Led8x8.numbers[y])  # load the row values
    self.shifter.shiftByte(1 << (x-1))   # select the given row
      