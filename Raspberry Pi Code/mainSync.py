import subprocess
from firebaseUpload import FirebaseUpload
from firebaseDownload import FirebaseDownload
from firebase import firebase
import time

upload = FirebaseUpload()
download = FirebaseDownload()
firebaseProject = firebase.FirebaseApplication('https://par-live-target-tracking.firebaseio.com/DEV', None)

beamformerThreshold = 10.0 # Amplitude setting for threshold
offsetAngle = 5
waitStart = True
while True: # Outer loop for keeping radar listening continuously
    if waitStart == True:
        print('Capstone PAR Alpha System waiting for activation...')
        waitStart = False
    state, phase = download.firebaseDownloadRadar(firebaseProject)
    if state == 'Start':
        subprocess.call('python beamformerInitialize.py', shell=True) # Initialize beamformer

        while state != 'Stop': 
            # Acquisition Mode
            upload.firebaseUploadAcquisition(firebaseProject)
            state, phase = download.firebaseDownloadRadar(firebaseProject) # Check status of firebase
            if state == 'Stop':
                break
            amplitudeValues = []
            # Check every angle with beamformer
            beamformerPositions = 5
            for i in range(beamformerPositions): # for i=0 to i=(beamformerPositions-1)
                positionNumber = int(i)
                angleDivision = int(180/int(beamformerPositions-1))
                position = positionNumber * angleDivision
                subprocess.call('python beamformerSteer.py ' + str(position), shell=True)

                time.sleep(0.1) # Wait to stabilize beamformer signal input
                f = open('sweep.txt', 'w')
                f.write(str("Stop Sweep"))
                f.close()
                time.sleep(0.5) # Wait for analog discovery to stop measuring
                
                with open('amplitude.txt', 'r') as file:
                   amplitude = float(file.read())
                
                f = open('sweep.txt', 'w')
                f.write(str("Sweep"))
                f.close()

                if str(amplitude) != "failed to open device":
                    print("Amplitude found: " + amplitude)
                    amplitudeValues.append(float(amplitude))
                else:
                    i = i - 1 # Retest the previous position
            
            if max(amplitudeValues) > beamformerThreshold:
                maxAmplitudeIndex = amplitudeValues.index(max(amplitudeValues))
                print("Target found. Repositioning for tracking")
                positionNumber = int(maxAmplitudeIndex)
                angleDivision = int(180/int(beamformerPositions-1))
                position = positionNumber * angleDivision
                subprocess.call('python beamformerSteer.py ' + str(position), shell=True)
                
                time.sleep(0.1) # Wait to stabilize beamformer signal input
                f = open('sweep.txt', 'w')
                f.write(str("Stop Sweep"))
                f.close()
                time.sleep(0.5) # Wait for analog discovery to stop measuring
                
                with open('amplitude.txt', 'r') as file:
                   amplitude = float(file.read())
                upload.firebaseUploadTracking(firebaseProject) 

                f = open('sweep.txt', 'w')
                f.write(str("Sweep"))
                f.close()

                currentAngle = int(maxAmplitudeIndex) * int(180/int(beamformerPositions-1))
                while state != 'Stop': 
                    # Tracking Mode
                    state, phase = download.firebaseDownloadRadar(firebaseProject) # Wait for state to be local
                    if state == 'Stop':
                        break
                    if state == 'Local':
                        if float(phase) > 0:
                            currentAngle = currentAngle + offsetAngle
                            subprocess.call('python beamformerSteer.py ' + str(currentAngle), shell=True)
                        elif float(phase) < 0:
                            currentAngle = currentAngle - offsetAngle
                            subprocess.call('python beamformerSteer.py ' + str(currentAngle), shell=True)

                        time.sleep(0.1) # Wait to stabilize beamformer signal input
                        f = open('sweep.txt', 'w')
                        f.write(str("Stop Sweep"))
                        f.close()
                        time.sleep(0.5) # Wait for analog discovery to stop measuring

                        with open('amplitude.txt', 'r') as file:
                           amplitude = float(file.read())
                        if float(amplitude) > beamformerThreshold:
                            # state, phase = download.firebaseDownloadRadar(firebaseProject) 
                            # if state == 'Stop':
                            #     break
                            upload.firebaseUploadTracking(firebaseProject) 
                            f = open('sweep.txt', 'w')
                            f.write(str("Sweep"))
                            f.close()
                        else:
                            f = open('sweep.txt', 'w')
                            f.write(str("Sweep"))
                            f.close()
                            break # Go back to acquisition
                    else:
                        pass
        waitStart = True
        print("Stopping System...")
