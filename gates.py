
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
    Subclass of LogicGate class which gets the values from the two 
    input lines.
    """

    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        """Gets the first input line from the user."""
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        """Gets the second input line from the user."""
        if self.pin_b == None:
            return int(input("Enter Pin B input for gate "+self.get_label()+"-->"))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        # in the BinaryGate class, for gates with two possible input lines,
        # the connector must be connected to only one line. If both of them
        # are available we will choose pin_a by default. If pin_a is already
        # connnected, then we will choose pin_b. It is not possible to
        # connect to a gate with no available input lines.
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: There are no available pins")


class UnaryGate(LogicGate):
    """
    Subclass of LogicGate class which gets the value from the 
    input line.
    """

    def __init__(self,n):
        # initialize any data items which are inherited.
        LogicGate.__init__(self,n)

        self.pin = None

    def get_pin(self):
        """Gets the input line from the user."""
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.get_label()+"-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin (self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: No available pins")


class AndGate(BinaryGate):
    """
    Subclass of BinaryGate which performs the "And" gate logic. Both input
    pins must be True for the gate to return True.
    """

    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        """Gets and compares pins. If both pins are 1, returns 1, else 0."""
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """
    Subclass of BinaryGate which performs the "OR" gate logic. Either input
    pin must be True for gate to return True.
    """

    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        """Gets and compares pins. If any pin is 1 it returns 1, else 0."""
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 or b==1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """
    Subclass of UnaryGate. Output is the opposite of the input pin.
    """
    def __init__(self, n) -> None:
        # initialize any data items which are inherited.
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        """Returns the opposite Bool of the pin."""
        if self.get_pin():
            return 0
        else:
            return 1


# Extra gates
class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a ==1 and b==1:
            return 0
        elif (a ==0 and b==1) or (a==1 and b==0):
            return 1
        else:
            return 0


class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        return NotGate(OrGate(self))


class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        return NotGate(AndGate(self))

            