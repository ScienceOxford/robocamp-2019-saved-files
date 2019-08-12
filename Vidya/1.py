from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll('HELLO, MY NAME IS VIDYA')
    if accelerometer.was_gesture('up'):
        display.show(Image.COW)
    if button_b.was_pressed():
        display.scroll('I LIKE CODING!!!')
    if accelerometer.was_gesture('down'):
        display.show(Image.GIRAFFE)
        sleep(1000)
