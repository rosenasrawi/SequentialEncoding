""" Import packages"""

from psychopy import visual
from psychopy.hardware import keyboard

""" Import configuration parameters """

from param_configuration import *

""" Window & Keyboard """

mywin = visual.Window(
    color = backgroundColor,
    monitor = "testMonitor", 
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
    edges = 50,
    lineWidth = LineWidth,
    lineColor = fixColor)

turnUpper = visual.Circle( 
    win = mywin,
    radius = miniCircleRadius,
    pos = upper_turnUpper,
    edges = 50,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

turnLower = visual.Circle(
    win = mywin,
    radius = miniCircleRadius,
    pos = upper_turnLower,
    edges = 50,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

""" Text """

precueTextColor = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Relevant color(s) this block:",
    color = fontColor,
    pos = [0,barSize[1]],
    height = fontSizePreCue)

precueColors1 = visual.TextStim( # Middle
    win = mywin, 
    font = textFont,
    text = "",
    pos = [0,0],
    height = fontSizePreCue)

precueColors2 = visual.TextStim( # Left
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

feedbackText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,2*fixSize],
    height = fontSizeFeedback)