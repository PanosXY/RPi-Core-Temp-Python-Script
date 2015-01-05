import plotly.plotly as py
import datetime
import time
import os

py.sign_in("username", "APIkey") #Your Username and API Key
STREAM_TOKEN = 'token' 			 #Your Streaming API token

s = py.Stream(STREAM_TOKEN)
s.open()

while True:
	x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')				  #Get Date & Time
	y = os.popen("/opt/vc/bin/vcgencmd measure_temp | cut -b 6- | cut -b -4") #Get Core Temp
	y = y.read()

	s.write(dict(x=x,y=y)) #Push data to Streaming API

	time.sleep(900)	#15min

s.close