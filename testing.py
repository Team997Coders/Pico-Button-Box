import inputs, outputs
import board
import time

board_led = outputs.led(board.LED)

while True:
    board_led.on()
    time.sleep(0.2)
    board_led.off()
    time.sleep(0.2)