import digitalio
import analogio
import extramath

class sw:
    def __init__(self, pin): #pin must be board.GP##
        self.sw = digitalio.DigitalInOut(pin)
        self.sw.switch_to_input(pull=digitalio.Pull.DOWN)
        
    def read(self):
        return self.sw.value
    
class pot:
    def __init__(self, pin): #pin must be board.GP##
        self.pot = analogio.AnalogIn(pin)
        
    def read_u16(self):
        return self.pot.value
    
    def percent(self):
        return extramath.Map(self.pot.value, 0, 65535, 0, 100)
    
    def unitInterval(self):
        return self.pot.value / 65535
    
    def joy(self):
        return (self.pot.value / 32767.5) - 1