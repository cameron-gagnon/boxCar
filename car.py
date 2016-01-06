#! /usr/bin/python3.4
import RPi.GPIO as gpio
import time
import Tkinter as tk

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
    gpio.setup(29, gpio.OUT)
    gpio.setup(31, gpio.OUT)
    gpio.setup(33, gpio.OUT)
    gpio.setup(35, gpio.OUT)

def forward(tf):
    print("Moving foward")
    init()
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(33, True)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    print("Moving backward")
    init()
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(33, False)
    gpio.output(35, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    print("Pivot left")
    init()
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(33, True)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    print("Pivot right")
    init()
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    print("Turning right")
    init()
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    print("Turning left")
    init()
    gpio.output(29, False)
    gpio.output(31, False)
    gpio.output(33, True)
    gpio.output(35, False)
    time.sleep(tf)
    gpio.cleanup()

if __name__ == "__main__":
    main()
