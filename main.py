"""
    Author: Zachary Kennedy
    Date: 2/27/2022
    Desc:
            This python scripts generates a sine curve with a random period, then removes a portion of the
            data points making the period unrecognizeable. This script is meant to be used to test a
            string length minimization script for accuracy.

"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
import random as r

# Define function for sin curve
def sin(f, time, amp):
   return amp*m.sin(2*m.pi*f*time)

# Rate of how many data points are recorded per second
sample_rate = 0.03333333333

# Start time & end time for each data set
start_time = 0
end_time = 600

# Amplitude of Period
amp = 10

# Period of curve in seconds
T = 600

# Frequency of sine curve. Depends on period
f = 1/T

# Generate the time data points
time = np.arange(start_time, end_time, 1/sample_rate)

# Generate the sine curve outputs
sinewave = amp * np.sin(2 * np.pi * f * time)

# Plot and show curve
plt.scatter(time, sinewave)
plt.show()

