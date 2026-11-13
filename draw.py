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

def display_clear():	# Reset display by making input Lo and output Hi. No segments display.
    for segment in segment_pins.segments:
        GPIO.output(segment,False)
    for digit in digit_pins.digits:
        GPIO.output(digit,True)

# ===============================================================================
# ToDo: Is there a way to loop and compact 'segment_pins' and 'digit_pins' sections?
# ===============================================================================

# ===============================================================================
# 'segment_pins' loop

def decimal():
    for segment in segment_pins.decimal:
        GPIO.output(segment,True)

def zero():
    for segment in segment_pins.zero:
        GPIO.output(segment,True)

def one():
    for segment in segment_pins.one:
        GPIO.output(segment,True)

def two():
    for segment in segment_pins.two:
        GPIO.output(segment,True)

def three():
    for segment in segment_pins.three:
        GPIO.output(segment,True)

def four():
    for segment in segment_pins.four:
        GPIO.output(segment,True)

def five():
    for segment in segment_pins.five:
        GPIO.output(segment,True)

def six():
    for segment in segment_pins.six:
        GPIO.output(segment,True)

def seven():
    for segment in segment_pins.seven:
        GPIO.output(segment,True)

def eight():
    for segment in segment_pins.eight:
        GPIO.output(segment,True)

def nine():
    for segment in segment_pins.nine:
        GPIO.output(segment,True)

# ===============================================================================
# 'digit_pins' loop

def place_one():
    for digit in digit_pins.one:
        GPIO.output(digit,False)

def place_two():
    for digit in digit_pins.two:
        GPIO.output(digit,False)

def place_three():
    for digit in digit_pins.three:
        GPIO.output(digit,False)

def place_four():
    for digit in digit_pins.four:
        GPIO.output(digit,False)

# ===============================================================================
# Loop to map symbol-numbers to word-numbers.

def display(position,number):
    display_clear()
    if number == 0:
        zero()
    if number == 1:
        one()
    if number == 2:
        two()
    if number == 3:
        three()
    if number == 4:
        four()
    if number == 5:
        five()
    if number == 6:
        six()
    if number == 7:
        seven()
    if number == 8:
        eight()
    if number == 9:
        nine()

    if position == 1:
        place_one()
    if position == 2:
        place_two()
    if position == 3:
        place_three()
    if position == 4:
        place_four()

# ===============================================================================
#
# ===============================================================================
