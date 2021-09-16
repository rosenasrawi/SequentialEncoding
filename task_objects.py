""" Import packages"""

from psychopy import visual
from psychopy.hardware import keyboard

""" Import configuration parameters """

from param_configuration import *

""" Window & Keyboard """

mywin = visual.Window(
    color = backgroundColor,
    monitor = "testMonitor", 
    size = monitorSize,
    units = "pix",
    fullscr = True)

kb = keyboard.Keyboard()

""" Objects """

fixCross = visual.ShapeStim(
    win = mywin, 
    vertices = ((0,-fixSize), (0,fixSize), (0,0), (-fixSize,0), (fixSize,0)),
    lineWidth = LineWidth,
    closeShape = False,
    units = 'pix')

leftBar1 = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = leftBarPos)

rightBar1 = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = rightBarPos)

leftBar2 = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = leftBarPos)

rightBar2 = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = rightBarPos)

practiceBar = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = [0,0])

responseCircle = visual.Circle(
    win = mywin,
    radius = circleRadius,
    edges = circleEdges,
    lineWidth = LineWidth,
    lineColor = fixColor)

turnUpper = visual.Circle( 
    win = mywin,
    radius = miniCircleRadius,
    pos = upper_turnUpper,
    edges = circleEdges,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

turnLower = visual.Circle(
    win = mywin,
    radius = miniCircleRadius,
    pos = upper_turnLower,
    edges = circleEdges,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

""" Eye-tracking calibration """

eyecalibrationCircle = visual.Circle(
    win = mywin,
    radius = miniCircleRadius,
    edges = circleEdges,
    lineWidth = LineWidth,
    lineColor = fixColor,
    fillColor = fixColor
    #pos = determined later
)

eyecalibrationCircleMini = visual.Circle(
    win = mywin,
    radius = miniCircleRadius/3,
    edges = circleEdges,
    lineWidth = LineWidth,
    lineColor = eyeCalibMini,
    fillColor = eyeCalibMini
    #pos = determined later
)

""" Text """

precueTextColor = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Relevant color(s) this block:",
    color = fontColor,
    pos = [0,barSize[1]],
    height = fontSizePreCue)

precueColors1 = visual.TextStim( # Middle   # Is a color in load one, is "or" in load two
    win = mywin, 
    font = textFont,
    text = "",
    pos = [0,0],
    height = fontSizePreCue)

precueColors2 = visual.TextStim( # Left     # Is a color in load two, is empty in load one
    win = mywin, 
    font = textFont,
    text = "",
    pos = [-barSize[1],0],
    height = fontSizePreCue)

precueColors3 = visual.TextStim( # Right
    win = mywin, 
    font = textFont,
    text = "",
    pos = [barSize[1],0],
    height = fontSizePreCue)

precueTextDial = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Response dial this block:",
    color = fontColor,
    pos = [0,barSize[1]],
    height = fontSizePreCue)

space2continue = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Press [space] to continue",
    color = fontColor,
    pos = [0,-barSize[1]],
    height = fontSizePreCue)

practiceDialText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Practice turning the response dial:",
    color = fontColor,
    pos = [0,barSize[1]],
    height = fontSizePreCue)

practiceDialButtons = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Press and hold: \n \n \n [Z] to turn counterclockwise \n \n [M] to turn clockwise",
    color = fontColor,
    pos = [0,-barSize[1]],
    height = fontSizePreCue)

feedbackText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,2*fixSize],
    height = fontSizeFeedback)

blockFeedbackText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,barSize[1]],
    height = fontSizePreCue)

blockFeedbackPerformanceText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,0],
    height = fontSizePreCue)

eyecalibrationText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = 'Please follow the moving dot in:',
    color = fontColor,
    pos = [0,barSize[0]],
    height = fontSizePreCue)

eyecalibrationCounterText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,-barSize[0]],
    height = fontSizePreCue)

taskFinishedText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = 'You have now completed this session, thank you! \n \n Press [space] to close this window',
    color = fontColor,
    pos = [0,0],
    height = fontSizePreCue)