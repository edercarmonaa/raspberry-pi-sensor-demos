import picamera
import picamera.array
import time
import cv2

camara = picamera.PiCamera()
camara.resolution=(640,480)
rawCapture = picamera.array.PiRGBArray(camara)

time.sleep(0.1)
camara.capture(rawCapture, format="bgr")
imagen= rawCapture.array

time.sleep(0.1)

cv2.imshow("Image", imagen)
cv2.waitKey(0)
