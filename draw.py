# ===============================================================================
#
# ===============================================================================
# It seems that both Pi pins, per segment, are set as output.
# LED input pin set '1' and output pin set '0'.
# The "digit" pin goes low and the "segment" pin goes hi to drive the segment.

import RPi.GPIO as GPIO		# Import 'RPi.GPIO' module as 'GPIO'.
				# Module contents can be called by 'GPIO.<var>'
				# instead of 'RPi.GPIO.<var>'
GPIO.setmode(GPIO.BCM)          # Set pin mode to BCM
GPIO.setwarnings(False)         # Suppress display of warnings

import segment_pins		# Import 'segment_pins' and 'digit_pins' modules
import digit_pins		# These provide pin to segment/digit mapping

# ===============================================================================

for segment in segment_pins.segments:	# Set both 'segment' and 'digit' pins as GPIO.OUT.
    GPIO.setup(segment,GPIO.OUT)	# Only need to do this once.
for digit in digit_pins.digits:		# Used to do this multiple times with each:
    GPIO.setup(digit,GPIO.OUT)		# 'def Zero()' etc

# ===============================================================================

def DisplayClear():	# Reset display by making input Lo and output Hi. No segments display.
    for segment in segment_pins.segments:
        GPIO.output(segment,False)
    for digit in digit_pins.digits:
        GPIO.output(digit,True)

# ===============================================================================
# ToDo: Is there a way to loop and compact 'segment_pins' and 'digit_pins' sections?
# ===============================================================================

# ===============================================================================
# 'segment_pins' loop

def Decimal():
    for segment in segment_pins.decimal:
        GPIO.output(segment,True)

def Zero():
    for segment in segment_pins.zero:
        GPIO.output(segment,True)

def One():
    for segment in segment_pins.one:
        GPIO.output(segment,True)

def Two():
    for segment in segment_pins.two:
        GPIO.output(segment,True)

def Three():
    for segment in segment_pins.three:
        GPIO.output(segment,True)

def Four():
    for segment in segment_pins.four:
        GPIO.output(segment,True)

def Five():
    for segment in segment_pins.five:
        GPIO.output(segment,True)

def Six():
    for segment in segment_pins.six:
        GPIO.output(segment,True)

def Seven():
    for segment in segment_pins.seven:
        GPIO.output(segment,True)

def Eight():
    for segment in segment_pins.eight:
        GPIO.output(segment,True)

def Nine():
    for segment in segment_pins.Nine:
        GPIO.output(segment,True)

# ===============================================================================
# 'digit_pins' loop

def PlaceOne():
    for digit in digit_pins.One:
        GPIO.output(digit,False)

def PlaceTwo():
    for digit in digit_pins.Two:
        GPIO.output(digit,False)

def PlaceThree():
    for digit in digit_pins.Three:
        GPIO.output(digit,False)

def PlaceFour():
    for digit in digit_pins.Four:
        GPIO.output(digit,False)

# ===============================================================================
# Loop to map symbol-numbers to word-numbers.

def Display(Position,Number):
    DisplayClear()
    if Number == 0:
        Zero()
    if Number == 1:
        One()
    if Number == 2:
        Two()
    if Number == 3:
        Three()
    if Number == 4:
        Four()
    if Number == 5:
        Five()
    if Number == 6:
        Six()
    if Number == 7:
        Seven()
    if Number == 8:
        Eight()
    if Number == 9:
        Nine()

    if Position == 1:
        PlaceOne()
    if Position == 2:
        PlaceTwo()
    if Position == 3:
        PlaceThree()
    if Position == 4:
        PlaceFour()

# ===============================================================================
#
# ===============================================================================
