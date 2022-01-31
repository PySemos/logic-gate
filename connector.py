

class Connector:

    def __init__(self, fgate, tgate) -> None:
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a == source
        else: 
            if self.pin_b == None:
                self.pin_b == source
            else:
                raise RuntimeError("Error: there are no empty pins")