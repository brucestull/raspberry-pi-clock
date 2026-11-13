# ===============================================================================
#
# ===============================================================================

from time import sleep

import draw

# ===============================================================================

from time import strftime, localtime

time_delay = .001
time_delay_small = .001
time_display = .005

while True:
    local_time = strftime("%X", localtime())
    current_time = [int(value) for value in local_time.split(":")]

#    print(current_time)

    H = current_time[0]
    M = current_time[1]

    time_hours_tens = int(H/10)
    time_hours_ones = H%10

    time_minutes_tens = int(M/10)
    time_minutes_ones = M%10

    Tyme = [ time_hours_tens, time_hours_ones, ".", time_minutes_tens, time_minutes_ones ]

#    print(Tyme)

    draw.display_clear()

    sleep(time_delay)
    draw.display(1,time_hours_tens)
    sleep(time_display)

    draw.display(2,time_hours_ones)
    sleep(time_display)

    draw.display(3,time_minutes_tens)
    sleep(time_display)

    draw.display(4,time_minutes_ones)
    sleep(time_display)
    
# =============================================================================

