import picamera


camara = picamera.PiCamera()
camara.resolution = (640, 480)
camara.start_preview()
camara.start_recording('video.h264')
camara.wait_recording(60)
camara.stop_recording()
