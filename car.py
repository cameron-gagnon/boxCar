#! /usr/bin/python3

import RPi.GPIO as gpio
import time
import threading

TRIG = 18
ECHO = 3

L_WHEEL_P = 16
L_WHEEL_N = 12
R_WHEEL_P = 10
R_WHEEL_N = 8

def main():
    init()
    distance = ping()
    print(distance)
    car()

def car():
    while True:
    
        try:
            direction = input("Enter direction ")
            if direction == 'w':
                forward()
            elif direction == 'a':
                pass
            elif direction == 's':
                pass
            elif direction == 'd':
                pass
            elif direction == 'q':
                print("Quit")
                gpio.cleanup()
                break 
            time.sleep(1)

        except KeyboardInterrupt:
            gpio.cleanup()
            break

# moves the car foward
def forward():
    init()
    gpio.output(L_WHEEL_P, False)
    gpio.output(L_WHEEL_N, True)
    gpio.output(R_WHEEL_P, False)
    gpio.output(R_WHEEL_N, True)
    time.sleep(3)
    gpio.cleanup()

def ping():
    # initializes the ultrasonic distance
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

    # get length of the pulse
    pulse_length = pulse_stop - pulse_start

    # 34300 = Dist/ (time/ 2) simplifies to
    # 17150 = dist / time
    # 17150 * time = distance
    distance = pulse_length * 17150

    # round the distance in cm
    distance = round(distance, 2)
    
    return distance

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(TRIG, gpio.OUT)
    gpio.setup(ECHO, gpio.IN)    
    gpio.output(TRIG, False)
    
    gpio.setup(L_WHEEL_P, gpio.OUT)
    gpio.setup(L_WHEEL_N, gpio.OUT)
    gpio.setup(R_WHEEL_P, gpio.OUT)
    gpio.setup(R_WHEEL_N, gpio.OUT)

    
    #print("Letting sensor settle")
    #time.sleep(2)

if __name__ == "__main__":
    main()
