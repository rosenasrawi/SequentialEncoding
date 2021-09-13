from psychopy import parallel
import eyelinker

from param_configuration import resetTrigger, eyeDirectory
from task_objects import mywin
import os

def activateEEGandEyeTracker(subjectID, session):

    # EEG
    portBioSemi = parallel.ParallelPort(address = 0x3010)
    portBioSemi.setData(resetTrigger)

    # Eye-tracker
    tracker = eyelinker.EyeLinker(window = mywin, 
                                    filename = 'rn1_' + subjectID + session + '.edf',
                                    eye = 'BOTH')

    return portBioSemi, tracker

def eyeTrackerStart(tracker):
    os.chdir(eyeDirectory)

    tracker.open_edf() # open a data file
    tracker.initialize_tracker()
    tracker.start_recording()

def eyeTrackerStop(tracker):
    tracker.stop_recording()
    tracker.transfer_edf()
    tracker.close_edf()

    