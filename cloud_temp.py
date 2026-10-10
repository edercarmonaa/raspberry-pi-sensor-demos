import http.client
import os
import time
import urllib.parse

import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 26
thingspeak_api_key = os.getenv("THINGSPEAK_API_KEY")

if not thingspeak_api_key:
  raise RuntimeError("THINGSPEAK_API_KEY environment variable is required")

while True:
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
  params = urllib.parse.urlencode({'field1': temperatura, 'field2': humedad, 'key': thingspeak_api_key})
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
  conn = http.client.HTTPConnection("api.thingspeak.com:80")
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(response.status, response.reason)
   data = response.read()
   conn.close()
  except:
   print("connection failed")
  time.sleep(2)
