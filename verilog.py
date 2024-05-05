from amaranth.back import verilog
from encoder import Encoder

top = Encoder()
with open("encoder.v", "w") as f:
    f.write(verilog.convert(top, ports=top.ports()))