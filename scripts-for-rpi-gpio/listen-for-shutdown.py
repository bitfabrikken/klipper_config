#!/usr/bin/env python

import subprocess
import time
import RPi.GPIO as GPIO

PIN = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    print "Pressed"
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(PIN) == GPIO.LOW:
        time.sleep(0.01)
    length = time.time() - start
    print length

    if length > 1:
        print "Long Press"
        subprocess.call(['shutdown', '-h', 'now'], shell=False)

    else:
        print "Short Press"



#GPIO.setmode(GPIO.BCM)
#GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(3, GPIO.FALLING)


#print("shutdown button pressed")

#subprocess.call(['shutdown', '-h', 'now'], shell=False)
