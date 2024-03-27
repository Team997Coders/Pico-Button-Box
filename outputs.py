from machine import Pin, PWM
import neopixel

import extramath

class led:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        
    def on(self):
        try:
            PWM.deinit(self.led)
        except:
            print("led already not PWM object")
        self.led.value(1)
        
    def off(self):
        try:
            PWM.deinit(self.led)
        except:
            print("led already not PWM object")
        self.led.value(0)
        
    def toggle(self):
        try:
            PWM.deinit(self.led)
        except:
            print("led already not PWM object")
        self.led.toggle()
    
    def brightness(self, percent):
        try:
            self.led = PWM(self.led)
            self.led.freq(16000)
        except:
            print("led already PWM object")
        
        self.led.duty_u16(extramath.Map(percent, 0, 100, 0, 65535))
        
class neopixel:
    def __init__(self, pin, len):
        self.neopixel = neopixel.NeoPixel(Pin(pin), len)
        
    def fill(self, rgb):
        self.neopixel.fill(rgb)
        self.neopixel.write()
        
    def set(self, index, rgb):
        self.neopixel.__setitem__(index, rgb)
        self.neopixel.write()