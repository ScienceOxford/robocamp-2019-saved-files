from microbit import *
import radio
radio.config(channel=12,group=3,queue=1)
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
    x = pin0.read_analog() - 531
    y = pin1.read_analog() - 526
    left = y + x
    right = y - x
    return left, right
while True:
    if button == 'F':
        radio.send('hello')
        sleep(500)
    elif button == 'E':
        radio.send('hi')
        sleep(500)
    else:
        message = str(joystick[0]) + " " + str(joystick[1])
        radio.send(message)
        sleep(10)
