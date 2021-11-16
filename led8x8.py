
from shifter import Shifter    # extend by composition

class led():

  numbers = [ 
    0b11111110, # 0 
    0b11111101, # 1
    0b11111011, # 2
    0b11110111, # 3
    0b11101111, # 4
    0b11011111, # 5
    0b10111111, # 6
    0b01111111] # 7

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, r, c):
    self.shifter.shiftByte(led.numbers[r])  
    self.shifter.shiftByte(1 << (c-1))   
      