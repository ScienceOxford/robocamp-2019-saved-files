from microbit import *
import radio
radio.config(channel=11, group=14, queue=1)
radio.on()

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
    x = pin0.read_analog() -527
    y = pin1.read_analog() -524
    left = int((y+x)*1.19)
    right = int((y-x)*1.19)
    return left, right


while True:
    joystick = joystick_push()
    message = str(joystick[0]) + " " + str(joystick[1])
    radio.send(message)
    print(message)
    sleep(10)
