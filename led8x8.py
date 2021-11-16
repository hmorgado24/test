
from shifter import Shifter    # extend by composition

class led():

  pat = [
    0b01111111,
    0b10111111,
    0b11011111,
    0b11101111,
    0b11110111,
    0b11111011,
    0b11111101,
    0b11111110]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, r, c):
    self.shifter.shiftByte(led.pat[c])  
    self.shifter.shiftByte(1 << (r-1))   
      