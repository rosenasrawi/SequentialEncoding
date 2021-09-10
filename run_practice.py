#from psychopy import core, event
import random

""" Import other task scripts """

from task_functions import *

""" Run Practice"""

random.shuffle(dialTypesPractice)           # Random order dial up & right

for dial in range(len(dialTypesPractice)):
    dialType = dialTypesPractice[dial]
    presentPrecueDial(dialType, targetColors = [])

    random.shuffle(loadTypesPractice)       # For this dial, random order load one & two

    for load in range(len(loadTypesPractice)):
        loadType = loadTypesPractice[load]
        targetColors, nonTargetColors = determineBlockSpecifics(loadType)
        presentPrecueLoad(targetColors,loadType)
        
        practice = False    # turn of practice dial

        random.shuffle(trialTypesPractice)       # For this load random order of the trialtypes 0-7
        performanceBlock = []

        for trial in range(len(trialTypesPractice)):
            targetColors, nonTargetColors = determineTrialSpecifics(trialTypesPractice[trial], loadType, targetColors, nonTargetColors)
            presentStim()
            clockwise, count = presentResponse(loadType, dialType, practice, targetColors)
            performance = presentTrialFeedback(count, clockwise, dialType)

            performanceBlock.append(performance)

        presentBlockFeedback(performanceBlock) # show block feedback