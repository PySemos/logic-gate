
class LogicGate:
    """
    Most general class to build a Logic Gate. Contains the methods 
    which every Logic Gate needs to know: the gate label and the 
    output of value.
    """

    def __init__(self, n) -> None:
        self.label = n
        self.output = None

    def get_label(self):
        """Allows the user of a gate to ask the gate for its label."""
        return self.label

    def get_output(self):
        """Returns the output value of the logic gate."""
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """
    Subclass of LogicGate class which adds two input lines.
    """

    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        super().__init__(n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        """Gets the first input line from the user."""
        return int(input("Enter Pin A input for gate " \
            + self.get_label() \
            + "-->"))

    def get_pin_ab(self):
        """Gets the second input line from the user."""
        return int(input("Enter Pin B input for gate " \
            + self.get_label() \
            + "-->"))


class UnaryGate(LogicGate):
    """
    
    """

    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        super().__init__(n)
    
