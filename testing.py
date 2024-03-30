import inputs, outputs
import board
import time

board_led = outputs.led(board.LED)
button = inputs.sw(board.GP15)

while True:
    board_led.value(button.read())
    time.sleep(0.1)