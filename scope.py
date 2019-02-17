###########################
#  Scope Image Generator  #
#    Author: Hanfei Cui   #
#        17/02/2019       #
###########################

import numpy as np
import matplotlib.pyplot as plt
import time

# Request for inputs
channel = input('Please enter the number of channels (1 or 2): ')
filename = input('Please enter of the CSV data file name: ')

# Create canvas for diagram
fig1 = plt.figure(1,figsize=(10,6))

def labelling():
    """
    This function replacing the repeated work of labelling x-axis, y-axis , the title, legends and finally save the figure."""
    title = input('Please enter the title of output figure: ')
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.legend()
    plt.savefig("Scope_%s"%str(round(time.time())))   # Time stamp on file names
    plt.show()

if channel == "1" :
    t,y1 = np.loadtxt(filename,delimiter=",",unpack=True,skiprows=2)
    t = t - min(t)
    plt.plot(t,y1,"b-",label="Oscilloscope observation")
    labelling()
elif channel == "2":
    t,y1,y2 = np.loadtxt(filename,delimiter=",",unpack=True,skiprows=2)
    t = t - min(t)
    plt.plot(t,y1,"b-",label=input('y1 legend: '))
    plt.plot(t,y2,"r-",label=input('y2 legend: '))
    labelling()
else:
    print("Input of channel is invalid. Program stops.")
    quit() # End program if invalid of channel 2

# Closing the program 
input('Enter to exit.')