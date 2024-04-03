import digitalio
import analogio
import extramath

class sw: #confirmed as fully working
    def __init__(self, pin): #pin must be board.GP##
        self.sw = digitalio.DigitalInOut(pin)
        self.sw.switch_to_input(pull=digitalio.Pull.DOWN)
        
    def read(self):
        return self.sw.value
    
class pot: #IN TESTING PROCESS - NONFUNCTIONAL
    def __init__(self, pin): #pin must be board.GP##
        self.pot = analogio.AnalogIn(pin)
        
    def read_u16(self): #confirmed as working
        return self.pot.value
    
    def percent(self, rounding=False): #confirmed as working
        self.value = extramath.Map(self.pot.value, 0, 65535, 0, 100)
        
        if rounding:
            self.value = round(self.value)
            
        return self.value
    
    def unitInterval(self): #confirmed as working
        return self.pot.value / 65535
    
    def joy(self): #confirmed as working
        return (self.pot.value / 32767.5) - 1