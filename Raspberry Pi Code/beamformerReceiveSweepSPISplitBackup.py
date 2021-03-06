import time
import sys
from math import *
import subprocess
import os

#********************* T a b l e   o f  P h a s e  S e t t i n g s ************
angle_array = [0, 2.813, 5.625, 8.438, 11.25, 14.063, 16.875, 19.688, 22.5, 25.313, 28.125, 30.938, 33.75, 36.563, 39.375, 42.188, 45, 47.813, 50.625, 53.438, 56.25, 59.063, 61.875, 64.688, 67.5, 70.313, 73.125, 75.938, 78.75, 81.563, 84.375, 87.188, 90, 92.813, 95.625, 98.438, 101.25, 104.063, 106.875, 109.688, 112.5, 115.313, 118.125, 120.938, 123.75, 126.563, 129.375, 132.188, 135, 137.813, 140.625, 143.438, 146.25, 149.063, 151.875, 154.688, 157.5, 160.313, 163.125, 165.938, 168.75, 171.563, 174.375, 177.188, 180, 182.813, 185.625, 188.438, 191.25, 194.063, 196.875, 199.688, 202.5, 205.313, 208.125, 210.938, 213.75, 216.563, 219.375, 222.188, 225, 227.813, 230.625, 233.438, 236.25, 239.063, 241.875, 244.688, 247.5, 250.313, 253.125, 255.938, 258.75, 261.563, 264.375, 267.188, 270, 272.813, 275.625, 278.438, 281.25, 284.063, 286.875, 289.688, 292.5, 295.313, 298.125, 300.938, 303.75, 306.563, 309.375, 312.188, 315, 317.813, 320.625, 323.438, 326.25, 329.063, 331.875, 334.688, 337.5, 340.313, 343.125, 345.938, 348.75, 351.563, 354.375, 357.188]
I_array = [0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3E, 0x3E, 0x3D, 0x3D, 0x3C, 0x3C, 0x3B, 0x3A, 0x39, 0x38, 0x37, 0x36, 0x35, 0x34, 0x33, 0x32, 0x30, 0x2F, 0x2E, 0x2C, 0x2B, 0x2A, 0x28, 0x27, 0x25, 0x24, 0x22, 0x21, 0x1, 0x3, 0x4, 0x6, 0x7, 0x8, 0xA, 0xB, 0xD, 0xE, 0xF, 0x11, 0x12, 0x13, 0x14, 0x16, 0x17, 0x18, 0x19, 0x19, 0x1A, 0x1B, 0x1C, 0x1C, 0x1D, 0x1E, 0x1E, 0x1E, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1E, 0x1E, 0x1D, 0x1D, 0x1C, 0x1C, 0x1B, 0x1A, 0x19, 0x18, 0x17, 0x16, 0x15, 0x14, 0x13, 0x12, 0x10, 0xF, 0xE, 0xC, 0xB, 0xA, 0x8, 0x7, 0x5, 0x4, 0x2, 0x1, 0x21, 0x23, 0x24, 0x26, 0x27, 0x28, 0x2A, 0x2B, 0x2D, 0x2E, 0x2F, 0x31, 0x32, 0x33, 0x34, 0x36, 0x37, 0x38, 0x39, 0x39, 0x3A, 0x3B, 0x3C, 0x3C, 0x3D, 0x3E, 0x3E, 0x3E, 0x3F, 0x3F, 0x3F]
Q_array = [0x20, 0x21, 0x23, 0x24, 0x26, 0x27, 0x28, 0x2A, 0x2B, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x38, 0x39, 0x3A, 0x3A, 0x3B, 0x3C, 0x3C, 0x3C, 0x3D, 0x3D, 0x3D, 0x3D, 0x3D, 0x3D, 0x3D, 0x3D, 0x3D, 0x3C, 0x3C, 0x3C, 0x3B, 0x3A, 0x3A, 0x39, 0x38, 0x38, 0x37, 0x36, 0x35, 0x34, 0x33, 0x31, 0x30, 0x2F, 0x2E, 0x2D, 0x2B, 0x2A, 0x28, 0x27, 0x26, 0x24, 0x23, 0x21, 0x20, 0x1, 0x3, 0x4, 0x6, 0x7, 0x8, 0xA, 0xB, 0xD, 0xE, 0xF, 0x10, 0x11, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x1A, 0x1B, 0x1C, 0x1C, 0x1C, 0x1D, 0x1D, 0x1D, 0x1D, 0x1D, 0x1D, 0x1D, 0x1D, 0x1D, 0x1C, 0x1C, 0x1C, 0x1B, 0x1A, 0x1A, 0x19, 0x18, 0x18, 0x17, 0x16, 0x15, 0x14, 0x13, 0x11, 0x10, 0xF, 0xE, 0xD, 0xB, 0xA, 0x8, 0x7, 0x6, 0x4, 0x3, 0x1]

# ADAR1000 RX Channel setup
def Init_ADAR1000():
    os.system('sudo ./spi_write 0x00 0x81 0')
    return
    ## Initializing ADAR1000 RX_1 for signal input ##
    writeDelay = 0.1
    # Reset the whole board
    instruction = 'sudo ./spi_write 0x00 0x81 0'
    subprocess.call(instruction)
    return
    time.sleep(writeDelay)
    instruction = './spi_write 0x00 0x81 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    # Configure the whole board for SPI communication
    instruction = './spi_write 0x00 0x18 0'
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x00 0x18 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)
    
    # Set 1.8v LDO output (Adjust LDOs) # NEED THIS TO WORK LATER
    instruction = './spi_write 0x400 0x55 0' # LDO_TRIM_CTRL_0
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x400 0x55 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    # Select SPI for channel settings
    instruction = './spi_write 0x38 0x60 0'
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x38 0x60 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    # Enable LNA
    instruction = './spi_write 0x2E 0x7F 0' 
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x2E 0x7F 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    #Set RX LNA bias to 8
    instruction = './spi_write 0x34 0x08 0' 
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x34 0x08 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    #Set RX VGA bias to 2
    instruction = './spi_write 0x35 0x16 0' 
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x35 0x16 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    # Enables the whole Rx 
    instruction = './spi_write 0x31 0x20 0' 
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x31 0x20 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

    # Loads the Rx working registers from the SPI 
    instruction = './spi_write 0x28 0x01 0' 
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 1'
    subprocess.call(instruction)
    time.sleep(writeDelay)

def phaseShift(angle):
    wavelength = 2.778 #cm
    eDist = 1.5 #Distance between each patch antenna elements in centimeters
    plane = 360
    
    #Constant for phase increment. ref: http://www.radartutorial.eu/06.antennas/Phased%20Array%20Antenna.en.html
    pCon = ( plane * eDist ) / wavelength
    #Use formula to calculate phase shift. ref: above
    pShift = pCon * math.sin(math.radians(angle))
    return pShift

# Calculate the I and Q register values and set each channel
def BeamSteering(angle):
    #Calculate phase shift between two elements
    pshift = phaseShift(angle) 
    #print "angle "+ str(angle) +"\tpshift: " + str(pshift)
    #Copy list of angles into a numerical python array
    phases = np.asarray(angle_array)
    plane = 360
    writeDelay = 0.1
    
    #****************** B o a r d A - RX_1  **************** 
    # 
    #Set the first antenna to 0 degrees    
    
    #//////////////////////////////////////////////////
    index = (np.abs(phases-angle)).argmin()
    #Write to Registers 
    instruction = './spi_write 0x10 0xFF 0' #Ch1_RX_GAIN
    subprocess.call(instruction)
    return
    time.sleep(writeDelay) # add if needed in between everything
    instruction = './spi_write 0x14 ' + str(I_array[index]).replace('0x','') + ' 0' #CH1_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x15 ' + str(Q_array[index]).replace('0x','') + ' 0' #CH1_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 0' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d A - RX_2  **************** 
    
    #Map the angle to a value between 0 and 360 degrees
    aE2Shift = pshift % plane   
    index = (np.abs(phases-aE2Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(aE2Shift)+'\t'+str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers 
    instruction = './spi_write 0x11 0xFF 0' #Ch2_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x16 ' + str(I_array[index]).replace('0x','') + ' 0' #CH2_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x17 ' + str(Q_array[index]).replace('0x','') + ' 0' #CH2_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 0' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d A - RX_3  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    aE3Shift = (2 * pshift) % plane
    index = (np.abs(phases-aE3Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(aE3Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x12 0xFF 0' #Ch3_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x18 ' + str(I_array[index]).replace('0x','') + ' 0' #CH3_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x19 ' + str(Q_array[index]).replace('0x','') + ' 0' #CH3_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 0' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d A - RX_4  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    aE4Shift = (3 * pshift) % plane
    index = (np.abs(phases-aE4Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(aE4Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x13 0xFF 0' #Ch4_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x1A ' + str(I_array[index]).replace('0x','') + ' 0' #CH4_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x1B ' + str(Q_array[index]).replace('0x','') + ' 0' #CH4_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 0' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d B - RX_1  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    bE1Shift = (4 * pshift) % plane
    index = (np.abs(phases-bE1Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(bE1Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x10 0xFF 1' #Ch5_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x14 ' + str(I_array[index]).replace('0x','') + ' 1' #CH5_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x15 ' + str(Q_array[index]).replace('0x','') + ' 1' #CH5_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 1' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d B - RX_2  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    bE2Shift = (5 * pshift) % plane
    index = (np.abs(phases-bE2Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(bE2Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x11 0xFF 1' #Ch6_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x16 ' + str(I_array[index]).replace('0x','') + ' 1' #CH6_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x17 ' + str(Q_array[index]).replace('0x','') + ' 1' #CH6_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 1' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d B - RX_3  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    bE3Shift = (6 * pshift) % plane
    index = (np.abs(phases-bE3Shift)).argmin()
    #print str(angle_array[index])+'\t'+str(bE3Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x12 0xFF 1' #Ch7_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x18 ' + str(I_array[index]).replace('0x','') + ' 1' #CH7_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x19 ' + str(Q_array[index]).replace('0x','') + ' 1' #CH7_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 1' #Load Work Registers
    subprocess.call(instruction)


    #****************** B o a r d B - RX_4  **************** 

    #Apply phase shift to next antenna  
    #Map the angle to a value between 0 and 360 degrees
    bE4Shift = (7 * pshift) % plane
    index = (np.abs(phases-bE4Shift)).argmin()  
    #print str(angle_array[index])+'\t'+str(bE4Shift)+'\t'+ str(I_array[index]) + '\t'+ str(Q_array[index]) 
    #Write to Registers
    instruction = './spi_write 0x13 0xFF 1' #Ch8_RX_GAIN
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x1A ' + str(I_array[index]).replace('0x','') + ' 1' #CH8_RX_PHASE_I
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x1B ' + str(Q_array[index]).replace('0x','') + ' 1' #CH8_RX_PHASE_Q
    subprocess.call(instruction)
    time.sleep(writeDelay)
    instruction = './spi_write 0x28 0x01 1' #Load Work Registers
    subprocess.call(instruction)

print "Initalizing ADAR1004..."
Init_ADAR1000()

#b_start = -40
##b_end = sys.argv[1]
#b_end = 40
#b_increment = 10
#print "Beamformer Sweeping..."
#for angle in (range(b_start, b_end, b_increment)): # at each postion, loop through the beam angles
#    BeamSteering(angle)

#BeamSteering(0)
