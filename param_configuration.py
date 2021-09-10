""" Import packages"""

from math import pi, atan2, degrees

""" Configuration script """

setting = 'laptop'

if setting == 'laptop':
    monitorHZ = 60
    height = 25; distance = 60; vertResolution = 1536 

elif setting == 'lab':
    monitorHZ = 140
    height = 35; distance = 90; vertResolution = 1920 

deg_per_px = degrees(atan2(.5*height, distance)) / (.5*vertResolution) # Calculate the number of degrees that correspond to a single pixel

# Sizes
barSize = [int(0.4/deg_per_px), int(3/deg_per_px)] # width, height      # 
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)

circleRadius = int(1.5/deg_per_px)
miniCircleRadius = int(0.15/deg_per_px)

# Degrees and ranges
maxTurn = 200/(200/monitorHZ)
quarterCircle = 0.5*pi
radStep = quarterCircle/maxTurn

oriRangeLeft = [-85, -5]
oriRangeRight = [5, 85]

# Locations
leftBarPos = [-int(4/deg_per_px),0]
rightBarPos = [int(4/deg_per_px),0]
fixPos = [0,0]

upper_turnUpper = [0, circleRadius] # 
upper_turnLower = [0, -circleRadius]
right_turnUpper = [circleRadius, 0]
right_turnLower = [-circleRadius, 0]

# Timings
fixTime = [int(monitorHZ/2), int(monitorHZ*8/10)]   # 500, 800 ms
encodingTime = int(monitorHZ/4)                     # 250 ms
betweenTime = int(monitorHZ*0.75)                   # 750 ms
delayTime = int(monitorHZ*1.75)                     # 1750 ms
feedbackTime = int(monitorHZ/4)                     # 250 ms

# Colors
backgroundColor = (50/510,50/510,50/510)                 # A1A1A1 had to change for the eye-tracker
barColors = ["#C2A025", "#3843C2", "#2FC259", "#CF3C3C"]    # orange, blue, green, purple
barColorNames = ['YELLOW', 'BLUE', 'GREEN', 'RED']       
fixColor = (300/510,300/510,300/510)                        # lightgrey

# Dials
dialNames = ["upper", "right"]

# Text
textFont = 'Helvetica'
fontSizeFeedback = int(0.3/deg_per_px)
fontSizePreCue = int(0.4/deg_per_px)
fontColor = (300/510,300/510,300/510)                       # lightgrey

# Trialtypes
targetMoments    = [0,0,0,0,1,1,1,1]
targetLocations  = [0,0,1,1,0,0,1,1]
targetTilts      = [0,1,0,1,0,1,0,1]

# Trialstypes
trialTypes = [0,1,2,3,4,5,6,7]

# Practice blocks
dialTypesPractice   = [0,1]
loadTypesPractice   = [0,1] # per dial type 
trialTypesPractice  = trialTypes * 2 # per load

# Task blocks
dialTypesTask   = [0,1,0,1,0,1]
loadTypesTask   = [0,1] # per dial type 
trialTypesTask  = trialTypes * 4 # per load

# Blocktypes
#loads = [0,1,0,1] # load one
#dials = [0,0,1,1]
#blockTypes = [0,1,2,3]