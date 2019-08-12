from microbit import *
while True:
    if button_a.was_pressed():
        display.scroll('Hello im Harry')
    if button_b.was_pressed():
        display.show(Image.GIRAFFE)
    sleep(1000)
