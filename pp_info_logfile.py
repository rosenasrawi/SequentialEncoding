import os, csv
from datetime import datetime

from param_configuration import dataDirectory

def getInfo():
    session = input('Current session (a, b): ') 
    subjectID = input('Subject ID (01, 02, ...): ')
        
    return session, subjectID

def createNewDatafile(session, subjectID):

    os.chdir(dataDirectory)
    now = datetime.now()
    now = now.strftime('%m%d%Y_%H%M%S')

    filename = 'rn3_s' + subjectID + session + '_' + now + '.csv'

    with open(filename, mode = 'w') as datafile:

        header = ['Left bar ori 1',                 
                  'Right bar ori 1',
                  'Left bar col 1', 
                  'Right bar col 1',
                  'Left bar ori 2', 
                  'Right bar ori 2',
                  'Left bar col 2', 
                  'Right bar col 2',                
                  'Col cued 1', 
                  'Col cued 2',                     # only if load 2
                  'Col probed',
                  'Target moment',
                  'Target location',
                  'Target tilt',
                  'Ask degree',
                  'Rep degree',
                  'Circle steps', 
                  'Clockwise',
                  'Difference', 
                  'Fixation time', 
                  'Probe start time',
                  'Press start time', 
                  'Release start time', 
                  'Decision time', 
                  'Response duration',
                  'Performance',
                  'Dial type', 
                  'Load type', 
                  'Trial type',
                  'Task type',
                  'Trigger encoding 1',
                  'Trigger encoding 2',
                  'Trigger probe',
                  'Trigger response']

        writer = csv.DictWriter(datafile, delimiter = ',', fieldnames = header)
        writer.writeheader()

    return filename, header

def addTrialToData(filename, header, trialData):
    
    os.chdir(dataDirectory)
    
    with open(filename, mode = 'a', newline = '') as datafile:
        writer = csv.DictWriter(datafile, fieldnames = header)
        writer.writerow(trialData)

