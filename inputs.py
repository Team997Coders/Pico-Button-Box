from machine import Pin, ADC
import thread

import extramath

class sw:
    def __init__(self, pin):
        self.sw = Pin(pin, Pin.IN, Pin.PULL_DOWN)
    
    def get_value(self): #might be better as lambda?
        return self.sw.value()
    
class pot:
    def __init__(self, pin):
        self.pot = ADC(pin)
        
    def read_u16(self): #might be better as lambda?
        return self.pot.read_u16()
    
    def read_percent(self): #might be better as lambda?
        return extramath.Map(self.pot.read_u16(), 0, 65535, 0, 100)
    
    def read(self): #might be better as lambda?
        return self.pot.read_u16() / 65535
    
    def read_joy(self): #might be better as lambda?
        return (self.pot.read_u16() / 32,767.5) - 1