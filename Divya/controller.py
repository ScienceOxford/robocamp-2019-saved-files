from microbit import *
import radio

radio.config(channel=14, group=99, queue=1)
radio.on()

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
INPUTS
joystick:bit
'''
buttons = {2: 'A',
           516: 'B',
           684: 'C',
           768: 'D',
           853: 'E',
           819: 'F'}

def button_press():
    press = pin2.read_analog()
    if press < 900:
        for number in range(press-5, press+5):
            if number in buttons:
                return buttons[number]

def joystick_push():
    x = pin0.read_analog() -513
    y = pin1.read_analog() -523
    left = int((y+x)*1.18)
    right = int((y-x)*1.18)
    return left, right

while True:
    joystick = joystick_push()
    message = str(joystick[0]) + " " + str(joystick[1])
    print(message)
    radio.send(message)
    sleep(10)
