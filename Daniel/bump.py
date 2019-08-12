from microbit import *
check = pin12.read_digital()
check = pin13.read_digital()

while True:
    if check == 1:
        drive(200, 200)
        sleep(300)
