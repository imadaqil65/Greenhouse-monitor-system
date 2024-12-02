from cProfile import run
from flask import Flask, render_template
from datetime import date, datetime
from CustomPymata4 import *
import time, json, csv
from operator import delitem
board = CustomPymata4(baud_rate=57600, com_port = "COM7")

board.set_pin_mode_dht(12, sensor_type=11, differential=.05)
board.set_pin_mode_analog_input(2)

def temp():
    # temperature = 1
    temperature=board.dht_read(12)[1]
    return temperature

def humid():
    # humidity = 1
    humidity= board.dht_read(12)[0]
    return humidity

def light():
    # ldrVal=1
    ldrVal= board.analog_read(2)[0]
    return ldrVal

def date_time():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time

app = Flask(__name__)

@app.route("/post_data", methods=['POST']) 

def receive_data():
# def index():
#     global temperaturelist, humiditylist, lightlist

#     return render_template("index.html", Title="Flask server", lig=light(), tem=temp(),  hum=humid(), date_time=date_time(),
#                             avgtem=format(sum(temperaturelist)/(len(temperaturelist)-1),".2f"), mintem=format(min(i for i in temperaturelist if i > 1),".2f"),
#                             maxtem=format(max(temperaturelist),".2f"), tlist=temperaturelist, avghum=format(sum(humiditylist)/(len(humiditylist)-1),".1f"),
#                             minhum=min(i for i in humiditylist if i > 1), maxhum=max(humiditylist), hlist=humiditylist,
#                             avglig=round(sum(lightlist)/(len(lightlist)-1)), minlig=min(i for i in lightlist if i > 1),
#                             maxlig=max(lightlist), llist=lightlist)
    
    with open('stats.csv', 'r', newline='') as file: 
        reader = csv.reader(file)
        temperature=[]
        brightness=[]
        humidity=[]
        header = next(reader)
        for row in reader:
            tempt=row[1]
            temperature.append(tempt)
        for row in reader:
            brig=row[1]
            brightness.append(brig)
        for row in reader:
            humi=row[1]
            humidity.append(humi)
        avr=0
        avg=0
        ave=0
        for i in range(len(temperature)):
            avr+=float(temperature[i])
        avr=avr/len(temperature)
        for i in range(len(brightness)):
            avg+=float(brightness[i])
        avg=avg/len(temperature)
        for i in range(len(temperature)):
            ave+=float(humidity[i])
        ave=ave/len(humidity)
        return render_template("index.html", Title="Flask server", lig=light(), tem=temp(),  hum=humid(), date_time=date_time(),
                                maxtem=max(temperature), mintem=min(temperature),avgtem=int(avr),avgbri=int(avg),avghum=int(ave))

'''@app.route("/post_data", methods=['POST']) 
def receive_data():
'''

if __name__=="__main__":
    app.run() 
else: 
    print("Dont import me")
    
