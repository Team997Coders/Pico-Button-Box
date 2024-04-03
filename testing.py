import inputs
import board
import time

potentiometer = inputs.pot(board.GP26)

while True:
    print(potentiometer.joy())
    time.sleep(0.1)