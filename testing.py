import board
import digitalio
import analogio
import usb_hid
import extramath

from hid_gamepad import Gamepad #used alternate import, NEEDS TESTING

gp = Gamepad(usb_hid.devices) #boot.py file needs to be updated??

button_pins = (board.GP00, board.GP01)

gamepad_buttons = (1, 2)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    
ax = analogio.AnalogIn(board.GP26)
ay = analogio.AnalogIn(board.GP27)

while True:
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")
            
    gp.move_joysticks(
        x = extramath.Map(ax.value, 0, 65535, -127, 127),
        y = extramath.Map(ay.value, 0, 65535, -127, 127),
    )
    print(" x", ax.value, "y", ax.value)