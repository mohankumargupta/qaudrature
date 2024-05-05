from amaranth import *
from amaranth.sim import *
from myhdlpeek.amaranth import Peeker
  
class Encoder(Elaboratable):
    '''A simple counter that increments at every clock cycle.'''
    def __init__(self):
        self.a = Signal(1)
        self.b = Signal(1)
        
        # Create monitors for the counter value and individual bits.
        Peeker(self.a, 'A')
        Peeker(self.b, 'B')

    def ports(self):
        return [self.a, self.b]
 
    def elaborate(self, platform):
        m = Module()
        #toggle = Signal(1, reset=1)
        #toggle = Signal(1, init=1)
        toggle = Signal(1)
        aa = Signal(1)
        bb = Signal(1)

        with m.FSM():
            with m.State("zero"):
                m.d.sync += [
                    aa.eq(0),
                    bb.eq(0)
                ]
                m.next = "one"
            with m.State("one"):
                m.d.sync += [
                    aa.eq(1),
                    bb.eq(0)
                ]
                m.next = "two"
            with m.State("two"):
                m.d.sync += [
                    aa.eq(1),
                    bb.eq(1)
                ]
                m.next = "three"
            with m.State("three"):
                m.d.sync += [
                    aa.eq(0),
                    bb.eq(1)
                ]
                m.next = "zero"                

        m.d.comb += [
            self.a.eq(aa),
            self.b.eq(bb)
        ]
        return m
    
