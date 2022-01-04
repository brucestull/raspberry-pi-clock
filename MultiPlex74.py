# ===============================================================================
#
# ===============================================================================

from time import sleep

import Draw		# Don't need to import 'Segments' and 'Digits'.
			# 'Draw' already imported them.

timelapse = .25
timedisplay = .007
timedelay = .001

# ===============================================================================

for i in range(10):
    Draw.Display(1,i)
    sleep(timelapse)
Draw.DisplayClear()
