import digitalio
import analogio
import extramath as umath

class sw: #confirmed as fully working
    def __init__(self, pin): #pin must be board.GP##
        self.sw = digitalio.DigitalInOut(pin)
        self.sw.switch_to_input(pull=digitalio.Pull.DOWN)
        
    def read(self):
        return self.sw.value
    
class pot: #IN TESTING PROCESS - NONFUNCTIONAL
    def __init__(self, pin, trim_min=0, trim_max=65535): #pin must be board.GP##
        self.trim_min = trim_min
        self.trim_max = trim_max
        
        self.pot = analogio.AnalogIn(pin)
        
        self.applyTrim = lambda inputVal: umath.Map(inputVal, self.trim_min, self.trim_max, 0, 65535)
        self.clamp_u16 = lambda inputVal: umath.clamp(inputVal, 0, 65535)
        
    def read_u16(self): 
        return self.clamp_u16(self.applyTrim(self.pot.value))
    
    def percent(self, rounding=False): 
        self.value = umath.clamp(umath.Map(self.pot.value, self.trim_min, self.trim_max, 0, 100), 0, 100)
        
        if rounding:
            self.value = round(self.value)
            
        return self.value
    
    def unitInterval(self): 
        return umath.clamp(umath.Map(self.pot.value, self.trim_min, self.trim_max, 0, 1), 0, 1)
    
    def joy(self): 
        return umath.clamp(umath.Map(self.pot.value, self.trim_min, self.trim_max, 0, 2) - 1, -1, 1)