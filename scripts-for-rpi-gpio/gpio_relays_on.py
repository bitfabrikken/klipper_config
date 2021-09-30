#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
# import sys, getopt

quit()


psu_pin = 11
ssr_pin = 13

# GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin, GPIO.OUT)
GPIO.setup(psu_pin, GPIO.OUT)

OFF = True  #True = OFF, False = ON
ON = False  #True = OFF, False = ON



GPIO.output(psu_pin, ON)
GPIO.output(ssr_pin, ON)

print("GPIO relays on PINS 11+13 turned ON")

# GPIO.cleanup()

# OPEN = False

# time.sleep(1)

# try:
#     while True:

#         if not OPEN:
#             GPIO.output(psu_pin, ON)
#             GPIO.output(ssr_pin, ON)
#             OPEN = True
#             print("SSR + PSU relay switched to ON")
        
#         print("Sleeping 10 secs in loop")
#         time.sleep(10)
          


# except KeyboardInterrupt:
#     # GPIO.output(psu_pin, OFF)
#     # GPIO.output(ssr_pin, OFF)
