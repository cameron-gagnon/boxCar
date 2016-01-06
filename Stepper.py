#! /usr/bin/python3
import RPi.GPIO as gpio
import time
start_time = time.time()

class Stepper:
    
    def __init__(self, number_of_steps, motor_pin_1,
                 motor_pin_2, motor_pin_3, motor_pin_4):
        self.step_number = 0;
        self.speed = 0;
        self.direction = 0;
        self.last_step_time = 0;
        self.number_of_steps = number_of_steps;

        self.motor_pin_1 = motor_pin_1
        self.motor_pin_2 = motor_pin_2
        self.motor_pin_3 = motor_pin_3
        self.motor_pin_4 = motor_pin_4

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.motor_pin_1, gpio.OUT)
        gpio.setup(self.motor_pin_2, gpio.OUT)
        gpio.setup(self.motor_pin_3, gpio.OUT)
        gpio.setup(self.motor_pin_4, gpio.OUT)

        self.pin_count = 4;

    def setSpeed(self, whatSpeed):
        self.step_delay = 60 / self.number_of_steps / whatSpeed;

    def step(self, steps_to_move):
        # number of steps to take
        steps_left = abs(steps_to_move)
        
        # direction of motor depending on + or - steps
        if (steps_to_move > 0):
            self.direction = 1
        if (steps_to_move < 0):
            self.direction = 0

        while (steps_left > 0):
            
            if (millis() - self.last_step_time >= self.step_delay):
               
                self.last_step_time = millis();
                
                if (self.direction == 1):
                    self.step_number += 1
                    
                    if (self.step_number == self.number_of_steps):
                        self.step_number = 0

                else:
                    if (self.step_number == 0):
                        self.step_number = self.number_of_steps

                    self.step_number -= 1 
            
                steps_left -= 1

                self.stepMotor(self.step_number % 4)

    def stepMotor(self, thisStep):
        if (self.pin_count == 2):
            if (thisStep == 0):
                gpio.output(self.motor_pin_1, False)
                gpio.output(self.motor_pin_2, True)
            elif (thisStep == 1):
                gpio.output(self.motor_pin_1, True)
                gpio.output(self.motor_pin_2, True)
            elif (thisStep == 2):
                gpio.output(self.motor_pin_1, True)
                gpio.output(self.motor_pin_2, False)
            elif (thisStep == 3):
                gpio.output(self.motor_pin_1, False)
                gpio.output(self.motor_pin_2, False)

        elif (self.pin_count == 4):
            if (thisStep == 0):
                gpio.output(self.motor_pin_1, True)
                gpio.output(self.motor_pin_2, False)
                gpio.output(self.motor_pin_3, True)
                gpio.output(self.motor_pin_4, False)
            elif (thisStep == 1):
                gpio.output(self.motor_pin_1, False)
                gpio.output(self.motor_pin_2, True)
                gpio.output(self.motor_pin_3, True)
                gpio.output(self.motor_pin_4, False)
            elif (thisStep == 2):
                gpio.output(self.motor_pin_1, False)
                gpio.output(self.motor_pin_2, True)
                gpio.output(self.motor_pin_3, False)
                gpio.output(self.motor_pin_4, True)
            elif (thisStep == 3):
                gpio.output(self.motor_pin_1, True)
                gpio.output(self.motor_pin_2, False)
                gpio.output(self.motor_pin_3, False)
                gpio.output(self.motor_pin_4, True)
def millis():
   return time.time() - start_time
