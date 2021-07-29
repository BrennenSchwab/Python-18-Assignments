"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ """
        self.start = self.num = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start +1}>" 
        """tried using self.num not self.start +1, but kept returning start val """

    def generate(self):
        """ when called, this will generate the number you passed through in SerialGenerator
        and every sebsequent time its called it will ad one to the previous number
        """
        self.num = self.num + 1
        return self.num -1
        
    def reset(self):
        """ will reset the start number back to the original; calling serial.generate() will 
        start the number from the beginning
        """
        self.num = self.start

