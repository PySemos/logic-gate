from connector import *
from gates import *

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print("G4 output", g4.get_output())

#    g5 = NandGate("G5")
#    g6 = NorGate("G6")
#    g7 = XorGate("G7")

main()