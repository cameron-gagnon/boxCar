#! /usr/bin/python3
import RPi.GPIO as gpio
import time
import Stepper

STEPS_PER_REV = 200;
RPM = 110 # speed 

def main():
    myStepper = init()
    car(myStepper)

def car(myStepper):

    while True:
    
        try:
            direction = input("Enter direction ")
            if direction == 'f':
                print("Forward")
                myStepper.step(STEPS_PER_REV)
            elif direction == 'r':
                myStepper.step(-STEPS_PER_REV)
                print("Backward")
            elif direction == 'q':
                print("Quit")
                gpio.cleanup()
                break 
    
        except KeyboardInterrupt:
            gpio.cleanup()
            break


def init():
    gpio.setmode(gpio.BOARD)
    myStepper = Stepper.Stepper(STEPS_PER_REV, 8, 10, 16, 18)
    myStepper.setSpeed(RPM)
    return myStepper

if __name__ == "__main__":
    main()
