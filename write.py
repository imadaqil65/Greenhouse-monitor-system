from cProfile import run
from flask import Flask
from flask import render_template
from datetime import date, datetime
import random 
from CustomPymata4 import *
import csv
import time
from operator import delitem

board = CustomPymata4(baud_rate = 57600, com_port = "COM7")
board.set_pin_mode_dht(12, sensor_type=11, differential=.05)
board.set_pin_mode_analog_input(2)


while True:
    time.sleep(1)
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    humidity = board.dht_read(12)[0]
    temperature = board.dht_read(12)[1]
    ldrVal = board.analog_read(2)[0]
    result = [date_time, temperature, humidity, ldrVal]
    with open ('stats.csv','a', newline='', ) as filevar:
        writer = csv.writer(filevar)
        writer.writerow(result)