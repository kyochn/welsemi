
import time
import picamera
import RPi.GPIO as GPIO
from datetime import datetime

# インターバル ５秒
INTERVAL = 5

# スリープタイム
SLEEPTIME = 1

# 使用するGPIO
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

if __name__ == '__main__':
    try:
        print ("終了:ctrl+c")
        while True:
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                with picamera.PiCamera() as camera:
                    camera.resolution = (1024, 768)
                    camera.start_preview()
                    timestr = datetime.now().strftime('%Y%m%d%H%M%S')
                    camera.capture(timestr+'.jpg')
            else:
                time.sleep(SLEEPTIME)
    except KeyboardInterrupt:
        print("終了")
    finally:
        GPIO.cleanup()