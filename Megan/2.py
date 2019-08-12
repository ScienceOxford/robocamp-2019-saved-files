from microbit import*
Water = 0
food = 0
WL = 6
FL = 8
while True:
    if button_a.was_pressed():
        Water = Water + 1
    if button_a.was_pressed():
        food = food + 1
    if food == FL and Water == WL:
        display.show(Image.HAPPY)
    else:
        display.show(Image.Sad)
