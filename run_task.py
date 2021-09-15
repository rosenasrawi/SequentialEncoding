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
            trialData = {'Left bar ori 1':      leftBar1.ori,                 
                         'Right bar ori 1':     rightBar1.ori,
                         'Left bar col 1':      leftBar1.lineColor, 
                         'Right bar col 1':     rightBar1.lineColor,
                         'Left bar ori 2':      leftBar2.ori,                 
                         'Right bar ori 2':     rightBar2.ori,
                         'Left bar col 2':      leftBar2.lineColor, 
                         'Right bar col 2':     rightBar2.lineColor,
                         'Col cued 1':          colCued1, 
                         'Col cued 2':          colCued2,                     # only if load 2
                         'Col probed':          colCued1,
                         'Target moment':       targetMoment,
                         'Target location':     targetLocation,
                         'Target tilt':         targetTilt,
                         'Ask degree':          targetOri,
                         'Rep degree':          reportOri,
                         'Circle steps':        count, 
                         'Clockwise':           clockwise,
                         'Difference':          difference, 
                         'Fixation time':       thisFixTime, 
                         'Probe start time':    probeTime,
                         'Press start time':    pressTime, 
                         'Release start time':  releaseTime, 
                         'Decision time':       pressTime - probeTime, 
                         'Response duration':   releaseTime - pressTime,
                         'Performance':         performance, 
                         'Dial type':           dialType, 
                         'Load type':           loadType, 
                         'Trial type':          trialType,
                         'Task type':           session,
                         'Trigger encoding 1':  triggerEnc1,
                         'Trigger encoding 2':  triggerEnc2,
                         'Trigger probe':       triggerProbe,
                         'Trigger response':    triggerResponse}

            # Add trial data to logfile
            addTrialToData(filename, header, trialData) 

        presentBlockFeedback(performanceBlock, numBlocks, thisNumBlock) # show block feedback

    if triggerSend == True:
        eyeTrackerStop(tracker)