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

        header = ['leftBarOri1',                 
                  'rightBarOri1',
                  'leftBarCol1', 
                  'rightBarCol1',
                  'leftBarOri2', 
                  'rightBarOri2',
                  'leftBarCol2', 
                  'rightBarCol2',                
                  'colCued1', 
                  'colCued2',                     # only if load 2
                  'colProbed',
                  'targetMoment',
                  'targetLocation',
                  'targetTilt',
                  'askDegree',
                  'repDegree',
                  'circleSteps', 
                  'clockwise',
                  'difference', 
                  'fixationTime', 
                  'probeTime',
                  'pressTime', 
                  'releaseTime', 
                  'responseTime', 
                  'responseDuration',
                  'performance',
                  'dialType', 
                  'loadType', 
                  'trialType',
                  'taskType',
                  'triggerEncoding1',
                  'triggerEncoding2',
                  'triggerProbe',
                  'triggerResponse']

        writer = csv.DictWriter(datafile, delimiter = ',', fieldnames = header)
        writer.writeheader()

    return filename, header

def addTrialToData(filename, header, trialData):
    
    os.chdir(dataDirectory)
    
    with open(filename, mode = 'a', newline = '') as datafile:
        writer = csv.DictWriter(datafile, fieldnames = header)
        writer.writerow(trialData)

