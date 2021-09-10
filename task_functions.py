""" Import packages"""

from psychopy import core, event
from math import degrees, cos, sin
from statistics import mean
import random

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

def presentPracticeDial(dial, ori, targetColors):
    practice = True
    load = None

    fixCross.lineColor = fixColor
    practiceBar.fillColor = fixCross.lineColor
    practiceBar.lineColor = fixCross.lineColor
    practiceBar.opacity = 0.5

    if ori == 0:
        practiceBar.ori = random.randint(oriRangeLeft[0], oriRangeLeft[1])
    elif ori == 1:
        practiceBar.ori = random.randint(oriRangeRight[0], oriRangeRight[1])

    presentResponse(load, dial, practice, targetColors)

""" Pre-cue dial """

def presentPrecueDial(dial, targetColors):

    # Dial cue
    if dial == 0: # upper
        turnUpper.pos = upper_turnUpper
        turnLower.pos = upper_turnLower
    elif dial == 1: # right
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
    
    load = None
    oris = [0,1,0,1]

    for trial in range(len(oris)):
        ori = oris[trial]

        presentPracticeDial(dial, ori, targetColors)

    practiceBar.setAutoDraw(False)

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

""" Present main stimuli """

def presentStim():

    fixCross.lineColor = fixColor   
    fixCross.setAutoDraw(True)

    thisFixTime = random.randint(fixTime[0], fixTime[1])
    
    for i in range(thisFixTime):             # Fixation
        mywin.flip()
    
    leftBar1.setAutoDraw(True)
    rightBar1.setAutoDraw(True)

    for i in range(encodingTime):             # First encoding display
        mywin.flip()

    leftBar1.setAutoDraw(False)
    rightBar1.setAutoDraw(False)

    for i in range(betweenTime):             # Fixation
        mywin.flip()

    leftBar2.setAutoDraw(True)
    rightBar2.setAutoDraw(True)

    for i in range(encodingTime):             # Second encoding display
        mywin.flip()

    leftBar2.setAutoDraw(False)
    rightBar2.setAutoDraw(False)

    for i in range(delayTime):            # Memory delay
        mywin.flip()

    return thisFixTime
""" Present response dial """

def presentResponse(load, dial, practice, targetColors):

    kb.clearEvents()

    count = 0 # positions not updated yet
    clockwise = False
    key_release = []
    key_press = []

    if load == 0: # load 1
        fixCross.lineColor = targetColors
    elif load == 1: # load 2
        fixCross.lineColor = targetColors[0]        # 0 was the target
    
    if dial == 0: # upper
        turnUpper.pos = upper_turnUpper             # Dial circles in the correct position
        turnLower.pos = upper_turnLower
    elif dial == 1: # right
        turnUpper.pos = right_turnUpper
        turnLower.pos = right_turnLower        

    fixCross.setAutoDraw(True)
    responseCircle.setAutoDraw(True) 
    turnLower.setAutoDraw(True) 
    turnUpper.setAutoDraw(True) 

    if practice == True:
        practiceBar.setAutoDraw(True)

    mywin.flip()
    key_press = event.waitKeys(keyList = ['z', 'm', 'q', 'escape'])     # Wait for a keypress

    if 'z' in key_press:
        clockwise = False
        while key_release == [] and count < maxTurn:
            
            key_release = kb.getKeys(keyList = ['z'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = -radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]

            count += 1 # one step updated

            mywin.flip()

    elif 'm' in key_press:
        clockwise = True
        while key_release == [] and count < maxTurn:

            key_release = kb.getKeys(keyList = ['m'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]  

            count += 1 # one step updated
            mywin.flip()

    elif 'q' in key_press:
        core.quit()
        
    key_press = []
    key_release = []

    responseCircle.setAutoDraw(False) 
    turnLower.setAutoDraw(False) 
    turnUpper.setAutoDraw(False)
    fixCross.setAutoDraw(False)

    return clockwise, count

""" Practice trial feedback """

def presentTrialFeedback(count, clockwise, dial):

    # Determine response orientation
    if clockwise == False: # Z press
        reportOri = degrees(count * radStep)*-1
    if clockwise == True: # M press
        reportOri = degrees(count * radStep)

    if dial == 1: # start point 90* higher
        reportOri += 90
    
    # Target color
    targetCol = fixCross.lineColor

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

    return reportOri, targetOri, difference, performance    

def presentBlockFeedback(performanceBlock):
    performanceBlock = round(mean(performanceBlock))
    blockFeedbackPerformanceText.text = str(performanceBlock) + "% correct"
    blockFeedbackText.draw()
    blockFeedbackPerformanceText.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')    
