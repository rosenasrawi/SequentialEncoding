""" Import packages"""

#from psychopy import core, event
import random

""" Import other task scripts """

from task_functions import *

""" Run Task """

random.shuffle(dialTypesTask)           # Random order dial up & right

for dial in range(len(dialTypesTask)):
    dialType = dialTypesTask[dial]
    presentPrecueDial(dialType, targetColors = [])

    random.shuffle(loadTypesTask)       # For this dial, random order load one & two

    for load in range(len(loadTypesTask)):
        loadType = loadTypesTask[load]
        targetColors, nonTargetColors = determineBlockSpecifics(loadType)
        presentPrecueLoad(targetColors,loadType)
        
        practice = False    # turn of practice dial

        random.shuffle(trialTypesTask)       # For this load random order of the trialtypes 0-7
        performanceBlock = []

        for trial in range(len(trialTypesTask)):
            targetColors, nonTargetColors = determineTrialSpecifics(trialTypesTask[trial], loadType, targetColors, nonTargetColors)
            presentStim()
            clockwise, count = presentResponse(loadType, dialType, practice, targetColors)

            performance = presentTrialFeedback(count, clockwise, dialType)
            performanceBlock.append(performance)

        presentBlockFeedback(performanceBlock) # show block feedback      

""" Run task """

#random.shuffle(blockTypes)

#for block in range(len(loads)):

#    blockType = blockTypes[block]

#    dial = dials[blockType]
#    presentPrecueDial(dial, targetColors = [])
    
#    load = loads[blockType]
#    targetColors, nonTargetColors = determineBlockSpecifics(load)
#    presentPrecueLoad(targetColors,load)

#    practice = False
    
#    for trial in range(len(trialTypes)):
#        targetColors, nonTargetColors = determineTrialSpecifics(trial, load, targetColors, nonTargetColors)

#        presentStim()
#        clockwise, count = presentResponse(load, dial, practice, targetColors)
#        presentTrialFeedback(count, clockwise, dial)
