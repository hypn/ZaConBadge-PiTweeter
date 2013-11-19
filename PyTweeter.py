#!/usr/bin/env python
import sys
import serial
from twython import Twython

CONSUMER_KEY = 'Vg2rmgS1MxSG........'
CONSUMER_SECRET = 'kS9l7meJaGKDQDlMrLeSyIvXiCy4yovLPg........'
ACCESS_KEY = '2186052710-x7BTIHcp2hCCzEEAgcFBW64PwCLwLpx........'
ACCESS_SECRET = '6RcHXhS2R5kJ2zi1R6C0h0cxqHElVFP4PjcVK........'

ser = serial.Serial('/dev/ttyACM0', 9600)
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

while True:
        #message = sys.argv[1]
        message = ser.readline()
        if ('tweet:' in message):
                tweet = message.replace('tweet:', '').rstrip()
                print tweet
                try:
                        api.update_status(status=tweet)
                except Exception:
                        pass

#while True:
        #print ser.readline()
        #api.update_status(status=ser.readline())
