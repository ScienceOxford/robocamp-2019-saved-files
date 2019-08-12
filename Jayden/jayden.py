from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll('happy')
    if button_b.was_pressed():
        display.show(Image.SURPRISED)
