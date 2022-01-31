

class Connector:

    def __init__(self, fgate, tgate) -> None:
        self.from_gate = fgate
        self.to_gate = tgate
        
        # in the BinaryGate class, for gates with two possible input lines,
        # the connector must be connected to only one line. If both of them
        # are available we will choose pin_a by default. If pin_a is already
        # connnected, then we will choose pin_b. It is not possible to
        # connect to a gate with no available input lines.
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate