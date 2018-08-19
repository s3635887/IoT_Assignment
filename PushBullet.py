#!/usr/bin/env python3
import requests
import json
import os
from sense_hat import SenseHat

ACCESS_TOKEN="o.QXA7Z8fuI1nfW793pN45mH9P9Np22Csg"

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


def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def main():
    sense = SenseHat()
    temp1 = sense.get_temperature_from_humidity()
    temp2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    t = (t1+t2)/2
    t_corr = t - ((t_cpu-t)/1.5)
    t_corr = get_smooth(t_corr)
    temp = round(t_corr,1)
    if temp < 23.0:
        temp = str(temp)
        ip_address = os.popen('hostname -I').read()
        send_notification_via_pushbullet(ip_address, "The temperature is "+temp+" *C. Please keep some warm cloths with you.")
    else:
        temp = str(temp)
        ip_address = os.popen('hostname -I').read()
        send_notification_via_pushbullet(ip_address,"The temperature is : "+temp+" *C. Quite Warm.")
#Execute
main()
