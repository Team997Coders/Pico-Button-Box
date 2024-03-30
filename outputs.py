#import digitalio ##currently unneccessary
import pwmio
import extramath

class led:
    def __init__(self, pin): #pin must be board.GP##
        self.led = pwmio.PWMOut(pin, frequency=1000)
    
    def value(self, value: bool): #confirmed as working
        if value:
            self.on()
        else:
            self.off()
        
    def on(self): #confirmed as working
        self.led.duty_cycle = 65535
        
    def off(self): #confirmed as working
        self.led.duty_cycle = 0
    
    def duty(self, duty: int): #confirmed as working. have not tested unnacceptable values
        try:
            self.led.duty_cycle = duty
        except:
            print("invalid duty cycle")
    
    def percent(self, percent): #confirmed as working. have not tested unnacceptable values
        try:
            self.led.duty_cycle = round(extramath.Map(percent, 0, 100, 0, 65535))
        except:
            print("invalid duty cycle")