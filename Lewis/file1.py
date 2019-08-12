from microbit import *

while True:
    if button_a.is_pressed():

        if accelerometer.was_gesture('down'):
            display.scroll('down')
            display.show(Image.ARROW_S)
            sleep(3000)
            display.clear()

        if accelerometer.was_gesture('left'):
            display.scroll('left')
            display.show(Image.ARROW_W)
            sleep(3000)
            display.clear()

        if accelerometer.was_gesture('right'):
            display.scroll('right')
            display.show(Image.ARROW_E)
            sleep(3000)
            display.clear()
