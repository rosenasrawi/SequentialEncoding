""" Import packages"""

import random

""" Import other task scripts """

from task_functions import *

""" Run Practice"""

numBlocks = len(dialTypesPractice) * len(loadTypesPractice)
thisNumBlock = 0

random.shuffle(dialTypesPractice)           # Random order dial up & right

for dial in range(len(dialTypesPractice)):
    #eyetrackingCalibration(triggerSend)

    dialType = dialTypesPractice[dial]
    presentPrecueDial(dialType, targetColors = [])

    random.shuffle(loadTypesPractice)       # For this dial, random order load one & two

    for load in range(len(loadTypesPractice)):
        thisNumBlock += 1

        loadType = loadTypesPractice[load]
        targetColors, nonTargetColors = determineBlockSpecifics(loadType)
        presentPrecueLoad(targetColors,loadType)
        
        random.shuffle(trialTypesPractice)       # For this load random order of the trialtypes 0-7
        performanceBlock = []

        for trial in range(len(trialTypesPractice)):
            trialType = trialTypesPractice[trial]
            targetColors, nonTargetColors, targetMoment, targetLocation, targetTilt = determineTrialSpecifics(trialType, loadType, targetColors, nonTargetColors)
            presentStim(triggerSend, trialType, loadType, dialType)
            
            clockwise, count, probeTime, pressTime, releaseTime, triggerProbe, triggerResponse = presentResponse(loadType, dialType, targetColors)
            reportOri, targetOri, difference, performance = presentTrialFeedback(count, clockwise, dialType)

            performanceBlock.append(performance)

        presentBlockFeedback(performanceBlock, numBlocks, thisNumBlock) # show block feedback