import sys
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 26
try:
    while True:
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))
        time.sleep(10)
except:
    print ("Ocurrio un Error")
