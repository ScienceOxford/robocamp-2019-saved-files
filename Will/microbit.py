from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll("I'm Will")
    if accelerometer.was_gesture("up"):
        display.show(Image.DIAMOND_SMALL)
        sleep(500)
        display.show(Image.DIAMOND)
        sleep(500)
        display.show(Image.DIAMOND_SMALL)
        sleep(500)
        display.show(Image.DIAMOND)
        sleep(500)
        display.show(Image.DIAMOND_SMALL)
        sleep(500)
        display.show(Image.DIAMOND)
        sleep(500)
    if accelerometer.was_gesture("shake"):
        sleep(500)
        display.scroll("Hello")
    if button_b.was_pressed():
        display.show(Image.HAPPY)
        sleep(1000)
    if accelerometer.was_gesture("down"):
        display.scroll("Good bye")
