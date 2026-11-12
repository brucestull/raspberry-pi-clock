# ===============================================================================
#
# ===============================================================================

from time import sleep

import draw

# ===============================================================================

from time import strftime, localtime

TimeDelay = .001
TimeDelaySmall = .001
TimeDisplay = .005

while True:
    tyme = strftime("%X", localtime())
    tyme = tyme.split(":")

#    print(tyme)

    for t in range(len(tyme)):
        tyme[t] = int(tyme[t])

#    print(tyme)

    H = tyme[0]
    M = tyme[1]

    tymeH = int(H/10)
    tymeh = H%10

    tymeM = int(M/10)
    tymem = M%10

    Tyme = [ tymeH, tymeh, ".", tymeM, tymem ]

#    print(Tyme)

    draw.DisplayClear()

    sleep(TimeDelay)
    draw.Display(1,tymeH)
    sleep(TimeDisplay)

    draw.Display(2,tymeh)
    sleep(TimeDisplay)

    draw.Display(3,tymeM)
    sleep(TimeDisplay)

    draw.Display(4,tymem)
    sleep(TimeDisplay)
    
# =============================================================================

