Core-Temperature-Python-Script
==============================

This python script reads the temperature of the core of Raspberry Pi (or every linux machine) and 
pushes it to the Streaming API of https://plot.ly/ every 15 minutes to create a real-time scatter plot.

![alt tag](https://github.com/PanosXY/RPi-Core-Temp-Python-Script/blob/master/raspberry_pi_core_temperature.png)

First run once initial_plot.py to create the scatter plot with your layout options:

        python initial_plot.py

Now you have to run streaming_plot.py to push the core temperature to the API:

        python streaming_plot.py
 
At last you can modify your crontab to run this script on reboot. Open crontab by:

        sudo crontab -e
and put this in the end:

        @reboot sudo python /path/of/streaming_plot.py &
