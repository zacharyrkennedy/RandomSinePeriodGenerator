"""
    Author: Zachary Kennedy
    Date: 2/27/2022
    Desc:
            This python scripts generates a sine curve with a random period, then removes a portion of the
            data points making the period unrecognizeable. This script is meant to be used to test a
            string length minimization script for accuracy.

    Github: https://github.com/zacharyrkennedy/RandomSinePeriodGenerator

"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter as xl
import random as r
import os
import openpyxl

# Randomzies Seed
r.seed()

# Define function for sin curve
def sin(f, time, amp):
   return amp*m.sin(2*m.pi*f*time)

# Output final sinecurve
def finalOutput(period):

    # Read Output1 excel file and add columns to two lists
    df = pd.read_excel('output1.xlsx')
    t1 = df['Time (s)'].tolist()
    m1 = df['Magnitude'].tolist()

    # Read Output2 excel file and add columns to two lists
    df = pd.read_excel('output2.xlsx')
    t2 = df['Time (s)'].tolist()
    m2 = df['Magnitude'].tolist()

    # Read Output3 excel file and add columns to two lists
    df = pd.read_excel('output3.xlsx')
    t3 = df['Time (s)'].tolist()
    m3 = df['Magnitude'].tolist()

    # Create empty lists for the final time and magnitude points
    t_final = []
    m_final = []

    # Loop through all of the 3 previous file lists, and add them to our final lists
    for i in range(len(t1)):
        t_final.append(t1[i])
        t_final.append(t2[i])
        t_final.append(t3[i])

        m_final.append(m1[i])
        m_final.append(m2[i])
        m_final.append(m3[i])

    # Create output excel worksheet
    workbook = xl.Workbook('outputFinal.xlsx')

    # Add worksheet to workbook
    worksheet = workbook.add_worksheet()

    # Set starting row for data
    row = 1

    # Create column titles
    worksheet.write_string(0, 0, 'Time (s)')
    worksheet.write_string(0, 1, 'Magnitude')
    worksheet.write_string(0, 5, 'Actual Period (s)')

    # Write the "real" period to the excel spreadsheet
    worksheet.write(1, 5, period)

    # Add data to worksheet
    for i in range(len(t_final)):
        worksheet.write(row, 0, t_final[i])
        worksheet.write(row, 1, m_final[i])
        row += 1


    # Close workbook
    workbook.close()

    # Delete old unnecessary excel files
    os.remove('output1.xlsx')
    os.remove('output2.xlsx')
    os.remove('output3.xlsx')

    # Plot final graphs, commented out as it's mostly for testing
    #plt.scatter(t_final,m_final)
    #plt.show()

# Function that generates a sinecurve according to a period, then removes all of the points but a specified number
def generateData(filenumber, period):

    # Rate of how many data points are recorded per second
    sample_rate = 0.03333333333

    # Start time & end time for each data set
    start_time = 0
    end_time = period*4.23344

    # Amplitude of Period
    amp = 1

    # Period of curve in seconds
    T = period

    # Frequency of sine curve. Depends on period
    f = 1/T

    # Generate the time data points
    time = np.arange(start_time, end_time, 1/sample_rate)

    # Generate the sine curve outputs
    sinewave = amp * np.sin(2 * np.pi * f * time) + 10

    # Convert Numpy arrays to python lists
    new_time = time.tolist()
    new_sinewave = sinewave.tolist()

    # Change the number of points per 3 data sets based on if the period is shorter or longer
    if period < 100000:
        numberPoints = 4
    elif period >= 100000:
        numberPoints = 5

    # Randomly remove data points
    for i in range(int(len(new_time)-numberPoints)):
        random_index = np.random.randint(0, int(len(new_time)))
        new_time.pop(random_index)
        new_sinewave.pop(random_index)

    # Create output excel worksheet
    workbook = xl.Workbook('output' + str(filenumber) + '.xlsx')

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
    #plt.scatter(new_time, new_sinewave)
    #plt.show()

    # Show the true period graph. Commented out, mostly for testing purposes
    #if filenumber == 3:
        #plt.scatter(time, sinewave)
        #plt.show()

# Generate a random period between one day and 4 days but in seconds
rand_Period = r.randint(43200,345600)

# Print the actual period to the console
print("The actual period of the curve is: " + str(rand_Period) +"s or " + str(rand_Period/86400) + " days")

# Generate 3 data sets with our randomly generated period
for i in range(3):
    generateData(i+1, rand_Period)

# Generate the final output excel file with all 3 data sets combined and the "real" period listed
finalOutput(rand_Period)