""" Import packages"""

import random

""" Import other task scripts """

from pp_info_logfile import *

session, subjectID = getInfo()
filename, header = createNewDatafile(session, subjectID)

from task_objects import *
from task_functions import *

""" EEG & Eye-tracker"""

if triggerSend == True:
    from eeg_and_eyetrack import *
    portBioSemi, tracker = activateEEGandEyeTracker(subjectID, session)
    eyeTrackerStart(tracker)
elif triggerSend == False:
    portBioSemi = []; tracker = []

""" Run Task """
numBlocks = len(dialTypesTask) * len(loadTypesTask)
thisNumBlock = 0

random.shuffle(dialTypesTask)           # Random order dial up & right

for dial in range(len(dialTypesTask)):
    #eyetrackingCalibration(triggerSend, portBioSemi, tracker)

    dialType = dialTypesTask[dial]
    presentPrecueDial(dialType, targetColors = [])
    random.shuffle(loadTypesTask)       # For this dial, random order load one & two

    for load in range(len(loadTypesTask)):
        thisNumBlock += 1
        loadType = loadTypesTask[load]

        # Block specs
        targetColors, nonTargetColors = determineBlockSpecifics(loadType)
        presentPrecueLoad(targetColors,loadType)
        
        random.shuffle(trialTypesTask)       # For this load random order of the trialtypes 0-7
        performanceBlock = []

        for trial in range(len(trialTypesTask)):
            # Determine specs
            trialType = trialTypesTask[trial]
            targetColors, nonTargetColors, targetMoment, targetLocation, targetTilt = determineTrialSpecifics(trialType, loadType, targetColors, nonTargetColors)

            # Stimulus and response
            thisFixTime, triggerEnc1, triggerEnc2 = presentStim(triggerSend, trialType, loadType, dialType, portBioSemi, tracker)
            clockwise, count, probeTime, pressTime, releaseTime, triggerProbe, triggerResponse = presentResponse(loadType, dialType, targetColors, portBioSemi, tracker, triggerSend, trialType)

            # Feedback presentation
            reportOri, targetOri, difference, performance = presentTrialFeedback(count, clockwise, dialType)
            performanceBlock.append(performance)

            # For logfile
            if loadType == 0: #load one
                colCued1 = targetColors; colCued2 = []
            elif loadType == 1: #load two
                colCued1 = targetColors[0]; colCued2 = targetColors[1]

            # Create trialdata
            trialData = {'leftBarOri1':         leftBar1.ori,                 
                         'rightBarOri1':        rightBar1.ori,
                         'leftBarCol1':         leftBar1.lineColor, 
                         'rightBarCol1':        rightBar1.lineColor,
                         'leftBarOri2':         leftBar2.ori,                 
                         'rightBarOri2':        rightBar2.ori,
                         'leftBarCol2':         leftBar2.lineColor, 
                         'rightBarCol2':        rightBar2.lineColor,
                         'colCued1':            colCued1, 
                         'colCued2':            colCued2,                     # only if load 2
                         'colProbed':           colCued1,
                         'targetMoment':        targetMoment,
                         'targetLocation':      targetLocation,
                         'targetTilt':          targetTilt,
                         'askDegree':           targetOri,
                         'repDegree':           reportOri,
                         'circleSteps':         count, 
                         'clockwise':           clockwise,
                         'difference':          difference, 
                         'fixationTime':        thisFixTime, 
                         'probeTime':           probeTime,
                         'pressTime':           pressTime, 
                         'releaseTime':         releaseTime, 
                         'responseTime':        pressTime - probeTime, 
                         'responseDuration':    releaseTime - pressTime,
                         'performance':         performance, 
                         'dialType':            dialType, 
                         'loadType':            loadType, 
                         'trialType':           trialType,
                         'taskType':            session,
                         'triggerEncoding1':    triggerEnc1,
                         'triggerEncoding2':    triggerEnc2,
                         'triggerProbe':        triggerProbe,
                         'triggerResponse':     triggerResponse}

            # Add trial data to logfile
            addTrialToData(filename, header, trialData) 

        presentBlockFeedback(performanceBlock, numBlocks, thisNumBlock) # show block feedback

if triggerSend == True:
    eyeTrackerStop(tracker)
    
presentTaskFinished()