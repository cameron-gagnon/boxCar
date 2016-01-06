#! /usr/bin/python3

import RPi.GPIO as gpio
import time
import Tkinter as tk

# pins
TRIG = 18
ECHO = 3
L_WHEEL_P = 16
L_WHEEL_N = 12
R_WHEEL_P = 10
R_WHEEL_N = 8

STOP_DISTANCE = 20

def main():
    main_init()

def car(event):
    pin_init()
    direction = event.char.lower()
    st = 0.030 # sleep time
    rt = 0.500 # reverse time 

    try:
        if direction == 'w':
            forward(st)
        elif direction == 'a':
            turn_left(st)
        elif direction == 's':
            reverse(st)
        elif direction == 'd':
            turn_right(st)
        elif direction == 'q':
            pivot_left(st)
        elif direction == 'e':
            pivt_right(st)
        else:
            gpio.cleanup()
            break
        
        # get the distance from an object to the front of our car
        curDist = ping()
        
        # if our distance from an object to the front of the
        # car is too short then we make the car reverse for half a
        # second.
        if curDist < STOP_DISTANCE:
            reverse(rt)
            
            
    except KeyboardInterrupt:
        gpio.cleanup()
        break

def main_init():
    command = tk.Tk()
    command.bind('<KeyPress>', car)
    command.mainloop()

def pin_init():
    gpio.setmode(gpio.BOARD)
    # ultrasonic sensor pins
    gpio.setup(TRIG, gpio.OUT)
    gpio.setup(ECHO, gpio.IN)    
    #gpio.output(TRIG, False)

    # motor pins
    gpio.setup(L_WHEEL_P, gpio.OUT)
    gpio.setup(L_WHEEL_N, gpio.OUT)
    gpio.setup(R_WHEEL_P, gpio.OUT)
    gpio.setup(R_WHEEL_N, gpio.OUT)


# moves the car foward
def forward():
    gpio.output(L_WHEEL_P, False)
    gpio.output(L_WHEEL_N, True)
    gpio.output(R_WHEEL_P, False)
    gpio.output(R_WHEEL_N, True)
    time.sleep(3)
    gpio.cleanup()

def ping():
    # pin_initializes the ultrasonic distance
    # sensor to begin its ping program
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)

    # gets the last time that our echo was low
    # basically just before it goes high
    while gpio.input(ECHO) == 0:
        pulse_start = time.time()

    # tells us the latest time our echo pulse
    # was high
    while gpio.input(ECHO) == 1:
        pulse_stop = time.time()

    # stop the signals
    gpio.cleanup()

def pivot_left(tf):
    print("Pivot left")
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(33, True)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    print("Pivot right")
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    print("Turning right")
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    print("Turning left")
    gpio.output(29, False)
    gpio.output(31, False)
    gpio.output(33, True)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()
    
    # get length of the pulse
    pulse_length = pulse_stop - pulse_start

    # 34300 = Dist/ (time/ 2) simplifies to
    # 17150 = dist / time
    # 17150 * time = distance
    distance = pulse_length * 17150

    # round the distance in cm
    distance = round(distance, 2)
    
    return distance

   
    
    #print("Letting sensor settle")
    #time.sleep(2)

if __name__ == "__main__":
    main()
