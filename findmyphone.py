#!/usr/bin/env python3
import bluetooth
import os
import time
from sense_hat import SenseHat

# Main function
def main():
    user_name = input("Enter your name: ")
    device_name = input("Enter the name of your phone: ")
    search(user_name, device_name)

# Search for device based on device's name
def search(user_name, device_name):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        for mac_address in nearby_devices:
            if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                device_address = mac_address
                break
       # if os.path.exists("demo.txt") not True:
           # f = open("demo.txt","x")
        if device_address is not None:
            print("found")
            print(device_address)
            f = open("demo.txt","r")
            mac_address_present = False
            for line in f:
           # mac_address = (str)mac_address
               if line == mac_address:
                    mac_address_present = True
                    print("Hey {}! Welcome back".format(user_name))
                    break
            if mac_address_present == False:       
                f1 = open("demo.txt","a")
                f1.write(mac_address)
                print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
            #sense = SenseHat()
            #temp = round(sense.get_temperature(), 1)
            #port = 1
            #print("Hi {}! Current Temp is {}*c".format(user_name, temp))
        else:
            print("Could not find target device nearby...")

#Execute program
main()
