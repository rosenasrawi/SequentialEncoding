""" Import packages"""

from psychopy import core, event
from math import degrees, cos, sin
from statistics import mean
import random, time

""" Import other task scripts """

from task_objects import *                              # Task objects

""" Turning the dial """

def turnPositionsCircle(turnUpperPos, turnLowerPos, thisTurn):

    turnUpperPos = [turnUpperPos[0] * cos(thisTurn) + turnUpperPos[1] * sin(thisTurn),
                    -turnUpperPos[0] * sin(thisTurn) + turnUpperPos[1] * cos(thisTurn)]
    turnLowerPos = [turnLowerPos[0] * cos(thisTurn) + turnLowerPos[1] * sin(thisTurn),
                    -turnLowerPos[0] * sin(thisTurn) + turnLowerPos[1] * cos(thisTurn)]
    
    return turnUpperPos, turnLowerPos


""" Block specifics"""

def determineBlockSpecifics(load):

    nonTargetColors = barColors.copy() # Copy barcolors so I we remove the targets
    
    if load == 0: # load one
        targetColors = random.choice(barColors)     # Pick on color
        nonTargetColors.remove(targetColors)        # All other colors are non-targets

    elif load == 1: # load two
        targetColors = random.sample(barColors,2)   # Pick two colors
        nonTargetColors.remove(targetColors[0])     # The other two are non-targets
        nonTargetColors.remove(targetColors[1])
    
    #random.shuffle(trialTypes)                      # Trialtypes shuffled for each block
    return targetColors, nonTargetColors

""" Trial specifics"""

def determineTrialSpecifics(trial, load, targetColors, nonTargetColors):

    #trialType = trialTypes[trial]                   # What are the specs of this trial

    targetMoment = targetMoments[trial]
    targetLocation = targetLocations[trial]
    targetTilt = targetTilts[trial]

    random.shuffle(nonTargetColors)                 # non-target colors randomised
    
    if load == 0: # load one

        if targetMoment == 0 and targetLocation == 0:       # encoding one, left
            leftBar1.fillColor = targetColors # target
            rightBar1.fillColor = nonTargetColors[0] # divide other three 
            leftBar2.fillColor = nonTargetColors[1]
            rightBar2.fillColor = nonTargetColors[2]

        elif targetMoment == 0 and targetLocation == 1:     # encoding one, right
            leftBar1.fillColor = nonTargetColors[0]
            rightBar1.fillColor = targetColors # target
            leftBar2.fillColor = nonTargetColors[1]
            rightBar2.fillColor = nonTargetColors[2]   

        elif targetMoment == 1 and targetLocation == 0:     # encoding two, left
            leftBar1.fillColor = nonTargetColors[0]
            rightBar1.fillColor = nonTargetColors[1]
            leftBar2.fillColor = targetColors # target
            rightBar2.fillColor = nonTargetColors[2]

        elif targetMoment == 1 and targetLocation == 1:     # encoding two, right
            leftBar1.fillColor = nonTargetColors[0]
            rightBar1.fillColor = nonTargetColors[1]
            leftBar2.fillColor = nonTargetColors[2]
            rightBar2.fillColor = targetColors # target

    if load == 1: # load two
        random.shuffle(targetColors)                        # shuffle them, 0 = the target

        if targetMoment == 0 and targetLocation == 0:       # encoding one, left
            leftBar1.fillColor = targetColors[0] # target
            rightBar1.fillColor = nonTargetColors[0]
            leftBar2.fillColor = nonTargetColors[1]
            rightBar2.fillColor = targetColors[1] # other

        elif targetMoment == 0 and targetLocation == 1:     # encoding one, right
            leftBar1.fillColor = nonTargetColors[0]
            rightBar1.fillColor = targetColors[0] # target
            leftBar2.fillColor = targetColors[1] # other
            rightBar2.fillColor = nonTargetColors[1]   

        elif targetMoment == 1 and targetLocation == 0:     # encoding two, left
            leftBar1.fillColor = nonTargetColors[0]
            rightBar1.fillColor = targetColors[1] # other
            leftBar2.fillColor = targetColors[0] # target
            rightBar2.fillColor = nonTargetColors[1]

        elif targetMoment == 1 and targetLocation == 1:     # encoding two, right
            leftBar1.fillColor = targetColors[1] # other
            rightBar1.fillColor = nonTargetColors[0]
            leftBar2.fillColor = nonTargetColors[1]
            rightBar2.fillColor = targetColors[0] # target

    # Change all the linecolors accordingly
    leftBar1.lineColor = leftBar1.fillColor
    rightBar1.lineColor = rightBar1.fillColor
    leftBar2.lineColor = leftBar2.fillColor
    rightBar2.lineColor = rightBar2.fillColor

    # Orientations
    if targetLocation == 0:         # target left

        if targetTilt == 0:         # target tilted to the left
            leftBar1.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1])
            rightBar1.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            leftBar2.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 
            rightBar2.ori = random.randint(oriRangeRight[0],oriRangeRight[1])   

        elif targetTilt == 1:       # target tilted to the right
            leftBar1.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            rightBar1.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 
            leftBar2.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            rightBar2.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 

    elif targetLocation == 1:       # target right
        if targetTilt == 0:         # target tilted to the left
            leftBar1.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            rightBar1.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 
            leftBar2.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            rightBar2.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1])           
        elif targetTilt == 1:       # target tilted to the right
            leftBar1.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 
            rightBar1.ori = random.randint(oriRangeRight[0],oriRangeRight[1])
            leftBar2.ori = random.randint(oriRangeLeft[0],oriRangeLeft[1]) 
            rightBar2.ori = random.randint(oriRangeRight[0],oriRangeRight[1])    

    return targetColors, nonTargetColors, targetMoment, targetLocation, targetTilt

""" Practice dial """

def presentPracticeDial(dial, ori, targetColors, trial):

    practiceBar.setAutoDraw(True)
    practiceDialText.setAutoDraw(True)
    practiceDialButtons.setAutoDraw(True)

    if trial > 0: # Only instructions during the first trial
        practiceDialText.setAutoDraw(False)
        practiceDialButtons.setAutoDraw(False)

    loadPractice = None

    fixCross.lineColor = fixColor
    practiceBar.fillColor = fixCross.lineColor
    practiceBar.lineColor = fixCross.lineColor
    practiceBar.opacity = 0.5

    if ori == 0:
        practiceBar.ori = random.randint(oriRangeLeft[0], oriRangeLeft[1])
    elif ori == 1:
        practiceBar.ori = random.randint(oriRangeRight[0], oriRangeRight[1])

    presentResponse(loadPractice, dial, targetColors, portBioSemi = None, tracker = None, triggerSend = False)

""" Pre-cue dial """

def presentPrecueDial(dialType, targetColors):

    # Dial cue
    if dialType == 0: # upper
        turnUpper.pos = upper_turnUpper
        turnLower.pos = upper_turnLower
    elif dialType == 1: # right
        turnUpper.pos = right_turnUpper
        turnLower.pos = right_turnLower     

    fixCross.lineColor = fixColor

    precueTextDial.draw()
    responseCircle.draw()
    turnUpper.draw()
    turnLower.draw()
    fixCross.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')

    # Run practice
    oris = [0,1,0,1]

    for trial in range(len(oris)):
        ori = oris[trial]
        presentPracticeDial(dialType, ori, targetColors, trial)

    practiceBar.setAutoDraw(False)
    practiceDialText.setAutoDraw(False)

""" Pre-cue color """

def presentPrecueLoad(targetColors, load):

    # Load cue
    if load == 0: # load one
        precueColors1.color = targetColors
        precueColors1.text = barColorNames[barColors.index(targetColors)]

        precueColors2.text = ""
        precueColors3.text = ""

    elif load == 1: # load two   
        precueColors2.color = targetColors[0]
        precueColors2.text = barColorNames[barColors.index(targetColors[0])]

        precueColors1.color = fontColor
        precueColors1.text = "and"    

        precueColors3.color = targetColors[1]
        precueColors3.text = barColorNames[barColors.index(targetColors[1])]

    precueTextColor.draw()
    precueColors1.draw()
    precueColors2.draw()
    precueColors3.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')

""" Eye-tracker calibration """

def eyetrackingCalibration(triggerSend, portBioSemi = None, tracker = None):

    # Please follow the dot in 3, 2, 1:
    eyecalibrationText.setAutoDraw(True)
    eyecalibrationCounterText.setAutoDraw(True)

    eyecalibrationCounterText.text = '3'
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()

    eyecalibrationCounterText.text = ''
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()

    eyecalibrationCounterText.text = '2'
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()

    eyecalibrationCounterText.text = ''
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()

    eyecalibrationCounterText.text = '1'
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()    

    eyecalibrationCounterText.text = ''
    for i in range(encodingTime*2): # 500 ms
        mywin.flip()

    eyecalibrationText.setAutoDraw(False)
    eyecalibrationCounterText.setAutoDraw(False)

    # Dots start to appear
    eyecalibrationCircle.setAutoDraw(True)
    eyecalibrationCircleMini.setAutoDraw(True)

    posOrder = list(range(len(allPositions)))
    random.shuffle(posOrder)

    for pos in posOrder:
        eyecalibrationCircle.pos = list(allPositions[pos])
        eyecalibrationCircleMini.pos = list(allPositions[pos])

        if triggerSend == True:
            triggerCalib = calibrationTriggers[pos]
            mywin.callOnFlip(portBioSemi.setData, triggerCalib)
            mywin.callOnFlip(tracker.send_message, 'trig' + str(triggerCalib))

        for i in range(calibrationTime): # 1500 ms
            mywin.flip()
            if triggerSend == True:
                if i == 2:
                    portBioSemi.setData(resetTrigger)

    eyecalibrationCircle.setAutoDraw(False)
    eyecalibrationCircleMini.setAutoDraw(False)    

""" Present main stimuli """

def presentStim(triggerSend, trialType, loadType, dialType, portBioSemi, tracker):

    if loadType == 0: loadAdd = 0
    elif loadType == 1: loadAdd = 50

    if dialType == 0: dialAdd = 0
    elif dialType == 1: dialAdd = 100

    triggerEnc1 = trialType + 1 + loadAdd + dialAdd + 0
    triggerEnc2 = trialType + 1 + loadAdd + dialAdd + 10

    fixCross.lineColor = fixColor   
    fixCross.setAutoDraw(True)

    thisFixTime = random.randint(fixTime[0], fixTime[1])
    
    for i in range(thisFixTime):             # Fixation
        mywin.flip()
    
    leftBar1.setAutoDraw(True)
    rightBar1.setAutoDraw(True)

    if triggerSend == True:
        mywin.callOnFlip(portBioSemi.setData, triggerEnc1)
        mywin.callOnFlip(tracker.send_message, 'trig' + str(triggerEnc1))

    for i in range(encodingTime):             # First encoding display
        mywin.flip()
        if triggerSend == True:
            if i == 2: # turn off EEG trigger after 2 frames
                portBioSemi.setData(resetTrigger)

    leftBar1.setAutoDraw(False)
    rightBar1.setAutoDraw(False)

    for i in range(betweenTime):             # Fixation
        mywin.flip()

    if triggerSend == True:
        mywin.callOnFlip(portBioSemi.setData, triggerEnc2)
        mywin.callOnFlip(tracker.send_message, 'trig' + str(triggerEnc2))

    leftBar2.setAutoDraw(True)
    rightBar2.setAutoDraw(True)

    for i in range(encodingTime):             # Second encoding display
        mywin.flip()
        if triggerSend == True:
            if i == 2: # turn off EEG trigger after 2 frames
                portBioSemi.setData(resetTrigger)

    leftBar2.setAutoDraw(False)
    rightBar2.setAutoDraw(False)

    for i in range(delayTime):            # Memory delay
        mywin.flip()

    return thisFixTime, triggerEnc1, triggerEnc2

""" Present response dial """

def presentResponse(loadType, dialType, targetColors, portBioSemi, tracker, triggerSend, trialType = 0):

    if loadType == 0: loadAdd = 0
    elif loadType == 1: loadAdd = 50
    else: loadAdd = 0

    if dialType == 0: dialAdd = 0
    elif dialType == 1: dialAdd = 100

    triggerProbe = trialType + 1 + loadAdd + dialAdd + 20

    if triggerSend == True:
        mywin.callOnFlip(portBioSemi.setData, triggerProbe)
        mywin.callOnFlip(tracker.send_message, 'trig' + str(triggerProbe))

    kb.clearEvents()

    count = 0 # positions not updated yet
    clockwise = False
    key_release = []
    key_press = []

    if loadType == 0: # load 1
        fixCross.lineColor = targetColors
    elif loadType == 1: # load 2
        fixCross.lineColor = targetColors[0]        # 0 was the target
    
    if dialType == 0: # upper
        turnUpper.pos = upper_turnUpper             # Dial circles in the correct position
        turnLower.pos = upper_turnLower
    elif dialType == 1: # right
        turnUpper.pos = right_turnUpper
        turnLower.pos = right_turnLower        

    fixCross.setAutoDraw(True)
    responseCircle.setAutoDraw(True) 
    turnLower.setAutoDraw(True) 
    turnUpper.setAutoDraw(True) 

    probeTime = time.time()

    mywin.flip()
    if triggerSend == True:
        core.wait(2/monitorHZ) # two frames, 0.008 s
        portBioSemi.setData(resetTrigger) # turn off probe trigger

    key_press = event.waitKeys(keyList = ['z', 'm', 'q', 'escape'])     # Wait for a keypress

    if 'z' in key_press:
        pressTime = time.time()
        clockwise = False

        triggerResponse = trialType + 1 + loadAdd + dialAdd + 30
        if triggerSend == True:
            portBioSemi.setData(triggerResponse) #count 1
            tracker.send_message('trig' + str(triggerResponse))
            core.wait(2/monitorHZ) # two frames, 0.008 s
            portBioSemi.setData(resetTrigger) # turn off probe trigger

        while key_release == [] and count < maxTurn:
            
            key_release = kb.getKeys(keyList = ['z'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = -radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]

            count += 1 # one step updated

            mywin.flip()

    elif 'm' in key_press:
        pressTime = time.time()
        clockwise = True

        triggerResponse = trialType + 1 + loadAdd + dialAdd + 40
        if triggerSend == True:
            portBioSemi.setData(triggerResponse) #count 1
            tracker.send_message('trig' + str(triggerResponse))
            core.wait(2/monitorHZ) # two frames, 0.008 s
            portBioSemi.setData(resetTrigger) # turn off probe trigger

        while key_release == [] and count < maxTurn:

            key_release = kb.getKeys(keyList = ['m'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]  

            count += 1 # one step updated
            mywin.flip()

    elif 'q' in key_press:
        pressTime = time.time()
        core.quit()
        
    releaseTime = time.time()
    key_press = []
    key_release = []

    responseCircle.setAutoDraw(False) 
    turnLower.setAutoDraw(False) 
    turnUpper.setAutoDraw(False)
    fixCross.setAutoDraw(False)

    return clockwise, count, probeTime, pressTime, releaseTime, triggerProbe, triggerResponse

""" Practice trial feedback """

def presentTrialFeedback(count, clockwise, dial):

    # Determine response orientation
    if clockwise == False: # Z press
        reportOri = degrees(count * radStep)*-1
    if clockwise == True: # M press
        reportOri = degrees(count * radStep)

    if dial == 1: # start point 90* higher
        reportOri += 90
    
    # Determine the target orientation
    if (fixCross.lineColor == leftBar1.fillColor).all():
        targetOri = leftBar1.ori
    elif (fixCross.lineColor == rightBar1.fillColor).all():
        targetOri = rightBar1.ori
    elif (fixCross.lineColor == leftBar2.fillColor).all():
        targetOri = leftBar2.ori
    elif (fixCross.lineColor == rightBar2.fillColor).all():
        targetOri = rightBar2.ori

    if dial == 1 and targetOri < 0:     # if "left" tilt, actually "right" tilt
        targetOri += 180

    difference = abs(targetOri - round(reportOri))

    if difference > 90:                 # difference can't be more than 90
        difference -= 180
        difference *= -1

    performance = round(100 - difference/90 * 100)
    performanceText = str(performance)
    feedbackText.text = performanceText

    fixCross.setAutoDraw(True)
    feedbackText.setAutoDraw(True)

    for i in range(feedbackTime): # 250 ms 
        mywin.flip()

    fixCross.setAutoDraw(False)
    feedbackText.setAutoDraw(False)  

    return round(reportOri), targetOri, difference, performance    

def presentBlockFeedback(performanceBlock, numBlocks, thisNumBlock):

    performanceBlock = round(mean(performanceBlock))
    blockFeedbackPerformanceText.text = str(performanceBlock) + "% correct"

    numBlocks = str(numBlocks)
    thisNumBlock = str(thisNumBlock)

    blockFeedbackText.text = "Performance this block [" + thisNumBlock + "/" + numBlocks + "]:"
    blockFeedbackText.draw()
    blockFeedbackPerformanceText.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')    


def presentTaskFinished():
    taskFinishedText.draw()
    mywin.flip()
    event.waitKeys(keyList = 'space')    