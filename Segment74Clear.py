# Learn how to use the 4-digit 7-segment display
# It seems that both Pi pins are set as output, LED input pin set '1' and output pin set '0'
# The "digit" pin goes low and the "segment" pin goes hi to drive the segment

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)		# Set pin mode to BCM
#
GPIO.setwarnings(False)
#
digits = [2,3,4,17]
segments = [16,21,19,6,5,26,20,13]
#
for digit in digits:
    GPIO.setup(digit,GPIO.OUT)		# Set digits to output
for segment in segments:
    GPIO.setup(segment,GPIO.OUT)	# Set segments to output
#
for digit in digits:
    GPIO.output(digit,False)    # Set digits low
for segment in segments:
    GPIO.output(segment,False)  # Set segments low
