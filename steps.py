from amaranth import *
from amaranth.sim import *
from myhdlpeek.amaranth import Peeker
  
class Steps(Elaboratable):
    '''A simple counter that increments at every clock cycle.'''
    def __init__(self):
        self.step = Signal(1)
        self.direction = Signal(1)
        
        
        # Create monitors for the counter value and individual bits.
        Peeker(self.step, 'S')
        Peeker(self.direction, 'D')

    def ports(self):
        return [self.step, self.direction]
 
    def elaborate(self, platform):
        m = Module()
        #toggle = Signal(1, reset=1)
        #toggle = Signal(1, init=1)
        toggle = Signal(1)
        aa = Signal(1)
        bb = Signal(1)

        m.d.comb += [
            self.step.eq(aa),
            self.direction.eq(bb)
        ]

        m.d.sync += bb.eq(1)
        m.d.sync += aa.eq(~aa)

        return m