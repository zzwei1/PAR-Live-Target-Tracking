# Requires Python 3.5 or lower version of Python 3

import sys
import csv
import json
import numpy
from firebase import firebase 

class firebaseDownload:
    ### LOCAL MODULES ###

    def firebaseDownloadLocal(self, firebaseProject):
        while True:
            result = firebaseProject.get('/DEV', 'SignalData')
            if result['Mode'] == 'Tracking' or result['Mode'] == 'Acquisition':
                break
            
        print(result['Channel1'])
        print(result['Channel2'])
        print(result['Mode'])
        print(result['PhaseDifference'])
        
        if result['Mode'] == 'Tracking':
            dataOut1 = numpy.asarray(result['Channel1']) # Convert result data from database into an array
            dataOut1 = dataOut1.reshape(len(dataOut1), 1) # Shape data for putting in one column of csv file

            with open(str(sys.argv[1])+"1.csv", "w") as f:
                writer = csv.writer(f, dialect='excel', lineterminator = '\n')
                writer.writerows(dataOut1)

            dataOut2 = numpy.asarray(result['Channel2']) # Convert result data from database into an array
            dataOut2 = dataOut2.reshape(len(dataOut2), 1) # Shape data for putting in one column of csv file

            with open(str(sys.argv[1])+"2.csv", "w") as f:
                writer = csv.writer(f, dialect='excel', lineterminator = '\n')
                writer.writerows(dataOut2)
            
            # Write to a CSV file here the tracking mode so MATLAB can check it
            with open(str(sys.argv[1])+"Status.csv", "w") as f:
                writer = csv.writer(f, dialect='excel', lineterminator = '\n')
                writer.writerow([result['Mode']])
        elif result['Mode'] == 'Acquisition':
            # Write to a CSV file here the aquisition mode so MATLAB can check it
            with open(str(sys.argv[1])+"Status.csv", "w") as f:
                writer = csv.writer(f, dialect='excel', lineterminator = '\n')
                writer.writerow([result['Mode']])

            print("Acquisition Mode")

    ### RADAR MODULES ###

    def firebaseDownloadRadar(self, firebaseProject):
        while True:
            result = firebaseProject.get('/DEV', 'SignalData')
            if result['Mode'] == 'Start' or result['Mode'] == 'Stop' or result['Mode'] == 'Local':
                break

        print(result['Mode'])
        print(result['PhaseDifference'])
        
        if result['Mode'] == 'Start':
            print("Starting system...")
            # Call driver stuff
        elif result['Mode'] == 'Stop':  
            print("Stopping system...")
            # Kill everything
        elif result['Mode'] == 'Local':
            print("Steering beamformer...")
            # Return phase difference result['PhaseDifference'] to steer beam
        

# firebaseProject = firebase.FirebaseApplication('https://par-live-target-tracking.firebaseio.com/DEV', None)
# firebaseDownloadRadar(firebaseProject)