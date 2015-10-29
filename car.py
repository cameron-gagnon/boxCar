#! /usr/bin/python3.4
import RPi.GPIO as gpio
import time

def main():
    init()
    car()

def car():

    while True:
    
        try:
            direction = input("Enter direction ")
            if direction == 'f':
                forward(2)
            elif direction == 'r':
                reverse(2)
                
            elif direction == 'q':
                break 
    
        except KeyboardInterrupt:
            break


def init():
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

if __name__ == "__main__":
    main()
