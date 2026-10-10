import picamera
import time

camara = picamera.PiCamera()
camara.resolution=(640,480)
camara.start_preview()
time.sleep(2)
camara.capture('foto.jpg')

