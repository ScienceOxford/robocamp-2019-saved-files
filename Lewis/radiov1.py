from microbit import *
import radio

radio.on()
radio.config(group=2)

if button_a.was_pressed():
        radio.send("hi")

elif button_b.was_pressed():
        message = radio.receive()
        display.scroll(str(message))
