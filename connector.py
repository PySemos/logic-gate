

class Connector:

    def __init__(self, fgate, tgate) -> None:
        self.from_gate = fgate
        self.to_gate = tgate
        
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate