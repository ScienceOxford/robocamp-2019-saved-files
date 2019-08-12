from microbit import*

while True:
    if button_a.was_pressed():
        display.scroll('Divya.')
    if accelerometer.was_gesture('up'):
        display.show(Image.COW)
        sleep(1000)
    if accelerometer.was_gesture('down'):
        display.show(Image.PACMAN)
        sleep(1000)
    if button_b.was_pressed():
        display.scroll('R')
