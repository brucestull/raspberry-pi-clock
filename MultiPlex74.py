# ===============================================================================
#
# ===============================================================================

from time import sleep

import draw		# Don't need to import 'segment_pins' and 'digit_pins'.
			# 'draw' already imported them.

time_lapse = .25
time_display = .007
time_delay = .001

# ===============================================================================

for i in range(10):
    draw.display(1,i)
    sleep(time_lapse)
draw.display_clear()
