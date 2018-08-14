#!/usr/bin/env python3

import time
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/assignment/assignment1.db'
sampleFreq = 1 # time in seconds

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    sense.show_message('show this message')
    temp = sense.get_temperature()
    humidity = sense.get_humidity()	
    if temp is not None:
        temp = round(temp, 1)
    if humidity is not None:
        humidity = round(humidity, 1)
        logData (temp, humidity)
        sense.show_message('The program is working in cron ')
# log sensor data on database
def logData (temp, humidity):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO ass1_data values(datetime('now','localtime'), (?), (?))",(temp,humidity))
    conn.commit()
    conn.close()
# main function
def main():
    for i in range (0,3):
        getSenseHatData()
        time.sleep(sampleFreq)
# Execute program 
main()
