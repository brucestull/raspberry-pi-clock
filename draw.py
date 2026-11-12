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

import Segments		# Import 'Segments' and 'Digits' modules
import Digits		# These provide pin to segment/digit mapping

# ===============================================================================

for segment in Segments.segments:	# Set both 'segment' and 'digit' pins as GPIO.OUT.
    GPIO.setup(segment,GPIO.OUT)	# Only need to do this once.
for digit in Digits.digits:		# Used to do this multiple times with each:
    GPIO.setup(digit,GPIO.OUT)		# 'def Zero()' etc

# ===============================================================================

def DisplayClear():	# Reset display by making input Lo and output Hi. No segments display.
    for segment in Segments.segments:
        GPIO.output(segment,False)
    for digit in Digits.digits:
        GPIO.output(digit,True)

# ===============================================================================
# ToDo: Is there a way to loop and compact 'Segments' and 'Digits' sections?
# ===============================================================================

# ===============================================================================
# 'Segments' loop

def Decimal():
    for segment in Segments.Decimal:
        GPIO.output(segment,True)

def Zero():
    for segment in Segments.Zero:
        GPIO.output(segment,True)

def One():
    for segment in Segments.One:
        GPIO.output(segment,True)

def Two():
    for segment in Segments.Two:
        GPIO.output(segment,True)

def Three():
    for segment in Segments.Three:
        GPIO.output(segment,True)

def Four():
    for segment in Segments.Four:
        GPIO.output(segment,True)

def Five():
    for segment in Segments.Five:
        GPIO.output(segment,True)

def Six():
    for segment in Segments.Six:
        GPIO.output(segment,True)

def Seven():
    for segment in Segments.Seven:
        GPIO.output(segment,True)

def Eight():
    for segment in Segments.Eight:
        GPIO.output(segment,True)

def Nine():
    for segment in Segments.Nine:
        GPIO.output(segment,True)

# ===============================================================================
# 'Digits' loop

def PlaceOne():
    for digit in Digits.One:
        GPIO.output(digit,False)

def PlaceTwo():
    for digit in Digits.Two:
        GPIO.output(digit,False)

def PlaceThree():
    for digit in Digits.Three:
        GPIO.output(digit,False)

def PlaceFour():
    for digit in Digits.Four:
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
