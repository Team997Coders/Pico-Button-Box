import digitalio

class led:
    def __init__(self, pin): #pin must be board.GP##
        self.led = digitalio.DigitalInOut(pin)
        self.led = digitalio.Direction.OUTPUT
        
    def on(self):
        self.led.value = True
        
    def off(self):
        self.led.value = False