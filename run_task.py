""" Import packages"""

import random

""" Import other task scripts """

from pp_info_logfile import *

session, subjectID = getInfo()
filename, header = createNewDatafile(session, subjectID)

from task_objects import *
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
            trialType = trialTypesTask[trial]

            # Trial presentation
            targetColors, nonTargetColors, targetMoment, targetLocation, targetTilt = determineTrialSpecifics(trialType, loadType, targetColors, nonTargetColors)
            thisFixTime = presentStim()
            clockwise, count = presentResponse(loadType, dialType, practice, targetColors)

            reportOri, targetOri, difference, performance = presentTrialFeedback(count, clockwise, dialType)
            performanceBlock.append(performance)

            if load == 0: #load one
                colCued1 = targetColors; colCued2 = []
            elif load == 1:
                colCued1 = targetColors[0]; colCued2 = targetColors[1]

            # Adding data to logfile
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
         #                'Dial start moment',
         #                'Response start moment', 
         #                'Response end moment', 
         #                'Response time', 
         #                'Response duration',
                         'Performance':         performance, 
                         'Dial type':           dialType, 
                         'Load type':           loadType, 
                         'Trial type':          trialType,
                         'Task type':           session}

            addTrialToData(filename, header, trialData) 

        presentBlockFeedback(performanceBlock) # show block feedback