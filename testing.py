import inputs
import board
import time

potentiometer = inputs.pot(board.GP26, trim_min=530, trim_max=65535)

while True:
    print(potentiometer.joy())
    time.sleep(0.1)