import digitalio
import pwmio
import extramath

class led:
    def __init__(self, pin): #pin must be board.GP##
        self.led = pwmio.PWMOut(pin, frequency=1000)
        
    def on(self):
        self.led.duty_cycle = 65535
        
    def off(self):
        self.led.duty_cycle = 0
    
    def duty(self, duty):
        self.led.duty_cycle = duty
    
    def percent(self, percent):
        self.led.duty_cycle = extramath.Map(percent, 0, 100, 0, 65535)