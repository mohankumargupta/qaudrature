from amaranth import *
from amaranth.sim import *
from myhdlpeek.amaranth import Peeker
  
class Counter(Elaboratable):
    '''A simple counter that increments at every clock cycle.'''
    def __init__(self, width):
        self.v = Signal(width)
        
        # Create monitors for the counter value and individual bits.
        Peeker(self.v, 'count')
        for bit in self.v:
            Peeker(bit, self.v.name + '_bit')
 
    def elaborate(self, platform):
        m = Module()
        m.d.sync += self.v.eq(self.v + 1)
        return m
    
