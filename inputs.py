import digitalio

class sw:
    def __init__(self, pin): #pin must be board.GP##
        self.sw = digitalio.DigitalInOut(pin)
        self.sw.switch_to_input(pull=digitalio.Pull.DOWN)
        
    def read(self):
        return self.sw.value