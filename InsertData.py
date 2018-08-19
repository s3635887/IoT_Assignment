#!/usr/bin/env python3
import os
import time
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/assignment/assignment1.db'
sampleFreq = 1 # time in seconds

# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    temp_cpu = get_cpu_temp()
    humidity = sense.get_humidity()

# calculates the real temperature compesating CPU heating
    t = (t1+t2)/2
    temp_corr = t - ((temp_cpu-t)/1.5)
    temp_corr = get_smooth(temp_corr)
    if temp_corr is not None:
       temp_corr = round(temp_corr, 1)
    if humidity is not None:
        humidity = round(humidity, 1)
        logData (temp_corr, humidity)
       # sense.show_message('.')
# log sensor data on database
def logData (temp, humidity):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO ass1_data values(datetime('now','localtime'), (?), (?))",(temp,humidity))
    conn.commit()
    conn.close()
# main function
def main():
    for i in range (0,40):
        getSenseHatData()
       # time.sleep(sampleFreq)
# Execute program 
main()
