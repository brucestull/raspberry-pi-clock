# ===============================================================================
#
# ===============================================================================

from time import sleep

import draw		# Don't need to import 'segment_pins' and 'digit_pins'.
			# 'draw' already imported them.

timelapse = .25
timedisplay = .007
timedelay = .001

# ===============================================================================

for i in range(10):
    draw.Display(1,i)
    sleep(timelapse)
draw.DisplayClear()
