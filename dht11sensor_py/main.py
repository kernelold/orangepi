#!/usr/bin/env python
from flask import Flask,render_template

from pyA20.gpio import gpio
from pyA20.gpio import port
import dht11
import time



PIN2 = port.PA6
gpio.init()


app = Flask(__name__)
@app.route("/")
def index():
  raw = dht11.DHT11(pin=PIN2)
  data = raw.read()
  if data.humidity == 0:
    print(data.humidity)
    while data.humidity == 0:
      time.sleep(1)
      raw_late = dht11.DHT11(pin=PIN2)
      data_late = raw_late.read()
      print(str(data_late.humidity) + ' late')
      data = data_late
    return render_template('dht11.html',data=data)
  else:
    return render_template('dht11.html',data=data)
    
  gpio.cleanup(raw)

if __name__ == "__main__":
  app.run(host='::',debug=True)

