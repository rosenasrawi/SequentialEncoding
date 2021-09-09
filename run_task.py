""" Import packages"""

#from psychopy import core, event
import random

""" Import other task scripts """

from task_functions import *

""" Run task """

random.shuffle(blockTypes)

for block in range(len(loads)):

    blockType = blockTypes[block]

    dial = dials[blockType]
    presentPrecueDial(dial, targetColors = [])
    
    load = loads[blockType]
    targetColors, nonTargetColors = determineBlockSpecifics(load)
    presentPrecueLoad(targetColors,load)

    practice = False
    
    for trial in range(len(trialTypes)):
        targetColors, nonTargetColors = determineTrialSpecifics(trial, load, targetColors, nonTargetColors)

        presentStim()
        clockwise, count = presentResponse(load, dial, practice, targetColors)
        presentTrialFeedback(count, clockwise, dial)

