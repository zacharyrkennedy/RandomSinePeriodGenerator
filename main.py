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
import pandas as pd
import xlsxwriter as xl

# Define function for sin curve
def sin(f, time, amp):
   return amp*m.sin(2*m.pi*f*time)

# Rate of how many data points are recorded per second
sample_rate = 0.03333333333

# Start time & end time for each data set
start_time = 0
end_time = 144000

# Amplitude of Period
amp = 1

# Period of curve in seconds
T = 36000

# Frequency of sine curve. Depends on period
f = 1/T

# Generate the time data points
time = np.arange(start_time, end_time, 1/sample_rate)

# Generate the sine curve outputs
sinewave = amp * np.sin(2 * np.pi * f * time) + 10

# Convert Numpy arrays to python lists
new_time = time.tolist()
new_sinewave = sinewave.tolist()

# Randomly remove data points
for i in range(int(len(new_time)*.9975)):
    random_index = np.random.randint(0, int(len(new_time)*.9975))
    new_time.pop(random_index)
    new_sinewave.pop(random_index)

# Create output excel worksheet
workbook = xl.Workbook('output.xlsx')

# Add worksheet to workbook
worksheet = workbook.add_worksheet()

# Set starting row for data
row = 1

# Create column titles
worksheet.write_string(0, 0, 'Time (s)')
worksheet.write_string(0, 1, 'Magnitude')

# Add data to worksheet
for i in range(len(new_time)):
    worksheet.write(row, 0, new_time[i])
    worksheet.write(row, 1, new_sinewave[i])
    row += 1

# Close workbook
workbook.close()

# Plot and show curve
plt.scatter(new_time, new_sinewave)
plt.show()

