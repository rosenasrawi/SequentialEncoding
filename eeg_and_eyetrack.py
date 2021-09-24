from psychopy import parallel, event
import eyelinker

from param_configuration import resetTrigger, eyeDirectory
from task_objects import mywin
from task_functions import eyecalibrationWaitText
import os

def activateEEGandEyeTracker(subjectID, session):

    # EEG
    portBioSemi = parallel.ParallelPort(address = 0x3050)
    portBioSemi.setData(resetTrigger)

    # Eye-tracker
    tracker = eyelinker.EyeLinker(window = mywin, 
                                  filename = 'rn3_' + subjectID + session + '.edf',
                                  eye = 'RIGHT')

    return portBioSemi, tracker

def eyelinkStart(tracker):
    os.chdir(eyeDirectory)

    tracker.open_edf() # open a data file
    tracker.init_tracker()
    tracker.start_recording()

def eyelinkCalibrate(tracker):
    tracker.stop_recording()
    eyecalibrationWaitText.draw()

    event.waitKeys(keyList = 'E')
    tracker.start_recording()
    #tracker.calibrate(width = monitorSize[0], height = monitorSize[1])

def eyelinkStop(tracker):
    os.chdir(eyeDirectory)

    tracker.stop_recording()
    tracker.transfer_edf()
    tracker.close_edf()

    