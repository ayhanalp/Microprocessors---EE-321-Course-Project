'''
Ayhan Alp Aydeniz - Kemal Akçay
Adapted from the original code written by Adrian Rosebrock
Visit original post: https://www.pyimagesearch.com/2016/05/09/opencv-rpi-gpio-and-gpio-zero-on-the-
raspberry-pi/
'''
from __future__ import print_function
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import RPi.GPIO as GPIO
redLed = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)
colorLower = (0, 0, 0)
colorUpper = (90, 90, 90)
GPIO.output(redLed, GPIO.LOW)
ledOn = False
while True:
frame = vs.read()
frame = imutils.resize(frame, width=500)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, colorLower, colorUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None
if len(cnts) > 0:
c = max(cnts, key=cv2.contourArea)
((x, y), radius) = cv2.minEnclosingCircle(c)
M = cv2.moments(c)center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
if radius > 10:
cv2.circle(frame, (int(x), int(y)), int(radius),
(0, 255, 255), 2)
cv2.circle(frame, center, 5, (0, 0, 255), -1)
if not ledOn and GPIO.input(4)==0:
GPIO.output(redLed, GPIO.HIGH)
ledOn = True
elif GPIO.input(4)==0:
GPIO.output(redLed, GPIO.LOW)
ledOn = False
elif ledOn or GPIO.input(4)==0:
GPIO.output(redLed, GPIO.LOW)
ledOn = False
cv2.imshow("AAA - KA", frame)
key = cv2.waitKey(1) & 0xFF
if key == ord("q"):
break
print("\n Demo of the project is done - EE 321 \n")
GPIO.cleanup()
cv2.destroyAllWindows()
vs.stop()
