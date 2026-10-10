import time
import picamera

camara = picamera.PiCamera()
camara.resolution=(640,480)
camara.start_preview()
time.sleep(2)

for archivo in camara.capture_continuous('img{counter:03d}.jpg'):
    print("Captura %s" % archivo)
    time.sleep(10)
