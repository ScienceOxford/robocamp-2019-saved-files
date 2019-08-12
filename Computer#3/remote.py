from microbit import *
import radio as r

r.on()
def show(text,ttype="img"):
    if ttype=="text":
        display.scroll(text)
    elif ttype=="img":
        display.show(text)
while True:
    g=accelerometer.current_gesture()
    if button_a.was_pressed():
        r.send("stop")
        show(Image.NO)
        sleep(500)
    elif button_b.was_pressed():
        r.send("get")
        show(Image.YES)
    elif g=="down":
        r.send("forward")
        show(Image.ARROW_N)
    elif g=="up":
        r.send("backward")
        show(Image.ARROW_S)
    elif g=="right":
        r.send("right")
        show(Image.ARROW_E)
    elif g=="left":
        r.send("left")
        show(Image.ARROW_W)
