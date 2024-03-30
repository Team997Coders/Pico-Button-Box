import inputs, outputs
import board
import time

board_led = outputs.led(board.LED)

while True:
    for i in range(0, 100, 1):
        board_led.percent(i)
        time.sleep(0.001)
    for i in range (100, 0, -1):
        board_led.percent(i)
        time.sleep(0.001)