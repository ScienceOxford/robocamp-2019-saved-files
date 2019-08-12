from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
MOTOR CONTROL
Code for microbit with e.g. L9110s motor driver
With thanks to: http://www.multiwingspan.co.uk/micro.php?page=botline
'''
LF = pin8
LB = pin2
RF = pin0
RB = pin1

# 0 turns the motors off; 1023 turns them on at full speed
def stop():
    LF.write_analog(0)
    LB.write_analog(0)
    RF.write_analog(0)
    RB.write_analog(0)
    display.clear()

# Inputs between 0-1023 to control both motors
def drive(L, R):
    # Below is an adjustment to correct for motor speed discrepancy
    L = int(L*1)
    R = int(R*1)
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        LF.write_analog(abs(L))    # go forwards at speed given
        LB.write_analog(0)         # don't go backwards
    elif L < 0 and L >= -1023:
        LF.write_analog(0)         # don't go forwards
        LB.write_analog(abs(L))    # go backwards at speed given
    else:
        LF.write_analog(0)         # stop the left wheel
        LB.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        RF.write_analog(abs(R))    # go forwards at speed given
        RB.write_analog(0)         # don't go backwards
    elif R < 0 and R >= -1023:
        RF.write_analog(0)         # don't go forwards
        RB.write_analog(abs(R))    # go backwards at speed given
    else:
        RF.write_analog(0)         # stop the right wheel
        RB.write_analog(0)


'''
MAIN LOOP
'''
while True:
    if button_a.was_pressed():
        drive(1023, 1023)
