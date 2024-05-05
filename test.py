from quadrature import Quadrature
from amaranth.sim import *
from myhdlpeek.amaranth import Peeker

quadrature = Quadrature()

Peeker(quadrature.led, 'led')
sim = Simulator(quadrature)

def simple():
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    yield    
    yield Delay(1)

sim.add_process(simple)
Peeker.assign_simulator(sim, use_vcd_writer=True)
sim.run_until(1)

Peeker.to_html_table()